#Classe empréstimo, para ser criado um objeto empréstimo associando o usuário e o livro emprestado

class Emprestimo:
    def __init__(self, usuario, livro):
        #Atributos privados para encapsulamento
        self.__usuario = usuario
        self.__livro = livro

        #Criação do emprestimo com condicionais para ele ser criado
        if not livro.getDisponivel():
            print('Livro indisponível!\n')
            return
        
        if not usuario.validarEmprestimo():
            print('O usuário está no limite de livros alugados!\n')
            return
        
        usuario.addLivroAlugado(usuario, livro)
    
    #Métodos para acessar os atributos no encapsulamento
    def getUsuario(self):
        return self.__usuario
    
    def getLivro(self):
        return self.__livro