from funcionarios import Funcionario
from modulos import Cadastrar ,MostraDados, ExcluirDados, AlterarDados
from validacoes.validar_cpf import ValidaCpf
from interface import header, menu , header_atualizar_cadastro ,    header_cadastrar_funcionaro, header_excluir_funcionario, header_lista_funcionarios, header_verificar_funcionario
from re import sub
from datetime import date

import time



def selecao():
    menu()
    while True:
        opcao = int(input('Qual a sua opcão: '))
        if opcao == 1:
            cadastrar_funcionario()
            break
        elif opcao == 2:
            atualizar_funcionario()
            break
        elif opcao == 3:
            verificar_funcionario()
            break
        elif opcao == 4:
            listar_funcionarios()
            break
        elif opcao == 5:
            excluir_funcionario()
            break


def cadastrar_funcionario():
    header_atualizar_cadastro()

    nome = input('Infome o nome do funcionario: ')
    endereco = input('Informe o endereço do funcionario: ')
    cpf = input('Informe o cpf do funcionario: ')
    cpf = validar_cpf(cpf)
    cargo = input('Informe o cargo do funcionario: ')
    salario = input('Informe o salario do funcionario: ')
    data_admicao = date.today().strftime('%d/%m/%Y')
    print(data_admicao)
    data_nascimento = input('Informe a data de nacimento do funcioanrio: ')
    senha_do_funcionario = input('Infome a senha do funcionario')

    funcionario = Funcionario(nome, endereco, cpf, cargo , salario, data_admicao, data_nascimento, senha_do_funcionario)
    cadastra = Cadastrar(funcionario)
    status = cadastra.cadastra_no_banco_de_dados()

    if status == False:
        opcao = input('Deseja recomeçar ?? S/N:').upper()
        if opcao == 'S':
            cadastrar_funcionario()


def atualizar_funcionario():
    header_atualizar_cadastro()


    cpf_usuario = input('Infomer o cpf para a alteração dos dados ')
    cpf_usuario = remove_caracteres_especiais(cpf_usuario)
    nome = ''
    campo = ''
    alterar = AlterarDados(cpf_usuario, nome, campo)
    dados = alterar.mostra()
    
    if dados != None:
        print(f'1 - CPF: {dados[0]}') 
        print(f'2 - Nome: {dados[1]} ') 
        print(f'3 - Endereco: {dados[2]}')
        print(f'4 - Cargo: {dados[3]}') 
        print(f'5 - Salario: R${dados[4]}')
        print(f'6 - Data de Nascimento: {dados[5]}')
        print(f'7 - Voltar')

        opcao = int(input('Qual informação deseja alterar? '))
        if opcao == 1:
            novo_cpf = input('CPF: ')
            alterarDados = AlterarDados(cpf_usuario, novo_cpf, campo ='cpf')
            alterarDados.alterar()
        elif opcao == 2:
            print('oi')
            nome = input('Nome: ')
            alterarDados = AlterarDados(cpf_usuario , nome, campo ='nome')
            alterarDados.alterar()
        elif opcao == 3:
            novo_ender = input('Endereço: ')
            alterarDados = AlterarDados( cpf_usuario, novo_ender, campo ='endereco')
            alterarDados.alterar()
        elif opcao == 4:
            novo_cargo = input('Cargo: ')
            alterarDados = AlterarDados( cpf_usuario, novo_cargo, campo ='cargo')
            alterarDados.alterar()
        elif opcao == 5:
            novo_salario = input('Salario: ')
            alterarDados = AlterarDados(cpf_usuario, novo_salario, campo = 'salario')
            alterarDados.alterar()
        elif opcao == 6:
            data_nascimento = input('Data de nascimento: ')
            alterarDados = AlterarDados(cpf_usuario ,data_nascimento, campo = 'data_nascimento')
            alterarDados.alterar()
        elif opcao == 7:
            menu()
        else:
            print('erro')
    else:
        opcao = input('Deseja recomeçar ?? S/N:').upper()
        if opcao == 'S':
            atualizar_funcionario()


def verificar_funcionario():
    header_verificar_funcionario()

    cpf_usuario = input ('Informe o cpf que deseja verificar: ')
    mostra = MostraDados(cpf_usuario)
    dados = mostra.mostrar()

    if dados == None:
        print('Funcionario não encontrado: ')
        opcao = input('Deseja Cadastra-lo? Sim/Nao ').upper()
        if opcao == 'SIM':
            cadastrar_funcionario()
        else:
            selecao()
    else:
        opcao = 0
        while opcao > 2 or opcao < 1:
            opcao = int(input('Deseja fazer uma nova pesquisa ou voltar?? 1-Voltar/2-Nova Pesquisa'))
            print('Entrou')
            if opcao == 1:
                selecao()
            elif opcao == 2:
                verificar_funcionario()


def listar_funcionarios():
    header_lista_funcionarios()

    mostrar = MostraDados()
    mostrar.mostra_todos_funcionarios()


def excluir_funcionario():
    header_excluir_funcionario()

    cpf_usuario = input('Qual funcionario você deseja excluir? Informe o CPF por favor: ')
    excluir = ExcluirDados(cpf_usuario)
    excluir.excluir()


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
            cadastrar_funcionario()
        else:
            print('Saindo...')
            time.sleep(1.5)
            exit()
    return cpf




if __name__ == "__main__":
    selecao()