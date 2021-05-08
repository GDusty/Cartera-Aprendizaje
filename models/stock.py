class Stock:
    """
    Clase donde se van a introducir las acciones
    """

    nombre = None
    precio = 0.00

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

