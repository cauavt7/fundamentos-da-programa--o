#sistema de calculo de consumo de energia

consumo = float(input("Digite seu consumo: "))

#aplicar quantidadde do consumo
if consumo < 0:
    print(" deu erro consumo inválido")
    
    #se o consumo for maoir que menor que 100 sera aplicada a tarifade 0.40
elif consumo <= 100:
    tarifa = 0.40
    valor = consumo * tarifa
    
    print("Consumo:", consumo, "kWh")
    print("Tarifa: R$ 0.40 por kWh")
    print("Valor total: R$", valor)

 #se o valor se consumo for de 101 ha 200 sera aplicada tarifa de 0.60
elif consumo <= 200:

    tarifa = 0.60 
    valor = consumo * tarifa

    print("Consumo:", consumo, "kWh")
    print("Tarifa : R$ 0.60 por kWh")
    print("Valor: R$", valor)
#Acima de 200 sera aplicada tarifa de 0.90
else:

    tarifa = 0.90
    valor = consumo * tarifa
    
    print("Consumo:", consumo, "kWh")
    print("Tarifa : R$ 0.90 por kWh")
    print("Valor: R$", valor)





   


      

