class Usuario:
    def __init__(self,  nome, email, matricula, tipo, livrosAlugados=0):
        self.__nome = nome
        self.__email = email
        self.__matricula = matricula
        self.__tipo = tipo
        self.__livrosAlugados = livrosAlugados

    def listarUsuarios(usuarios):
        for usuario in usuarios:
            print(f'{usuario.__nome} - {usuario.__email} - {usuario.__matricula} - {usuario.__tipo} - {usuario.__livrosAlugados} Livros alugados\n')

class Professor(Usuario):
    def __init__(self, nome, email, matricula, tipo='Professor', livrosAlugados=0):
        super().__init__(nome, email, matricula, tipo, livrosAlugados=0)


class Estudante(Usuario):
    def __init__(self, nome, email, matricula, tipo='Estudante', livrosAlugados=0):
        super().__init__(self, nome, email, matricula, tipo, livrosAlugados=0)