import sqlite3
from funcionarios import Funcionario
from storege import ManagerDataBase
from re import sub
import os


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
            "INSERT INTO funcionarios VALUES (?, ?, ?, ?, ?, ?, ?, ?);",
                                                (Funcionario.getCpf, Funcionario.getNome, Funcionario.getEnder,
                                                Funcionario.getCargo,      Funcionario.getSalario, Funcionario.getDataA,
                                                Funcionario.getDataN,
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

    def __init__(self, cpf=0):
        self.__cpf = cpf


    def _ler_todos_funcionarios(self):
        conn = sqlite3.connect('Database.db')
        connection = conn.cursor()
        dados = connection.execute('SELECT * FROM funcionarios')
        return dados.fetchall()
    

    def mostra_todos_funcionarios(self):
        lista = self._ler_todos_funcionarios()
        
        print("-" * 150)
        for dado in lista:
            print('CPF:{} | Nome:{:19s} | Endereço:{:10s} | Cargo:{:16s} | Salario:{:.2f} | Data de admição{:10s} | Data de nacimento: {:10s} '.format(
                dado[0],dado[1],dado[2], dado[3], dado[4],dado[5],dado[6]))


    def mostrar(self):
        dados = self._mostrar_funcionario(self.__cpf)
        if dados != None:
            print('Usuario encontrado')
            print(f'CPF: {dados[0]}') 
            print(f'Nome: {dados[1]} ') 
            print(f'Endereco: {dados[2]}')
            print(f'Cargo: {dados[3]}') 
            print(f'Salario: R${dados[4]}')
            print(f'Data de Nascimento: {dados[5]}')

            return dados
        return None

    def _mostrar_funcionario(self,cpf):
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
        return None


            
class AlterarDados(MostraDados):

    def __init__(self, cpf, dados, campo, resul_pesquisa = ''):
        self.__cpf = cpf
        self.__dado = dados
        self.__campo = campo   
        self.resul_pesquisa = resul_pesquisa
        
    def alterar(self):
        dados = self.__alterar_dados(self.resul_pesquisa,self.__cpf, self.__dado, self.__campo)
        return dados

    def mostra(self):
        dados = self._mostrar_funcionario(self.__cpf)
        return dados

    
    def __alterar_dados(self, resul_pesquisa, cpf, dados, campo):
        print('oi')
        if resul_pesquisa != None:
            print('Entrei')
            print(dados)
            conn = sqlite3.connect('Database.db')
            connection = conn.cursor()
            connection.execute(f"UPDATE funcionarios SET {campo} = ? WHERE cpf = ?",(dados, cpf))
            conn.commit()
            conn.close
            print('Alterarados ')
            return True
        print('Não existe cliente  com o id informado')
        return False

        

class ExcluirDados(MostraDados):

    def __init__(self, cpf):
        self.__cpf = cpf


    def excluir(self):
        self._excluir_dados(self.__cpf)

    def _excluir_dados(self, cpf):
        cpf = self._remove_caracteres_especiais(cpf)
        dados = self._mostrar_funcionario(cpf)

        if dados != None:
            conn = sqlite3.connect('Database.db')
            connection = conn.cursor()
            connection.execute("DELETE FROM funcionarios WHERE cpf = ?",(cpf,))
            conn.commit()
            conn.close()
            print('Usuario delete com sucesso')
        else:
            print('Funcionario não cadastrado')

    
    def _remove_caracteres_especiais(self,cpf):
        cpf = sub('[^0-9]', '', cpf)
        return cpf

    