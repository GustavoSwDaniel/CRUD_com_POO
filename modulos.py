import sqlite3
from funcionarios import Funcionario
from storege import ManagerDataBase


class Cadastrar(ManagerDataBase):

    
    def cadastrar_funcionario(self, Funcionario):
        conn = sqlite3.connect('Database.db')
        print('conectado')
        connection = conn.cursor()
        try:
            connection.execute(
            "INSERT INTO funcionarios VALUES (?, ?, ?, ?, ?, ?);",
                                                (Funcionario.getCpf, Funcionario.getNome, Funcionario.getEnder,       Funcionario.getSalario, Funcionario.getDataA,Funcionario.getSenha ))
        except sqlite3.ProgrammingError:
            print('Dados faltando todos os dados devem ser informados')
        
        if conn:
            conn.commit()
        else:
            print('error')

        if conn:
            conn.close()
            print('Conexão fechada.')
    

