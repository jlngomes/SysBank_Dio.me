
menu = """
Bem vindo ao GoBank

[1] - Saque
[2] - Depósito
[3] - Extrato
[4] - Sair

> """

menu_cadastro = """
Bem vindo ao GoBank

[1] - Criar conta / Cadatro
[2] - Login / Sign in

> """

LIMITE_VALOR_DIARIO = 500
LIMITE_DE_SAQUES = 3
numero_saque = 0
extrato_total = []
lista_de_usuarios = []
saldo = 0
criar_usuario = False
numero_conta = '0000'
cont_conta = 0

def login():
    print("\nLogin de usuario\n")

    nome = input("Nome: ")
    cpf = input("CPF: ")

    for dicionario in lista_de_usuarios:
        for _, valor in dicionario.items():
            if dicionario["cpf"] == cpf:
                print('Login com sucesso!')
            else:
                print('Usuário não existente!')
                cadastro()

def cadastro(cont:int):

    dict_usuarios = {
        "Conta": "",
        "nome": "",
        "data de nascimento": "",
        "cpf": "",
        "endereco": "",
    }

    cont += 1
    numero_conta = str(f'000{cont}')
    print(f"\nCadastro de usuario - conta {numero_conta}\n")

    nome = input("Nome: ")
    dict_usuarios['nome'] =  nome

    nascimento = input("Data de nascimento: ")
    dict_usuarios['data de nascimento'] = nascimento

    CPF = input("CPF: ")
    dict_usuarios['cpf'] = CPF

    endereco = input("Endereco: ")
    dict_usuarios['endereco'] = endereco



    lista_de_usuarios.append(dict_usuarios)

    print("\nUsuário cadastrado com sucesso!")

def saque(diario: int,saldo: float, limite_diario: int):

    if numero_saque >= limite_diario:
        print("\nVocê tem apenas 3 saques por dia!")
        return

    valor_saque = (input('\nQual vai ser o valor do saque: '))
    valor_saque = valor_saque.replace(',','.')
    valor_saque = float(valor_saque)

    if valor_saque <= 0:
        print(f"\nO valor de {valor_saque:.2f} é inválido!")
    elif valor_saque > diario:
        print(f'\nO valor de {valor_saque:.2f} excede o limite de {diario:.2f} reais.')
    elif valor_saque > saldo:
        print(f'\nO valor de {valor_saque:.2f} excede o saldo de {saldo:.2f} reais.')
    else:
        print(f'\nO valor de {valor_saque:.2f} foi sacado com sucesso!')
        mensagem = f'Foi sacado {valor_saque:.2f} reais.'
        extrato_total.append(mensagem)
        return valor_saque

def deposito(saldo: float,extrato_total: list):

    valor_desposito = (input('\nQual vai ser o valor do deposito: '))
    valor_desposito = valor_desposito.replace(',','.')
    valor_desposito = float(valor_desposito)

    if valor_desposito < 0:
        print('\nNão é possível realizar um depósito negativo!')
        return

    if valor_desposito > 0:
        print(f'\nO valor de {valor_desposito:.2f} foi depositado com sucesso!')
        mensagem = f'Foi depositado {valor_desposito:.2f} reais.'
        extrato_total.append(mensagem)
        return valor_desposito

def extrato(extrato_total: list):
    todos_deposito = []
    todos_saques = []

    for mensagem in extrato_total:
        if 'Foi depositado' in mensagem:
            todos_deposito.append(mensagem)
        if 'Foi sacado' in mensagem:
            todos_saques.append(mensagem)

    print('\nExtrato:\n')

    if todos_deposito:
        for mensagem_deposito in todos_deposito:
            print(mensagem_deposito)

    if todos_saques:
        for mensagem_saque in todos_saques:
            print(mensagem_saque)

    print(f'\nSaldo: {saldo}')

while True:

    if not criar_usuario:
        escolha_cadastro = input(menu_cadastro)
        if escolha_cadastro == '1':
            cadastro(cont=cont_conta)
            criar_usuario = True
        if escolha_cadastro == '2':
            login()
            criar_usuario = True

    escolha = input(menu)

    if not escolha.isdigit():
        print("\nOpção inválida, tente novamente!")
        continue

    escolha = int(escolha)
    lista = [1, 2, 3, 4]
    if not escolha in lista:
        print("\nOpção inválida, tente novamente!")
        continue

    if escolha == 1:
        valor_saque = saque(diario=LIMITE_VALOR_DIARIO,saldo=saldo, limite_diario=LIMITE_DE_SAQUES)
        if not valor_saque:
            continue
        saldo -= valor_saque
        numero_saque += 1
        continue

    if escolha == 2:
        valor_desposito = deposito(saldo,extrato_total)
        if not valor_desposito:
            continue
        saldo += valor_desposito
        continue

    if escolha == 3:
        extrato(extrato_total=extrato_total)
        continue

    if escolha == 4:
        print("\nObrigado por usar nosso sistema bancário!")
        break
