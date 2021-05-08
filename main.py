from models.inversor import Inversor
from models.cartera import Cartera
from models.stock import Stock

if __name__ == '__main__':
    yo = Inversor(nombre='Luis', apellido='Galdeano')
    IICs = Cartera(nombre='Voy a ser rico', fondos= 10000)
    print(yo.nombre)
    print(yo.apellido)
