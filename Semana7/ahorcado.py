import random
def palabra()->str:
  palabras=["amarillo", "rosado", "jose","computador","salon","ean","zanahoria","tomate","laura"]
  numero=random.randint(0, len(palabras)-1)
  return palabras[numero]
a=palabra()
b=[]
for i in range(0,len(a)):
  b.append("_")
print(a)
while True:
  letra=str(input("Digite letra: "))
  for x in range(0,len(a)):
    if(a[x]==letra):
      b[x]=letra  
  print("".join(b))  
  x="".join(b)
  if(x==a):
    print("Ganaste!!")
    break  
