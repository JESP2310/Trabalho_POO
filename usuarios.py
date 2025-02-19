class Usuario:
    def __init__(self,  nome, email, matricula, tipo,  livrosAlugados=[], qtdLivrosAlugados=3):
        self.__nome = nome
        self.__email = email
        self.__matricula = matricula
        self.__tipo = tipo
        self.__livrosAlugados = livrosAlugados
        self.__qtdLivrosAlugados = qtdLivrosAlugados

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
    
    def getQtdLivrosAlugados(self):
        return int(self.__qtdLivrosAlugados)

    def addLivroAlugado(self, usuario, livro):
        self.getLivrosAlugados().append(livro)
        self.__qtdLivrosAlugados += 1
        livro.setDisponibilidade()
        usuario.getLivrosAlugados().append(livro)
        print(f'Livro alugado para {usuario.getNome()}\n')
    
    def validarEmprestimo(self):
        return True

    def setQtdLivrosAlugados(self, QtdLivrosAlugados):
        self.__qtdLivrosAlugados = QtdLivrosAlugados

class Professor(Usuario):
    def __init__(self, nome, email, matricula, tipo='Professor', livrosAlugados=[], qtdLivrosAlugados=0):
        super().__init__(nome, email, matricula, tipo, livrosAlugados, qtdLivrosAlugados)
    
    def validarEmprestimo(self):
        if self.getQtdLivrosAlugados() < 5:
            return True
        else:
            return False

class Estudante(Usuario):
    def __init__(self, nome, email, matricula, tipo='Estudante',  livrosAlugados=[], qtdLivrosAlugados=0):
        super().__init__(nome, email, matricula, tipo, livrosAlugados, qtdLivrosAlugados)
    
    def validarEmprestimo(self):
        if self.getQtdLivrosAlugados() < 3:
            return True
        else:
            return False