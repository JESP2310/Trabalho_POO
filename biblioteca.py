#Importações dos outros arquivos para modularização

from Livros import *
from usuarios import *
from emprestimos import *

#Class biblioteca para o gerenciamento do sistema
class Biblioteca:
    def __init__(self):
        #Atributos privados para encapsulamento
        self.__livros = []
        self.__users = []
        self.__emprestimos = []
        self.__qtdLivros = 0
        self.__qtdmatriculas = 0
    
    #Métodos get para acessar os atributos privados
    def getLivros(self):
        return self.__livros

    def getUsers(self):
        return self.__users
    
    def getEmprestimos(self):
        return self.__emprestimos
    
    #Método para listar todos os livros da biblioteca
    def listarLivros(self):
        if not self.__livros:
            print('Não há nenhum livro!')
            return
        print('\nTitulo - Autor - Ano - Código - Disponibilidade')
        for i in self.getLivros():
            if Livro.getDisponivel(i) == True:
                print(f'{Livro.getTitulo(i)} - {Livro.getAutor(i)} - {Livro.getAno(i)} - {Livro.getCodigo(i)} - Disponível')
            else:
                print(f'{Livro.getTitulo(i)} - {Livro.getAutor(i)} - {Livro.getAno(i)} - {Livro.getCodigo(i)} - Indisponível')
        print('\n')
    
    #Método para pesquisar livros por nome ou autor
    def pesquisarLivros(self, pesquisa):
        if not self.__livros:
            print('Não há nenhum livro!')
            return
        j = 0
        print('\nTitulo - Autor - Ano - Código - Disponibilidade')
        for i in self.getLivros():
            if (pesquisa in Livro.getTitulo(i)) or (pesquisa in Livro.getAutor(i)):
                if Livro.getDisponivel(i) == True:
                    print(f'{Livro.getTitulo(i)} - {Livro.getAutor(i)} - {Livro.getAno(i)} - {Livro.getCodigo(i)} - Disponível')
                    j = j+1
                else:
                    print(f'{Livro.getTitulo(i)} - {Livro.getAutor(i)} - {Livro.getAno(i)} - {Livro.getCodigo(i)} - Indisponível')
                    j = j+1
        if j == 0:
            print('Nenhum resultado encontrado!\n')
        
    #Método para cadastrar um novo livro
    def cadastrarLivro(self):
            self.__qtdLivros += 1
            livro = Livro(input('Digite o nome do livro: '), input('Digite o autor do livro: '), input('Digite o ano de publicação livro: '), self.__qtdLivros)
            self.__livros.append(livro)
            print('\nLivro cadastrado!\n')

    #Método para cadastrar um novo usuário
    def cadastrarUsuário(self):
        self.__qtdmatriculas += 1
        tipoUsuario = input('Digite o tipo de usuário a ser cadastrado:\n[1]Estudante\n[2]Professor\n')
        if tipoUsuario == '1':
            usuario = Estudante(input('Digite o nome do usuário: '), input('Digite o email do usuário: '), str(self.__qtdmatriculas))
            self.__users.append(usuario)
            print('Estudante cadastrado(a)!')
        elif tipoUsuario == '2':
            usuario = Professor(input('Digite o nome do usuário: '), input('Digite o email do usuário: '), str(self.__qtdmatriculas))
            self.__users.append(usuario)
            print('Professor(a) cadastrado(a)!')
    
    #Método para listar usuários com filtro para: Professor ou Estudante ou todos os usuários
    def listarUsuarios(self):
        if not self.__users:
            print('Não há nenhum usuário!')
            return
        tipoUsuarios = input('Digite o tipo de usuarios que voce quer listar(Ordem de matrículas):\n[1]Estudantes\n[2]Professores\n[3]Todos os usuários\n')
        print('\nNome - Email - Matrícula - Tipo de usuário - Livros alugados')
        if tipoUsuarios == '1':
            for usuario in self.__users:
                if usuario.getTipo() == 'Estudante':
                    print(f'{usuario.getNome()} - {usuario.getEmail()} - {usuario.getMatricula()} - {usuario.getTipo()} - {usuario.getQtdLivrosAlugados()} Livros alugados')
        
        elif tipoUsuarios == '2':
            for usuario in self.__users:
                if usuario.getTipo() == 'Professor':
                    print(f'{usuario.getNome()} - {usuario.getEmail()} - {usuario.getMatricula()} - {usuario.getTipo()} - {usuario.getQtdLivrosAlugados()} Livros alugados')
            print('\n')
        elif tipoUsuarios == '3':
            for usuario in self.__users:
                print(f'{usuario.getNome()} - {usuario.getEmail()} - {usuario.getMatricula()} - {usuario.getTipo()} - {usuario.getQtdLivrosAlugados()} Livros alugados')
            print('\n')
        else:
            print('Opção inválida!')
    
    #Método para deletar usuário por número de matrícula
    def deletarUsuário(self, usuarioMatricula):
        cont = 0
        for usuario in self.__users:
            if str(usuario.getMatricula()) == str(usuarioMatricula):
                self.__users.pop(cont)
                print('Usuário deletado!')
                break
            cont += 1
        else:
            print('Matrícula inválida!')
        
    #Método para devolver o livro para a biblioteca
    def devolverLivro(self, usuario, livro):
        UsuarioDevolver = None
        livroDevolver = None

        for Usuario in self.getUsers():
            if Usuario.getMatricula() == usuario:
                UsuarioDevolver = Usuario
                break

        if UsuarioDevolver == None:
            print('Usuário não encontrado!\n')
            return
        
        for Livro in UsuarioDevolver.getLivrosAlugados():
            if Livro.getTitulo() == livro:
                livroDevolver = Livro
                break

        if livroDevolver == None:
            print('Livro não encontrado!\n')
            return
        
        for emprestimo in self.getEmprestimos():
            if emprestimo.getLivro().getTitulo() == livroDevolver.getTitulo():
                livroDevolver.setDisponibilidade()
                break
        contador = 0
        AtualizarLivrosAlugados = UsuarioDevolver.getQtdLivrosAlugados()
        AtualizarLivrosAlugados = AtualizarLivrosAlugados - 1
        UsuarioDevolver.setQtdLivrosAlugados(AtualizarLivrosAlugados)
        for i in UsuarioDevolver.getLivrosAlugados():
            if i.getTitulo() == livroDevolver.getTitulo():
                break
            contador += 1
        UsuarioDevolver.getLivrosAlugados().pop(contador)

        print(f'Livro devolvido por {UsuarioDevolver.getNome()}\n')

    #Método para listar os livros alugados de um usuário(pesquisar por matrícula)
    def listarLivrosAlugados(self, usuario):
        user = None
        for Usuario in self.getUsers():
            if str(Usuario.getMatricula()) == str(usuario):
                user = Usuario
                if not Usuario.getLivrosAlugados():
                    print(f'O usuário {Usuario.getNome()} não está com nenhum livro emprestado')
                    return
                print(f'Livros alugados por {Usuario.getNome()}:')
        if user == None:
            print('Usuário não encontrado!\n')
            return
        for livro in user.getLivrosAlugados():
            print(f'{livro.getTitulo()} por {livro.getAutor()}')
            
    #Método para o menu com opções de gerenciamento
    def menu(self):
        print('Bem vindo! digite uma das opõçes para realizar a ação: ')
        while True:
            menu = input('\n[1]Gerenciar livros\n[2]Gerenciar usuários\n[3]Gerenciar empréstimos\n[4]Sair do sistema\n')
            if menu == '1':
                gerenciarLivros = input('\nEscolha uma opção para gerenciar os livros:\n[1]Cadastrar livro\n[2]Listar todos os livros\n[3]Pesquisar livro(s) por titulo ou autor\n')
                if gerenciarLivros == '1':
                    self.cadastrarLivro()
                    
                elif gerenciarLivros == '2':
                    self.listarLivros()

                elif gerenciarLivros == '3':
                    self.pesquisarLivros(input('Digite sua pesquisa: '))
                
                else:
                    print('Opção inválida!\n')

            elif menu == '2':
                gerenciarUsuarios = input('Escolha uma opção para gerenciar os Usuários: \n[1]Cadastrar usuário\n[2]Listar usuários\n[3]Deletar Usuário\n')
                if gerenciarUsuarios == '1':
                    self.cadastrarUsuário()

                elif gerenciarUsuarios == '2':
                    self.listarUsuarios()
                
                elif gerenciarUsuarios == '3':
                    self.deletarUsuário(int(input('Digite a matrícula do usuário a ser deletado: ')))
                
                else:
                    print('Opção inválida!\n')
            
            
            elif menu == '3':
                gerenciarEmprestimos = input('Escolha uma opção para gerenciar os Empréstimos:\n[1]Realizar empréstimo\n[2]Devolver livro\n[3]Consultar empréstimos o usuário\n')
                if gerenciarEmprestimos == '1':
                    livro, Usuario = input('Digite o Titulo do livro que será emprestado: '), input('Digite a matrícula do usuário que vai pegar o livro: ')
                    emprestado = None
                    emprestadoPara = None
                    for Livro in self.getLivros():
                        if Livro.getTitulo() == livro:
                            emprestado = Livro
                            for usuario in self.getUsers():
                                if str(usuario.getMatricula()) == str(Usuario):
                                    emprestadoPara = usuario
                                    self.getEmprestimos().append(Emprestimo(emprestadoPara, emprestado))
                                    break
                            else:
                                print('Usuario não encontrado!\n')
                                break
                    if emprestado == None:
                        print('Livro não encontrado!\n')
                            
                    
                
                elif gerenciarEmprestimos == '2':
                    self.devolverLivro(input('Digite a matrícula do usuário que irá devolver o livro: '), input('Digite o título do livro que o usuário irá devolver: '))
                
                elif gerenciarEmprestimos == '3':
                    self.listarLivrosAlugados(input('Digite a matrícula do usuário para listar seus livros: '))
                

                else:
                    print('Opção inválida!\n')
            
            elif menu == '4':
                print('Saindo...')
                return
            
            else:
                print('Opção inválida!\n')

biblioteca = Biblioteca()
biblioteca.menu()