class Inversor:

    """Clase donde se van a introducir todos los inversores"""

    dni = None
    nombre = None
    apellidos = None
    carteras = {}

    def __init__(self, dni, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni

    def __str__(self):
        return f'{self.dni} - {self.nombre} - {self.apellidos}'

    def __repr__(self):
        return self.__str__()

    @property
    def safe_str(self):
        return f'{self.dni},{self.nombre},{self.apellidos}\n'

    # @property
    # def capital(self):
    #     return None
