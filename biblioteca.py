from Livros import *
from usuarios import *
from emprestimos import *

class Biblioteca:
    def __init__(self):
        self.__livros = [Livro('massa', 'louco', '2005', 1), Livro('outro', 'maluco', '2010', 2)]
        self.__users = [Professor('Eric', 'joseeric2310@gmail.com', 1), Estudante('Jorge', 'jorge2310@gmail.com', 2)]
        self.__emprestimos = []
        self.__qtdLivros = 2
        self.__qtdmatriculas = 2
    
    def getLivros(self):
        return self.__livros

    def getUsers(self):
        return self.__users
    
    def getEmprestimos(self):
        return self.__emprestimos
    
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
    
    def pesquisarLivros(self, pesquisa):
        j = 0
        print('\nTitulo - Autor - Ano - Código - Disponibilidade')
        for i in self.getLivros():
            if (pesquisa in Livro.getTitulo(i)) or (pesquisa in Livro.getAutor(i)):
                if Livro.getDisponivel(i) == True:
                    print(f'{Livro.getTitulo(i)} - {Livro.getAutor(i)} - {Livro.getAno(i)} - {Livro.getCodigo(i)} - Disponível\n')
                    j = j+1
                else:
                    print(f'{Livro.getTitulo(i)} - {Livro.getAutor(i)} - {Livro.getAno(i)} - {Livro.getCodigo(i)} - Indisponível\n')
                    j = j+1
        if j == 0:
            print('Nenhum resultado encontrado!\n')
        
    
    def cadastrarLivro(self):
            self.__qtdLivros += 1
            livro = Livro(input('Digite o nome do livro: '), input('Digite o autor do livro: '), input('Digite o ano de publicação livro: '), self.__qtdLivros)
            self.__livros.append(livro)
            print('\nLivro cadastrado!\n')
    
    def cadastrarUsuário(self):
        self.__qtdmatriculas += 1
        tipoUsuario = input('Digite o tipo de usuário a ser cadastrado:\n[1]Estudante\n[2]Professor\n')
        if tipoUsuario == '1':
            usuario = Estudante(input('Digite o nome do usuário: '), input('Digite o email do usuário: '), self.__qtdmatriculas)
            self.__users.append(usuario)
            print('Estudante cadastrado(a)!')
        elif tipoUsuario == '2':
            usuario = Professor(input('Digite o nome do usuário: '), input('Digite o email do usuário: '), self.__qtdmatriculas)
            self.__users.append(usuario)
            print('Professor(a) cadastrado(a)!')
    
    def listarUsuarios(self):
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
        
        elif tipoUsuarios == '3':
            for usuario in self.__users:
                print(f'{usuario.getNome()} - {usuario.getEmail()} - {usuario.getMatricula()} - {usuario.getTipo()} - {usuario.getQtdLivrosAlugados()} Livros alugados')
        
        
        else:
            print('Opção inválida!')
    
    def deletarUsuário(self, usuarioMatricula):
        cont = 0
        for usuario in self.__users:
            if usuario.getMatricula() == usuarioMatricula:
                self.__users.pop(cont)
                print('Usuário deletado!')
                break
            cont += 1
        else:
            print('Matrícula inválida!')
        
        
    def menu(self):
        print('Bem vindo! digite uma das opõçes para realizar a ação: ')
        while True:
            menu = input('[1]Gerenciar livros\n[2]Gerenciar usuários\n[3]Gerenciar empréstimos\n')
            if menu == '1':
                gerenciarLivros = input('\nEscolha uma opção para gerenciar os livros:\n[1]Cadastrar livro\n[2]Listar todos os livros\n[3]Pesquisar livro(s) por titulo ou autor\n')
                if gerenciarLivros == '1':
                    self.cadastrarLivro()
                    
                elif gerenciarLivros == '2':
                    self.listarLivros()

                elif gerenciarLivros == '3':
                    self.pesquisarLivros(input('Digite sua pesquisa: '))
                
                else:
                    print('Opção inválida!')

            elif menu == '2':
                gerenciarUsuarios = input('Escolha uma opção para gerenciar os livros: \n[1]Cadastrar usuário\n[2]Listar usuários\n[3]Deletar Usuário\n')
                if gerenciarUsuarios == '1':
                    self.cadastrarUsuário()

                elif gerenciarUsuarios == '2':
                    self.listarUsuarios()
                
                elif gerenciarUsuarios == '3':
                    self.deletarUsuário(int(input('Digite a matrícula do usuário a ser deletado: ')))
                
                else:
                    print('Opção inválida!')
            
            
            elif menu == '3':
                gerenciarEmprestimos = input('Escolha uma opção para gerenciar os livros:\n[1]Realizar empréstimo\n[2]Devolver livro\n[3]Consultar empréstimos o usuário\n')
                if gerenciarEmprestimos == '1':
                    livro, Usuario = input('Digite o Titulo do livro que será emprestado: '), input('Digite a matrícula do usuário que vai pegar o livro: ')
                    emprestado = None
                    emprestadoPara = None
                    for Livro in self.getLivros():
                        if Livro.getTitulo() == livro:
                            emprestado = Livro
                            break
                    else:
                        print('Livro não encontrado!')
                    
                    for usuario in self.getUsers():
                        if str(usuario.getMatricula()) == str(Usuario):
                            emprestadoPara = usuario
                            break
                    else:
                        print('Usuario não encontrado!')

                    self.getEmprestimos().append(Emprestimo(emprestadoPara, emprestado))


            else:
                print('Opção inválida!')

biblioteca = Biblioteca()
biblioteca.menu()