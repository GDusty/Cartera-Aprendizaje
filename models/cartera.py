class Cartera:
    """
c    """

    id = 0
    nombre = None
    fondos = 0.00
    stock = []

    @property
    def valor(self):
        return None

    def __init__(self, id, nombre, fondos):
        self.id = id
        self.nombre = nombre
        self.fondos = fondos

    def __str__(self):
        return f'{self.id} - {self.nombre} - {self.fondos}'

    def __repr__(self):
        return str(self)
