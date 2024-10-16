class Restaurante:
    def __init__(self, nombre=None, especialidad=None, capacidad=0, ubicacion=None, contacto=None):
        self._nombre = nombre  
        self._especialidad = especialidad
        self._capacidad = capacidad
        self._ubicacion = ubicacion
        self._contacto = contacto

    @property
    def nombre(self):
        return self._nombre

    @property
    def especialidad(self):
        return self._especialidad

    @property
    def capacidad(self):
        return self._capacidad

    @property
    def ubicacion(self):
        return self._ubicacion

    @property
    def contacto(self):
        return self._contacto

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @especialidad.setter
    def especialidad(self, especialidad):
        self._especialidad = especialidad

    @capacidad.setter
    def capacidad(self, capacidad):
        self._capacidad = capacidad

    @ubicacion.setter
    def ubicacion(self, ubicacion):
        self._ubicacion = ubicacion

    @contacto.setter
    def contacto(self, contacto):
        self._contacto = contacto

    def mostrar_datos(self):
        print(f"Información del Restaurante:")
        print(f"Nombre: {self._nombre}")
        print(f"Especialidad: {self._especialidad}")
        print(f"Capacidad: {self._capacidad}")
        print(f"Ubicación: {self._ubicacion}")
        print(f"Contacto: {self._contacto}")

