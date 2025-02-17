class Emprestimo:
    def __init__(self, usuario, livro):
        self.__usuario = usuario
        self.__livro = livro

        if not livro.getDisponivel():
            print('Livro indisponível!')
            return
        
        if usuario.getQtdLivrosAlugados() >= usuario.getLimiteEmprestimos():
            print('O usuário está no limite de livros alugados!')
            return
        
        usuario.addLivroAlugado(livro)
    
    def getUsuario(self):
        return self.__usuario
    
    def getLivro(self):
        return self.__livro
    
    def devolverLivro(self):
        self.getLivro().disponivel = True
        