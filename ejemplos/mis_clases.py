"""

"""

# Crear dos clases en Python
# Usted defina el nombre y los atributos
# Puede usar las mismas clases usadas en Java en los ejemplos estudiados

# clase 01
class Moto:
    def __init__(self, n=None,e=None,m=None):
        self._nombre = n
        self._año = e
        self._modelo=m
        
    def __str__(self):
        return f"Moto(Marca ={self._nombre}, Año de fabricacion={self._año}, Modelo={self._modelo})"

    @property
    def atributo(self):
        return self._atributo
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def año(self):
        return self._año
    
    @property
    def modelo(self):
        return self._modelo

    @atributo.setter
    def nombreM(self, nom):
        self._nombre = nom

    @atributo.setter
    def añoF(self, a):
        self._año = a
        
    @atributo.setter
    def modeloM(self, mode):
        self._modelo = mode


# clase 02
class Carro:
    def __init__(self, n=None,e=None,d=None):
        self._nombre = n
        self._año = a
        self._modelo=d
        
    def __str__(self):
        return f"Carro(Marca ={self._nombre}, Año de fabricacion={self._año}, Modelo={self._modelo})"

    @property
    def atributo(self):
        return self._atributo
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def año(self):
        return self._año
    
    @property
    def modelo(self):
        return self._modelo

    @atributo.setter
    def nombreC(self, nom):
        self._nombre = nom

    @atributo.setter
    def añoF(self, a):
        self._año = a
        
    @atributo.setter
    def modeloC(self, mod):
        self._modelo = mod
