import sqlite3
from funcionarios import Funcionario
from storege import ManagerDataBase


class Cadastrar(object):

    def __init__(self, funcionario):
        self._funcionario = funcionario
    
    
    def cadastra_no_banco_de_dados(self):
        status = self.__cadastrar_funcionario(self._funcionario)

        if status == False:
            return False
    
    def __cadastrar_funcionario(self, Funcionario):
        conn = sqlite3.connect('Database.db')
        print('conectado')
        connection = conn.cursor()
        try:
            connection.execute(
            "INSERT INTO funcionarios VALUES (?, ?, ?, ?, ?, ?, ?);",
                                                (Funcionario.getCpf, Funcionario.getNome, Funcionario.getEnder,
                                                Funcionario.getCargo,      Funcionario.getSalario, Funcionario.getDataA,
                                                Funcionario.getSenha ))
        except sqlite3.ProgrammingError:
            print('Dados faltando todos os dados devem ser informados')
            return False
        
        conn.commit()
        conn.close

    @property
    def funcionario(self):
        return self._funcionario

    @funcionario.setter
    def funcionario(self, funcionario):
        self._funcionario = self.__cadastrar_funcionario(funcionario)  
        return
        

class MostraDados(object):

    def __init__(self, cpf):
        self.__cpf = cpf

    def mostra(self):
        dados = self.__mostar_dados(self.__cpf)
        return dados

    
    def __mostar_dados(self, cpf):
        conn = sqlite3.connect('Database.db')
        connection = conn.cursor()
        print('conectado')
        connection.execute(f"SELECT * FROM funcionarios WHERE cpf = {cpf}")
        
        c = connection.fetchone()
        print(c)

        if c != None:
            dados = []
            for linhas in c:
                dados.append(linhas)
            return dados
        else:
            print('CPF não localizado!')
            return None
        
    

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = self.__mostar_dados(cpf)

class AlterarDados():

    def __init__(self, cpf):
        self.__cpf = cpf
        
    def altera(self):
        dados = self.__alterar_dados(self.__cpf)
        return dados
    
    def __alterar_dados(self, cpf):
        # Aqui quero usar o método __mostar_dados que é chamado pelo método mostra da classe Mostrar Dados
        # return dados
        pass


    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = self.__alterar_dados(cpf)


    

    
    
        


