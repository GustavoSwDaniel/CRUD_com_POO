
class Funcionario(object):

    def __init__(self, nome, endereco, cpf, cargo, salario, data_admicao, senha):
        self.__nome = nome
        self.__endereco = endereco
        self.__cpf = cpf
        self.__salario = salario
        self.__data_admicao = data_admicao
        self.__senha = senha

    
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
    def getSalario(self):
        return self.__salario
    
    @property
    def getDataA(self):
        return self.__data_admicao

    @property
    def getSenha(self):
        return self.__senha

funcionario = Funcionario('Gustavo','Rua','88', 'chefe', 1500.00, '10/10/2020', '154')
