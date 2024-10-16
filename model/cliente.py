class Cliente:
    def __init__(self, nombre, preferencias, edad, contacto):
        self._nombre = nombre  
        self._preferencias = preferencias
        self._edad = edad
        self._contacto = contacto

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def preferencias(self):
        return self._preferencias
    
    @property
    def edad(self):
        return self._edad
    
    @property
    def contacto(self):
        return self._contacto

    @nombre.setter 
    def nombre(self, nombre):
        self._nombre = nombre

    @preferencias.setter
    def preferencias(self, preferencias):
        self._preferencias = preferencias

    @edad.setter
    def edad(self, edad):
        self._edad = edad
        
    @contacto.setter
    def contacto(self, contacto):
        self._contacto = contacto

    def mostrar_datos(self):
        print("Información del cliente:")
        print(f"Nombre: {self._nombre}")
        print(f"Preferencias: {self._preferencias}")
        print(f"Edad: {self._edad}")
        print(f"Contacto: {self._contacto}")

