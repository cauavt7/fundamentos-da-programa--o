# desenvlova um sistema de pizzaria onde será recebido oo preço # do pedido, um desconto de 10 porcento ,
#  e ao final exiba o valor total desse com esse desconto;

# declarar uma def (função)
def calcular_total (nome,preco,desconto=0.10):
    valor_desconto = preco * desconto
    total = preco - valor_desconto
    print(f""" Recibo
          pedido do cliente :{nome}
          Valor do pedidoR$ {preco}
          Desconto aplicado{desconto}
          total do pedido: R$ {total:.2f}
          """)

#invocação def
calcular_total("joão",45.90)
calcular_total("ana",38.50)
calcular_total("Maria",20)
calcular_total("Kitty",19)


