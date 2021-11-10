import random
numero=random.randint(0, 10)
print(numero)
c=0
while True:  
  if(c==3):
    print("Demaciados intentos")
    break
  try:
    adivina=int(input("Digite numero: "))
    if(adivina==numero):
      print("¡¡Ganaste!!")
      break
    else:
      print("Sigue intentando") 
      c=c+1 
  except ValueError:
    print("Digite un numero entero")
