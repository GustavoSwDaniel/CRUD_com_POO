from funcionarios import Funcionario
from modulos import Cadastrar ,MostraDados, AlterarDados
from validacoes.validar_cpf import ValidaCpf
import time
import sqlite3
import os
import bcrypt
from re import sub

# Entrada de dados



def selecao():

    while True:
        opcao = int(input('Qual a sua opcão: '))
        if opcao == 1:
            cadastra_funcionario()
            break
        elif opcao == 2:
            atualiza_funcionario()
            break
        elif opcao == 3:
            verifica_funcionario()
            break
        elif opcao == 4:
            lista_funcionarios()
            break
        elif opcao == 5:
            exclui_funcionario()
            break

def cadastra_funcionario():
    os.system('clear')
    interface()
    
    nome = input('Infome o dado do funcionario: ')
    endereco = input('Informe o endereço do funcionario: ')
    cpf = input('Informe o cpf do funcionario: ')
    cpf = validar_cpf(cpf)
    cargo = input('Informe o cargo do funcionario: ')
    salario = input('Informe o salario do funcionario: ')
    data_nascimento = input('Informe a data de nacimento do funcioanrio: ')
    senha_do_funcionario = input('Infome a senha do funcionario')

    funcionario = Funcionario(nome, endereco, cpf, cargo , salario,data_nascimento, senha_do_funcionario)
    cadastra = Cadastrar(funcionario)
    status = cadastra.cadastra_no_banco_de_dados()

    if status == False:
        opcao = input('Deseja recomeçar ?? S/N:').upper()
        if opcao == 'S':
            cadastra_funcionario()



def atualiza_funcionario():
    os.system('clear')
    interface()


    cpf = input('Infomer o cpf para a alteração dos dados ')
    cpf = remove_caracteres_especiais(cpf)
    '''mostraDados = MostraDados(cpf)
    dados = mostraDados.alterar()'''
    nome = ''
    alterar = AlterarDados(cpf)
    dados = alterar.altera()
    
    if dados != None:
        print(f'1 - CPF: {dados[0]}') 
        print(f'2 - Nome: {dados[1]} ') 
        print(f'3 - Endereco: {dados[2]}')
        print(f'4 - Cargo: {dados[3]}') 
        print(f'5 - Salario: R${dados[4]}')
        print(f'6 - Data de Nascimento: {dados[5]}')
        print(f'7 - Voltar')

        opcao = input('Qual informação deseja alterar? ')
        if opcao == 1:
            novo_cpf = input('CPF: ')
            alterarDados = AlterarDados(novo_cpf)
        elif opcao == 2:
            nome = input('Nome: ')
            alterarDados = AlterarDados(nome)
        elif opcao == 3:
            novo_ender = input('Endereço: ')
            alterarDados = AlterarDados(novo_ender)
        elif opcao == 4:
            novo_cargo = input('Cargo: ')
            alterarDados = AlterarDados(novo_cargo)
        elif opcao == 5:
            novo_salario = input('Salario: ')
            alterarDados = AlterarDados(novo_salario)
        elif opcao == 6:
            data_nascimento = input('Data de nascimento: ')
            alterarDados = AlterarDados(data_nascimento)
        elif opcao == 7:
            menu()
    else:
        opcao = input('Deseja recomeçar ?? S/N:').upper()
        if opcao == 'S':
            atualiza_funcionario()


def verifica_funcionario():
    pass

def lista_funcionarios():
    pass

def exclui_funcionario():
    pass

#validações 

def remove_caracteres_especiais(cpf):
    cpf = sub('[^0-9]', '', cpf)
    return cpf

def validar_cpf(cpf):
    cpf = remove_caracteres_especiais(cpf)
    cpfVerificado = ValidaCpf(cpf)
    if not cpfVerificado.valida():
        print('CPF invalido!')
        time.sleep(1.5)
        opcao = input('Deseja recomeçar? S/N: ').upper()
        if opcao == 'S':
            cadastra_funcionario()
        else:
            print('Saindo...')
            time.sleep(1.5)
            exit()
    return cpf

# Interface


def interface():
    print('*' * 50)
    print('Controle de funcionarios'.center(50))
    print('*' * 50)

def menu():
    interface()
    print('Meno princilpal'.center(50))
    print('*' * 50)
    print('1 - Cadastrar funcionario'.center(50))
    print('2 - Atualizar cadastro de funcionario'.center(50))
    print('3 - Verficar funcionario'.center(50))
    print('4 - Listar Funcionario'.center(50))
    print('5 - Excluir Funcionario'.center(50))
    selecao()


menu()