class Usuario:
    def __init__(self,  nome, email, matricula, tipo,  livrosAlugados=[], qtdLivrosAlugados=0):
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
        return self.__qtdLivrosAlugados

    def addLivroAlugado(self, livro):
        self.getLivrosAlugados().append(livro)
        self.__qtdLivrosAlugados += 1
        livro.setDisponibilidade()
        print('Livro alugado!')

    # def realizarEmprestimo(livro, usuarioMatricula, allLivros, allUsers):
    #     emprestado = None
    #     emprestadoPara = None
    #     for livrobusca in allLivros:
    #         if livro == livrobusca.getTitulo():
    #             emprestado = livrobusca
    #             break
    #     else:
    #         print('Livro não encontrado!')
    #         return
        
    #     for usuariobusca in allUsers:
    #         if str(usuarioMatricula) == str(usuariobusca.getMatricula()):
    #             emprestadoPara = usuariobusca
    #             break
    #     else:
    #         print('Usuário não encontrado!')
        
    #     if emprestado.getDisponivel() == False:
    #         print('Esse livro está indisponível!')
    #         return

    #     if emprestadoPara.getTipo() == 'Professor':
    #         if Professor.validarEmprestimo(emprestadoPara) == True:
    #             emprestadoPara.getLivrosAlugados().append(emprestado)
    #             emprestadoPara.__qtdLivrosAlugados += 1
    #             emprestado.disponivel = False
    #             print(f'Livro emprestado para {emprestadoPara.getNome()}')

    #         elif Professor.validarEmprestimo(emprestadoPara) == False:
    #             print('O livro não foi emprestado porque o usuário excedeu o limite de empréstimos(5)')
    
    def validarEmprestimo(self):
        return True

class Professor(Usuario):
    def __init__(self, nome, email, matricula, tipo='Professor', livrosAlugados=[], qtdLivrosAlugados=0):
        super().__init__(nome, email, matricula, tipo, livrosAlugados, qtdLivrosAlugados)

        self.__limiteEmprestimos = 5
    
    def getLimiteEmprestimos(self):
        return self.__limiteEmprestimos
    
    def validarEmprestimo(self):
        if len(self.getLivrosAlugados()) <= 5:
            return True
        else:
            return False

class Estudante(Usuario):
    def __init__(self, nome, email, matricula, tipo='Estudante',  livrosAlugados=[], qtdLivrosAlugados=0):
        super().__init__(nome, email, matricula, tipo, livrosAlugados, qtdLivrosAlugados)

        self.__limiteEmprestimos = 3
    
    def getLimiteEmprestimos(self):
        return self.__limiteEmprestimos
    
    def validarEmprestimo(self):
        if len(self.getLivrosAlugados()) <= 3:
            return True
        else:
            return False