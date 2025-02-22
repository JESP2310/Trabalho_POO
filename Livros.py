#Class livro para pegar atributos dos objetos livros

class Livro:
    def __init__(self, titulo, autor, ano, codigo, disponivel=True):
        #Atributos privados para encapsulamento
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
        self.__codigo = codigo
        self.__disponivel = disponivel

    #Métodos get para acessar os atributos privados
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

    #Método set para alternar entre emprestado e não emprestado no encapsulamento
    def setDisponibilidade(self):
        if self.getDisponivel() == True:
            self.__disponivel = False
        else:
            self.__disponivel = True
        return self.__disponivel