#Funçao para calcular o valor da pizza pelo tamanho

def calcular_preco_pizza(tamanho):
    tabela = {"p": 25.0, "m": 35.0, "G": 45.0}
    return tabela.get(tamanho,0 )