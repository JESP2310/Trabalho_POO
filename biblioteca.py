from livros import *
from usuarios import *
livros = []
print('Bem vindo! digite uma das opõçes para realizara a ação: ')
while True:
    menu = input('[1] Cadastrar livro\n[2]')
    if menu == '1':
        livro1 = livro(input('Digite o nome do livro: '), input('Digite o autor do livro: '), input('Digite o ano de publicação livro: '), input('Digite o código do livro: '))
        print()
        livros.append(livro1)
        for livro1 in livros:
            print(livro1.titulo)