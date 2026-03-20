# Estrutura de repetição
#if (se) ->  verifica se uma informação é (verdadeira). se for, ele executa o código.
#elif (ão se)-> é usado pra testar varia condicoes ele so executa se todas as condicoes aneriores forem falsas
#else (senão) -> Executa o código se a condição if for false (falsa).

# idade_usuario = 15

# se o usuario for maior de 18 anos, eu vou passar as informações. senão você é menor de idade.
# if idade_usuario >= 18:
#     print("você é maior de idade.")
# else:
#     print("você é menor de idade")

idade = 73
if idade>= 18:
    print ("você é maior de idade")
elif idade>= 0 and idade <18:
    print("você é jovem de idade.")
elif idade >= 70:
    print("você é experiente de idade.")
else:
    print("você é menor de idade.")