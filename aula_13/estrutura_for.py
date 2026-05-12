#contar de 1 ate 5 -
#for numero in range (1,6):
 #   print(f'Eu sou o numero {numero}')

#exemplo de tabuada -> 5
resultado = 5 # variavel no escopo global
for numero in range(1,11):
    total = resultado * numero # ariavel no escopo local 
    print(f'5 x {numero} = {total}')