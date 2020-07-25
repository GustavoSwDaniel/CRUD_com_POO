from funcionarios import Funcionario
from modulos import Cadastrar
from storege import ManagerDataBase
import sqlite3



try:
    create = ManagerDataBase()
    create.create_database()
except sqlite3.DatabaseError:
    funcionario = Funcionario('Gustavo','Rua','2', 'chefe', 1500.00,'10/10/  2020', '154')
    cadastrar = Cadastrar()
    cadastrar.cadastrar_funcionario(funcionario)
