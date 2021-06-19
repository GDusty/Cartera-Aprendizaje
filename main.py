from models.inversor import Inversor
from models.cartera import Cartera
from models.stock import Stock
from models.carga_y_guardado import *

if __name__ == '__main__':
    dict_inversores = carga()

    inversor_actual_dni = input('Introduce tu DNI: ').upper()
    if inversor_actual := dict_inversores.get(inversor_actual_dni, False):
        print(f'Bienvenido {inversor_actual}')
    else:
        print('Registrate')
        inversor_actual_nombre = input('Introduce tu nombre: ')
        inversor_actual_apellidos = input('Intrudocue tus apellidos: ')
        dict_inversores[inversor_actual_dni] = Inversor(inversor_actual_dni, inversor_actual_nombre, inversor_actual_apellidos)

    print(f'Actualmente tienes las siguientes carteras: {inversor_actual.carteras}')

    print('Opciones disponibles')
    print('1 - seleccionar cartera')
    print('2 - Crear cartera')
    print('3 - Salir')

    seleccion = input('¿Que opción elige?: ')

    print(seleccion)


    guardado(dict_inversores)
