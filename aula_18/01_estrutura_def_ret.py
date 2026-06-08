#parâmetros nomeados - ao nomear os arguentos a ordem não importa mais.

def registrar_cliente(nome,telefone,endereco):
    print(" === DADOS DO CLIENTE ===")
    print(f"cliente: {nome}")
    print(f"telefone: {telefone}")
    print(f"endereço:{endereco}")

# registrar_cliente(
#      telefone="217277277",
#      nome="Ana lima",
#      Endereço= "Rua das pizzas,42"
# )

# 
#Retorno de valores - desenpacota,ento de retorno (unpaking) - Devolve uma tupla com returns

def resumo_pedido(itens,desconto=0):
    subtotal = sum(itens)
    valor_desconto = subtotal * (desconto/100)
    total = subtotal - valor_desconto
    return subtotal, valor_desconto, total #devolme uma tupla(subtotal,valor_desconto,total)

#invocando e desempacotando a função retorno
# print (resumo_pedido([35.0, 12.0, 8.5 ],desconto=10))
sub, desc, tot = resumo_pedido([35.0, 12.0, 8.5 ],desconto=10)
print(f"Subtotal:  R$ {sub:.2f}")
print(f"Desconto:  R$ {desc:.2f}")
print(f"total:  R$ {tot:.2f}")

