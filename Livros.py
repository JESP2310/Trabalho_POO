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

    def setDisponibilidade(self):
        if self.getDisponivel() == True:
            self.__disponivel = False
        else:
            self.__disponivel = True
        return self.__disponivel