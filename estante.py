class Livro:
    def __init__(self, __titulo, __autor, __ano, __codigo, __disponivel=True):
        self.__titulo = __titulo
        self.__autor = __autor
        self.__ano = __ano
        self.__codigo = __codigo
        self.__disponivel = __disponivel

    def pesquisarLivros(pesquisa, livros):
        i = 0
        print('\nTitulo - Autor - Ano - Código')
        for livro in livros:
            if (pesquisa in livro.__titulo) or (pesquisa in livro.__autor):
                if livro.__disponivel == True:
                    print(f'{livro.__titulo} - {livro.__autor} - {livro.__ano} - {livro.__codigo} - Disponível\n')
                    i = i+1
                else:
                    print(f'{livro.__titulo} - {livro.__autor} - {livro.__ano} - {livro.__codigo} - Indisponível\n')
                    i = i+1              
        if i == 0:
            print('Nenhum resultado encontrado!')

    def listarLivros(livros):
        print('\nTitulo - Autor - Ano - Código')
        for livro in livros:
            if livro.__disponivel == True:
                print(f'{livro.__titulo} - {livro.__autor} - {livro.__ano} - {livro.__codigo} - Disponível\n')
            else:
                print(f'{livro.__titulo} - {livro.__autor} - {livro.__ano} - {livro.__codigo} - Indisponível\n')