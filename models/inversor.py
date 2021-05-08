class Inversor:
    """
    Clase donde se van a introducir todos los inversores
    """
    nombre = None
    apellido = None
    carteras = []

    @property
    def capital(self):
        return None

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        # self.apellido = apellido
