c=0
while True:
  try:
    if(c==3):
      print("demaciados intentos")
      break
    contraseña=int(input("Digite numero: "))
    break
  except ValueError:
    c=c+1 
    print("Solo se puede ingresar numero enteros") 
   

print("demas lineas")
