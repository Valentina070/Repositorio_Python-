class Menu:

    def __init__(self, nombre=None, tipo=None, precio=0.0):
        self._nombre = nombre  # Atributos privados
        self._tipo = tipo
        self._precio = precio

    # Métodos getter
    @property
    def nombre(self):
        return self._nombre

    @property
    def tipo(self):
        return self._tipo

    @property
    def precio(self):
        return self._precio

    # Métodos setter
    @nombre.setter 
    def nombre(self, nombre):
        self._nombre = nombre

    @tipo.setter 
    def tipo(self, tipo):
        self._tipo = tipo

    @precio.setter 
    def precio(self, precio):
        self._precio = precio

    def mostrar_datos(self):
        print(f"Información del menú:")
        print(f"Nombre: {self._nombre}")
        print(f"Tipo: {self._tipo}")
        print(f"Precio: {self._precio}")

