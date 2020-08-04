import bcrypt

class Funcionario(object):

    def __init__(self, nome, endereco, cpf, cargo, salario, data_admicao, senha):
        self.__nome = nome
        self.__endereco = endereco
        self.__cpf = cpf
        self.__cargo = cargo
        self.__salario = salario
        self.__data_admicao = data_admicao
        self.__senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt(14))

    
    @property
    def getNome(self):
        return self.__nome


    @property
    def getEnder(self):
        return self.__endereco

    
    @property
    def getCpf(self):
        return self.__cpf
    
    @property
    def getCargo(self):
        return self.__cargo

    
    @property
    def getSalario(self):
        return self.__salario
    
    @property
    def getDataA(self):
        return self.__data_admicao

    @property
    def getSenha(self):
        return self.__senha

