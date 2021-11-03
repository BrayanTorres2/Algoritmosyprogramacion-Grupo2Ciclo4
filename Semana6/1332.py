n=int(input())#casos de prueba
c=0#contador
while True:
  if(c==n):
    break
  c=c+1
  palabra=input("")
  tamaño=len(palabra)
  if(tamaño==5):
    print("3")
  elif(palabra[0]=="t" and palabra[1]=="w" or palabra[0]=="t" and palabra[2]=="o"or palabra[1]=="w" and palabra[2]=="o"):
    print("2")  
  else:
    print("1") 
