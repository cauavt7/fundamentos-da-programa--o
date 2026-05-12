# Uma distribuidora de energia elétrica aplica tarifas diferenciadas conforme o consumo mensal do cliente residencial. O setor de
# TI precisa de um programa simples que calcule automaticamente o valor da fatura com base no consumo informado.

# ENUNCIADO

# Escreva um programa que leia o consumo mensal em kWh de um cliente e calcule o valor da fatura conforme a tabela
# de tarifas abaixo:

# Até 100 kWh → R$ o,40 por kWh --> 40
# De 101 a 200 kWh → R$ 0,60 por kWh - 40 = 60
# Acima de 200 kWh → R$ 0,90 por kWh

# Exibir ao final: o consumo informado, a faixa de tarifa aplicada e o valor total a pagar.
# Caso o consumo informado seja negativo, exibir uma mensagem de valor inválido.

#Declaração das variaveis globais - snake_case cammel case
valor_ate_100kwh = 0.40
valor_ate_200kwa = 0.60
valor_acima_200kwa = 0.90

print(f"------Seja bem vindo ao programa de cálculo de energia elétrica------")
while True:
    input_kwa = input(f"Digite a quantidade de kwa consumidos(ou 'sair' para encerrar):")
    if input_kwa.lower() == 'sair':
        print("Encerrando o progama, obrigado por utilizar\n")
        break
    elif not input_kwa.isdigit():
        print("Entrada invalida! por favor, digite um numero válido ou 'sair' para encerrar.\n")
        continue
    else:
        kwh = int(input_kwa)
        if kwh <= 100: 
            valor_total = kwh * valor_ate_100kwh
            print(f"a faixa de comsume é: 0 a 100 kwh.")
            print(f'o valor total da conta de energia é: R${valor_total:.2f}\n')
        elif kwh <= 200:
            valor_total = 100 * valor_ate_100kwh + (kwh - 100) * valor_ate_200kwa
            print(f"a faixa de comsume é: 100 a 200 kwh.")
            print(f'o valor total da conta de energia é: R${valor_total:.2f}\n')
        else:
            valor_total = 100 * valor_ate_100kwh + 100 * valor_acima_200kwa + (kwh - 200) * valor_acima_200kwa
            print(f"a faixa de comsume é:  200 kwh ou mais")
            print(f'o valor total da conta de energia é: R${valor_total:.2f}\n')