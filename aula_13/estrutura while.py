# crie um sistema onde o valor inicial é de 1000 e o usuario consiga realiazr um saque e ao final seja exibido o valor restante do saldo
saldo = 1000
while saldo > 0:
    saque = float(input("digte o valor do saque:"))
    saldo -= saque #saldo = saldo - saque
    print(f'saldo restante: {saldo}')