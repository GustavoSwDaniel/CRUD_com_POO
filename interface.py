import os

# Interface

def header():
    print('*' * 50)
    print('Controle de funcionarios'.center(50))
    print('*' * 50)


def menu():
    os.system('clear')
    header()
    print('Meno princilpal'.center(50))
    print('*' * 50)
    print('1 - Cadastrar funcionario'.center(50))
    print('2 - Atualizar cadastro de funcionario'.center(50))
    print('3 - Verficar funcionario'.center(50))
    print('4 - Listar Todos os Funcionario'.center(50))
    print('5 - Excluir Funcionario'.center(50))


def header_cadastrar_funcionaro():
    os.system('clear')
    header()
    print('Cadastrar Funcionario'.center(50))
    print('*' * 50)


def header_atualizar_cadastro():
    os.system('clear')
    header()
    print('Cadastrar Funcionario'.center(50))
    print('*' * 50)


def header_verificar_funcionario():
    os.system('clear')
    header()
    print('Verificar Funcionario'.center(50))
    print('*' * 50)


def header_lista_funcionarios():
    os.system('clear')
    print('*' * 160)
    print('Controle de funcionarios'.center(160))
    print('*' * 160)
    print('Listar Todos os Funcionarios'.center(160))
    print('*' * 160)


def header_excluir_funcionario():
    os.system('clear')
    header()
    print('Excluir Funcionario'.center(50))
    print('*' * 50)

