idade = int(input("digite sua idade: "))
salario =float(input("digite seu salario:"))
tempo_de_trabalho = int(input("digite seu tempo de trabalho: "))

if idade<18: 
   print("você é menor de idade e não pode pegar o emprestimo")
elif salario>=5000:
   print("seu salario é aprovado")
 
elif idade >= 18 and salario >= 2000 and tempo_de_trabalho >= 2:
 print("seu emprestimo foi aprovado")

else:
 print(" Empréstimo negado")

print(f"Dados informados:")
print(f"Idade: {idade}")
print(f"Salário: R$ {salario}")
print(f"Tempo de trabalho: {tempo_de_trabalho} anos")