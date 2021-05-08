class Cartera:
    """
    Aqúí es donde vas a introducir las carteras que tienen los diferentes inversores
    """

    nombre = None
    fondos = 0.00
    stock = []

    @property
    def valor(self):
        return None

    def __init__(self, nombre, fondos):
        self.nombre = nombre
        self.fondos = fondos
