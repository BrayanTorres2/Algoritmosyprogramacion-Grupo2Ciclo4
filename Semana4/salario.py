"""
Entradas
SalarioBruto-->float-->Salario
Salidas
SalarioNeto-->float-->Sueldo
"""
#Entradas
Salario=float(input("Digite salario bruto"))
#cajanegra
SalarioNeto=0
if(Salario<900000):
  SalarioNeto=Salario*0.15+Salario
else:
  SalarioNeto=Salario*0.12+Salario
#Salida
print(SalarioNeto)
