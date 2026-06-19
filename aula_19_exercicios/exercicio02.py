
def verificar_mencao_honrosa (media:float , honra : bool = True):
    if media > 9:
         situação = "voce foi honrado , parabens "

    elif media> 5:

         situação = " voce esta de recuperação"

    else:
         situação = "voce esta reprovado"

    return situação, honra

print(verificar_mencao_honrosa())