from Livros import *
from usuarios import *
estante = Estante([Livro('massa', 'louco', '2005', '40028922'), Livro('outro', 'maluco', '2010', '23102005')])
usuarios = [Usuario('Eric', 'joseeric2310@gmail.com', '564922', 'Professor', 2), Usuario('Jorge', 'jorge2310@gmail.com', '345667', 'Estudante', 1)]
print('Bem vindo! digite uma das opõçes para realizara a ação: ')
while True:
    menu = input('[1]Gerenciar livros\n[2]Gerenciar usuários\n[3]Gerenciar empréstimos\n')
    if menu == '1':
        gerenciarLivros = input('\nEscolha uma opção para gerenciar os livros:\n[1]Cadastrar livro\n[2]Listar todos os livros\n[3]Pesquisar livro(s) por titulo ou autor\n')
        if gerenciarLivros == '1':
            livro = Livro(input('Digite o nome do livro: '), input('Digite o autor do livro: '), input('Digite o ano de publicação livro: '), input('Digite o código do livro: '))
            Estante.livros.append(livro)
            print('\nLivro cadastrado!\n')

        elif gerenciarLivros == '2':
            Estante.listarLivros(estante)

        elif gerenciarLivros == '3':
            Estante.pesquisarLivros(estante, input('Digite sua pesquisa: '))
            
    elif menu == '2':
        gerenciarUsuarios = input('Escolha uma opção para gerenciar os livros: \n[1]Cadastrar usuário\n[2]Listar usuários\n')
        if gerenciarUsuarios == '1':
            tipoUsuario = input('Digite o tipo de usuário a ser cadastrado:\n[1]Estudante')
            usuario = Usuario(input('Digite o nome do usuário: '), input('Digite o email do usuário: '), input('Digite a matrícula do usuário'), input('Digite o tipo de usuário'))
            usuarios.append(usuario)
            print('estudante cadastrado(a)!')
        elif gerenciarUsuarios == '2':
            print('Nome - Email - Matrícula - Tipo de usuário - Livros alugados')
            for usuario in usuarios:
                Usuario.listarUsuarios(usuarios)