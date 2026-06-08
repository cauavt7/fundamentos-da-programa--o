#as funções podem ou não receber propriedades

#saudacao()
#saudacao()
#saudacao()
#saudacao()

#calcule o preço total de uma pizza onde será passado um dicionario com os tamanhos e valores. além disso o cliente pode solicitar ou não a borda recheada. ao final, retorne o preço.

#1.pequena,média ou grande . qualquer pizza terá o mesmo valor dependendo do tamanho.
# 2. Se o cliente optar pela borda recheada, deverá ser acrescido no valor da pizza = R$8.
def calucar_preco_pizza(tamanho,borda_recheada=False):
    "calcule o preço final de uma puzza com opçõs."
    tabela = {"p":25.0 , "M":35.0 ,"g":45.0}
    preco = tabela[tamanho]
    if borda_recheada: # borda_recheada == true por adrão toda variavel é true
        preco += 8.0 #preco = preco + 8.0
        return preco
    
print(calucar_preco_pizza("p")) #23
print(calucar_preco_pizza("p",True)) #33
print(calucar_preco_pizza("M",False))# 23

lista_mercado = ["arroz","feijão" ,"danoninho","açucar"]