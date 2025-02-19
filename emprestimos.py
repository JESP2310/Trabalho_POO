class Emprestimo:
    def __init__(self, usuario, livro):
        self.__usuario = usuario
        self.__livro = livro

        if not livro.getDisponivel():
            print('Livro indisponível!\n')
            return
        
        if not usuario.validarEmprestimo():
            print('O usuário está no limite de livros alugados!\n')
            return
        
        usuario.addLivroAlugado(usuario, livro)
    
    def getUsuario(self):
        return self.__usuario
    
    def getLivro(self):
        return self.__livro
    