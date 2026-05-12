idade_do_motorista = int(input("digite sua idade:"))
cadastro = input("voce pusssui cadastro? - [sim],[não]:")
tipo_veiculo = input("qual tipo do seu veiculo?- [carro],[moto],[caminhao],[caminhonetes],[moto eletricas],[van]:")
clube_vip = input("voce faz parte do clube vip? - [sim],[não]:")

#regras de entrada
#motoristas menores de idades nao podera entrar
#não será permitida entrada de caminhoes e caminhonetese motos eletricas
#se o cliente estiver no vip ele pode entrar sem intevnçao de horário apenas taxa fixa.

print(f"dados do motorista")
print(f"idade do motista é: {idade_do_motorista}")
print(f"possui cadastro: {cadastro}")
print (f"tipo de veiculo: {tipo_veiculo}")
print (f"se tem clube vip: {clube_vip}")

if idade_do_motorista <18:
    print("acesso negado")

elif cadastro == "não":
    print("voce tera que fazer o seu registro")



                   
                   