nome = input("seu nome:")
idade = int(input("sua idade"))
convite = input("possui convite? - [sim], [não]:")

print ("dados informados")
print (f"seu é nome:{nome}")
print (f"sua iadede é :{idade}")
print (f"convite de acesso: {convite}")

if idade < 16:
    print("acesso negado")
elif idade > 16 and convite == "sim":
    print (" acesso permitido")
elif convite == "não":
   print(" acesso negado")
elif idade >=16 and convite =="sim" :
   print ("aceso aprovado")

while True:
    finalizar = input("continuar(ou 'sair' para encerrar): ")

    if finalizar == "sair":
        print("encerramento") 
        break  
 
