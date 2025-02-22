#Classe base usuário para herança 

class Usuario:
    def __init__(self,  nome, email, matricula, tipo,  livrosAlugados=[], qtdLivrosAlugados=3):
        #Atributos privados para encapsulamento
        self.__nome = nome
        self.__email = email
        self.__matricula = matricula
        self.__tipo = tipo
        self.__livrosAlugados = livrosAlugados
        self.__qtdLivrosAlugados = qtdLivrosAlugados

    #Métodos para acessar os atributos privados no encapsulamento
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

    #Método para cadastrar o livro na lista de livros que o usuário pegou emprestado
    def addLivroAlugado(self, usuario, livro):
        self.getLivrosAlugados().append(livro)
        self.__qtdLivrosAlugados += 1
        livro.setDisponibilidade()
        print(f'Livro alugado para {usuario.getNome()}\n')
    
    #Método que será sobrescrito com polimorfismo
    def validarEmprestimo(self):
        return True

    #Método set para modificar o atributo da quantidade de livros que foram alugados
    def setQtdLivrosAlugados(self, QtdLivrosAlugados):
        self.__qtdLivrosAlugados = QtdLivrosAlugados

#Classe professor que herda a Classe usuário
class Professor(Usuario):
    def __init__(self, nome, email, matricula, tipo='Professor', livrosAlugados=[], qtdLivrosAlugados=0):
        super().__init__(nome, email, matricula, tipo, livrosAlugados, qtdLivrosAlugados)
    
    #Classe para sobresecrever o método do usuário com polimorfismo alterando o limite de emprestimos para cada usuário
    def validarEmprestimo(self):
        if self.getQtdLivrosAlugados() < 5:
            return True
        else:
            return False

#Classe estudante que herda a Classe usuário
class Estudante(Usuario):
    def __init__(self, nome, email, matricula, tipo='Estudante',  livrosAlugados=[], qtdLivrosAlugados=0):
        super().__init__(nome, email, matricula, tipo, livrosAlugados, qtdLivrosAlugados)
    
    #Classe para sobresecrever o método do usuário com polimorfismo alterando o limite de emprestimos para cada usuário
    def validarEmprestimo(self):
        if self.getQtdLivrosAlugados() < 3:
            return True
        else:
            return False