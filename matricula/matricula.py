idade= int(input("digite sua idade:"))
nota= float(input("digite sua nota:"))
frequencia=int(input("digite sua frequencia:"))

aulas=100
frequencia_escolar = (frequencia / 100) *100

 
if idade < 18:
  print("naõ sera possivel fazer a matricula")

elif nota >= 9:
  print("matricula aprovada")

elif frequencia >= 75:
  print("nao sera possivel realizar a matricula")

elif  idade >=18 and nota >=6 and frequencia >= 75:
   print("matricula aprovada")

else:
   print("matricula nao sera aprovada")
   