#função que exibe os sabores,tamanhos e valores das pizzas
def exibir_cardapio():
    print('''Cardápio da pizzaria do código
          ''')
    print("Marguerita - p:R$25 | m: R$35 | G:R$45")
    print("Calabrasesa - p:R$25 | m: R$35 | G:R$45")
    print("Frago - p:R$25 | m: R$35 | G:R$45")

# exibir_cardapio()

#Função para apli desconto , onde o preço e o percentual  de  desconto  será passando no momento da inovação da função.
valor_sem_desc = 40

def aplicar_desconto(preço,percentual):
    # preço * (1 - percentual / 100)
    return preço * percentual

preco_final = valor_sem_desc - aplicar_desconto(valor_sem_desc,0.10)
# print(f"preço do desconto R${preco_final:.2f}")

#declarar funçao que recebera por padrão que a borda nãiooé recheada. além disso, irá receber tambem o sabor e o tamanho da  pizza com padrão "m"

def fazer_pedido(sabor,tamanho = "m" , borda_recheada = False):
    borda = "Com borda recheada" if borda_recheada else "sem borda"
    #variavel = valor se verdadeiro if condição logica else valor ser falso.'
    print(f"pedido: {sabor}| {tamanho}| {borda}")

    fazer_pedido("marguerita")
    fazer_pedido("Frango", "G")
    fazer_pedido("Calabresa", "p",True)

