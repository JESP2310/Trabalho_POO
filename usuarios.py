class Usuario:
    def __init__(self,  nome, email, matricula, tipo, livrosAlugados=0):
        self.__nome = nome
        self.__email = email
        self.__matricula = matricula
        self.__tipo = tipo
        self.__livrosAlugados = livrosAlugados
    
    def getNome(self):
        return self.__nome
    
    def getEmail(self):
        return self.__email
    
    def getMatricula(self):
        return self.__matricula
    
    def getTipo(self):
        return self.__tipo
    
    def getLivrosAlugados(self):
        return self.__livrosAlugados

class Professor(Usuario):
    def __init__(self, nome, email, matricula, tipo='Professor', livrosAlugados=0):
        super().__init__(nome, email, matricula, tipo, livrosAlugados)


class Estudante(Usuario):
    def __init__(self, nome, email, matricula, tipo='Estudante', livrosAlugados=0):
        super().__init__(nome, email, matricula, tipo, livrosAlugados)