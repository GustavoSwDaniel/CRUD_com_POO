import sqlite3

#Inicia e cria a tabela no banco de dados

class ManagerDataBase(object):

    def __init__(self):
        self.__conn = sqlite3.connect('Database.db')
        self.__connection = self.__conn.cursor()
        self.__conn.close()


    def create_database(self):  
        self.__conn = sqlite3.connect('Database.db')
        self.__connection = self.__conn.cursor()
        self.__connection.execute(""" 
        CREATE TABLE funcionarios (
                cpf                 INTEGE NOT NULL PRIMARY KEY,
                nome                TEXT NOT NULL,
                endereco            TEXT NOT NULL, 
                cargo               TEXT NOT NULL,
                salario             DECIMAL(10,5) NOT NULL,
                data_admicao        DATE NOT NULL,
                senha               TEXT NOT NULL
        );""")
        print('Successfully creata table')
        self.__conn.close()

    @property
    def get_conn(self):
        return self.__conn
        

try:
    create = ManagerDataBase()
    create.create_database()            
except sqlite3.OperationalError:
    pass