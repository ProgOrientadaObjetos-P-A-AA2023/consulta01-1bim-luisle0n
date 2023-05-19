from mis_clases import Carro
# Crear dos objetos de la clase 02

# objeto 01
# crear
carro1 = Carro("toyota",1998,"Supra MK3")
# Presentar objeto; usar el método __st__
print(carro1)
# objeto 02
carro2 = Carro()
# crear ingresando valores por teclado
print("Ingrese la marca del carro:")
nom=input()
print("Ingrese el año de fabricacion: ")
añ=input()
print("Ingrese el Modelo: ")
mod=input()

carro2.nombreC=nom
carro2.añoF=añ
carro2.modeloC=mod
# Presentar objeto; usar el método __st__
print(carro2)
