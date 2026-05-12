print("Sistema de emprestimo bancário")

# Entrada de dados
idade = int(input("Digite a idade: "))
salario = float(input("Digite o salário: "))
tempo_trabalhado = int(input("Digite o tempo trabalhado: "))


# estruuras condicionais
if idade < 18:
    print("Empréstimo negado. Você é menor de idade.")
elif salario >=5000:
    print("Empréstimo aprovado automaticamente.")
elif idade >= 18 and salario >= 2000 and tempo_trabalhado >= 2:
    print("Empréstimo aprovado.")
else: 
    print("emprestimo negado")
#verificar idade, o salario e o tempo_trabalhado
