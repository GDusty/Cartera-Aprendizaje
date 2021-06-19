import os

from models.inversor import Inversor
from models.cartera import Cartera

def carga():
    dict_inversores = {}
    try:
        file = open('models/lista_inversores.csv', 'r')
        for linea in file.readlines():
            linea = linea.replace('\n', '')
            dni, nombre, apellidos = linea.split(',')
            dict_inversores[dni] = Inversor(dni=dni, nombre=nombre, apellidos=apellidos)
        try:
            file_carteras = open('models/carteras.csv', 'r')
            for linea in file_carteras.readlines():
                linea = linea.replace('\n', '')
                id_cartera, nombre_cartera, fondos, dni_inversor = linea.split(',')
                if inversor := dict_inversores.get(dni_inversor, False):
                    inversor.carteras[id_cartera] = Cartera(id_cartera, nombre_cartera, fondos)

        except FileNotFoundError:
            print('No hay carteras para cargar')
    except FileNotFoundError:
        print('No hay datos disponibles para cargar')
    print('Carga realizada')
    return dict_inversores


def guardado(dict_inversores: dict):
    os.remove('models/lista_inversores.csv')
    file = open('models/lista_inversores.csv', 'w+')
    for inversor in dict_inversores.values():
        file.write(inversor.safe_str)

    file.close()
    print('El fichero se ha guardado')