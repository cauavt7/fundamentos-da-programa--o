# desenvlova um sistema de pizzaria onde será recebido oo preço # do pedido, um desconto de 10 porcento ,
#  e ao final exiba o valor total desse com esse desconto;

# porcentagem
# 100% = 1
# 50% = 0.5
# 25% = 0.25
# 18% = 0.18


preço1 = 45.90 # hardcode
desconto = preço1 * 0.10 #10% -> 4,59
total_do_pedido = preço1 - desconto
print(f"total: R$ {total_do_pedido:.2f}")


preço2 = 38.50 # hardcode
desconto2 =  preço2 * 0.10 #10% -> 4,59
total_do_pedido2 = preço2 - desconto
print(f"total: R$ {total_do_pedido2:.2f}")



