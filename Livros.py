class Livro:
    def __init__(self, titulo, autor, ano, codigo, disponivel=True):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
        self.__codigo = codigo
        self.__disponivel = disponivel

    def getTitulo(self):
        return self.__titulo
    
    def getAutor(self):
        return self.__autor

    def getAno(self):
        return self.__ano

    def getCodigo(self):
        return self.__codigo

    def getDisponivel(self):
        return self.__disponivel
        

class Estante:
    def __init__(self, livros):
        self.__livros = livros

    def getLivros(self):
        return self.__livros

    def listarLivros(self):
        print('\nTitulo - Autor - Ano - Código')
        for i in self.getLivros():
            if Livro.getDisponivel(i) == True:
                print(f'{Livro.getTitulo(i)} - {Livro.getAutor(i)} - {Livro.getAno(i)} - {Livro.getCodigo(i)} - Disponível')
            else:
                print(f'{Livro.getTitulo(i)} - {Livro.getAutor(i)} - {Livro.getAno(i)} - {Livro.getCodigo(i)} - Indisponível')
        print('\n')
    
    def pesquisarLivros(self, pesquisa):
        j = 0
        print('\nTitulo - Autor - Ano - Código')
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