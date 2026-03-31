# Variaveis da pizzaria
FRETE = 2 #Constande fake
pizza_sabor = input("informe o sabor da pizza - [frango com requeijao],[mussarela],[banana com chocolate]: ")
pizza_tamanho = input("informe o tamanho da pizza - [pequena],[media],[grande]: ")
dia_semana = input("informe o dia da semana - [quarta],[quinta],[sexta],[sabado],[domingo]: ")

print(f"o sabor da pizza é {pizza_sabor}, o tamanho é {pizza_tamanho} e hoje é {dia_semana}.")
# promoções -> Estruturas condicionas

# comprando qualquer pizza e qualquer tamanho no sábado,
# o refri é gratuito.
if dia_semana == "sabado": 
    print(f"🍕pedido aceito com sucesso.")
    print(f"o refri hoje é por conta da casa!.")
elif dia_semana == "domingo":
    print(f"🍕pedido aceito com sucesso.")
    print(f"o refri hoje é por conta da casa!.")
elif pizza_sabor == "calabresa" and pizza_tamanho =="media":
    print(f"🍕pedido aceito com sucesso.")
    print(f"o frete hoje é por conta da casa!.")

    
    

# comprando uma pizza e calabresa tamanho edio, em qualquer dia, o frete é gratuito.

# compando qualquer pizza de qualquer tamanho no domingo, o frete e o refri são gratuitos.
