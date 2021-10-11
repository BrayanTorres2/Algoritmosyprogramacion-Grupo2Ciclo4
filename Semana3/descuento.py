"""
Entradas
total_pagar-->float-->total_ pagar
Salidas
descuento-->float-->descuento
"""
#entradas
total_pagar=float(input("Digite total a pagar"))
#Caja negra
descuento=total_pagar-total_pagar*0.15#float
#Salida
print("debe pagar: ", descuento)
print("debe pagar:"+str(descuento))
print(f"debe pagar: {descuento}")
