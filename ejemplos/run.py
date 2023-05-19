from mis_clases import Moto
# Crear dos objetos de la clase 02

# objeto 01
# crear
moto1 = Moto("Honda",2023,"YZ")
# Presentar objeto; usar el método __st__
print(moto1)
# objeto 02
moto2 = Moto()
# crear ingresando valores por teclado
print("Ingrese la marca de la Moto:")
nom=input()
print("Ingrese el año de fabricacion: ")
añ=input()
print("Ingrese el Modelo: ")
mod=input()

moto2.nombreM=nom
moto2.añoF=añ
moto2.modeloM=mod
# Presentar objeto; usar el método __st__
print(moto2)
