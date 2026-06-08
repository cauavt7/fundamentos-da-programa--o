#sistema de calculo de consumo de energia

consumo = float(input("Digite seu consumo: "))

if consumo < 0:
    print(" deu erro consumo inválido")
    
    
elif consumo <= 100:
    tarifa = 100 * 0.40
    valor = consumo * tarifa
    
    print("Consumo:", consumo, "kWh")
    print("Tarifa: R$ 0.40 por kWh")
    print("Valor total: R$", valor)

 
elif consumo <= 200:

    tarifa =  100 * 0.60 
    valor = consumo * tarifa

    print("Consumo:", consumo, "kWh")
    print("Tarifa : R$ 0.60 por kWh")
    print("Valor: R$", valor)

else:

    tarifa = 0.90
    valor = consumo * tarifa

    print("Consumo:", consumo, "kWh")
    print("Tarifa : R$ 0.90 por kWh")
    print("Valor: R$", valor)





   


      

