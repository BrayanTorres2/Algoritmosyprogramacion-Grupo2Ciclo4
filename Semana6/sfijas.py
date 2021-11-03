vueltas=[]
while True:
  v=input("")#ventas
  (n,m)=v.split(" ")
  n=int(n)
  m=int(m)
  if(m==0 and n==0):
    break
  r=m-n
  vueltas.append(r)
caja=[7,12,22,52,102,15,25,55,105,30,60,110,70,120,150]
for i in vueltas:
  if(caja.count(i)==1):
    print("possible")
  else:
    print("impossible")  
