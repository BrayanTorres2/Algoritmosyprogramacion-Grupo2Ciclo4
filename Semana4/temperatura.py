"""
Entradas
temperatura-->float-->tem
Salidas
deporte-->str-->deporte
"""
#entrada
tem=float(input("Digite temperatura: "))
#caja negra
deporte=""
if(tem>85 and tem <=180):
  deporte="Natación"
elif(tem>=71.0 and tem<=85.9):
  deporte="Tenis"  
elif(tem>=33.0 and tem<=70.9):
  deporte="Golf"  
elif(tem>=11 and tem<=32):
  deporte="Esquí" 
elif(tem>=0 and tem<=10):
  deporte="Marcha"  
else:
  deporte="No se ha reconocido ningun deporte :("

#Salida
print(deporte)
