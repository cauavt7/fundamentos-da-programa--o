saldo = 1000,00
historico = []# lista vazia

print(f'🏧--- Bem vindo ao caixa eletronico---')

while True: # imprime pelo menos o while uma vez
    print(f'''---menu principal---
          [1] - depositar
          [2] - Sacar
          [3] - Ver saldo
          [4] - Ver historico
          [5] - Sair
          ''')
    opcao = input (' ➡️escolha uma opção: ')

    #lógica para a opção de Depósito
    if opcao == '1':
        valor_deposito = Float(input(' ➡️Digite o valor para depósito: R$'))
        # saldo = saldo = valor_deposito
        saldo += valor_deposito
        registro = f'Depósito: =R$ {valor_deposito:.2f}'
        historico.append(registro) #apend() adicionar algo a lista
        print('🆗Deposito realizado com suscesso.')
    else:
        print('❌ Valor invalido o depósito deve ser um numero positivo.')
    elif opcao == '2':
    valor_saque = Float(input(' ➡️Digite o valor para depósito: R$'))
    if valor_saque <= 0:
     print('vlor ivalido! o saque deve ser um numero positivo')
    elif valor_saque> saldo:
     print('❌Saldo insuficiente para realizar este saque.')
    else:
       #saldo = saldo - valor_saque
       saldo -= valor_saque
       registro = f'saque: -R$ {valor_saque:.2f}'
       historico.append(registro)
    print('🆗 Saque realizado com sucesso! retire o seu dinheiro.')
    elif opcao == '3'
    print ('seu saldo atual é: R$ {saldo: .2f}' ) 
    elif opcao == "4":
    print('historico de transaçoes')
    if not historico:
       print('nenhuma transação foi realizada ainda.')
    else:
       for transaçao in historico:
          print(transaçao)
    elif opcao == '5':
    print("😊 obrigdo por utilizar nosso caix eletronico")
        break
else:  
 print ("opcao invalisa. por favor escolha uma das opções do menu")

        













>



          
