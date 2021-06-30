from models.inversor import Inversor
from models.cartera import Cartera
from models.stock import Stock
from models.carga_y_guardado import *

if __name__ == '__main__':
    dict_inversores = carga()

    inversor_actual_dni = input('Introduce tu DNI: ').upper()
    if inversor_actual := dict_inversores.get(inversor_actual_dni, False):
        print(f'Bienvenido {inversor_actual}')
        print(f'Actualmente tienes las siguientes carteras: {inversor_actual.carteras}')
    else:
        print('Registrate')
        inversor_actual_nombre = input('Introduce tu nombre: ')
        inversor_actual_apellidos = input('Intrudocue tus apellidos: ')
        dict_inversores[inversor_actual_dni] = Inversor(inversor_actual_dni, inversor_actual_nombre,
                                                        inversor_actual_apellidos)

    opciones = False

    while not opciones:

        print('Opciones disponibles')
        print('1 - seleccionar cartera')
        print('2 - Crear cartera')
        print('3 - Salir')

        seleccion = int(input('¿Que opción elige?: '))

        if seleccion == 1:
            pass
        elif seleccion == 2:
            pass
        elif seleccion == 3:
            print(f'Gracias por invertir con nosotros {inversor_actual.nombre}')
            opciones = True
            guardado(dict_inversores)
        else:
            print('Esa opción no está disponible, intentalo de nuevo.')

