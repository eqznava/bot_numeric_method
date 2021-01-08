import os

def limpiar_pantalla():
    os.system('cls')


def menu():
    print('╔═════════════════════════════════════════════════════════════════╗')
    print('║  ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤   M E N Ú  O P C I O N E S   ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤   ║')
    print('╚═════════════════════════════════════════════════════════════════╝\n')
    print('''
    [1] E N U M E R A C I Ó N  E X H A U S T I V A
    [2] A P R O X I M A C I Ó N  D E  S O L U C I O N E S
    [3] B Ú S Q U E D A  B I N A R I A
    [4] L I M P I A R  P A N T A L L A
    [5] S A L I R\n''')


def obtener_opciones(texto):
    leido = False
    while not leido:
        try:
            numero = int(input(texto))
        except ValueError:
            print('╔═════════════════════════════════════════════════════╗')
            print('║   ERROR: » Sólo se admiten números como opciones «  ║')
            print('║          » y las opciones son del 1 al 5.        «  ║')
            print('╚═════════════════════════════════════════════════════╝\n')
        else:
            leido = True
    return numero


def busqueda_binaria():
    print('╔═════════════════════════════════════════════════════════════════╗')
    print('║     ¤ ¤ ¤ ¤  BOT PARA CALCULO CON BUSQUEDA BINARIA  ¤ ¤ ¤ ¤     ║')
    print('╚═════════════════════════════════════════════════════════════════╝\n')
    objetivo = int(input('Ingresa un número:\n'))
    epsilon = 0.001
    bajo = 0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'Bajo = {bajo}, Alto = {alto}, Respuesta = {respuesta}\n')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2
    print('═══════════════════════════════════════════════════════════════════════════════════════\n')
    print(f'\tLa raiz cuadrada aproximada de {objetivo} con un epsilon de {epsilon} es {respuesta}\n')
    print('═══════════════════════════════════════════════════════════════════════════════════════\n')


def aprox_soluciones():
    print('╔═════════════════════════════════════════════════════════════════╗')
    print('║ ¤ ¤ ¤ ¤ BOT PARA CALCULO DE APROXIMACIÓN DE SOLUCIONES ¤ ¤ ¤ ¤  ║')
    print('╚═════════════════════════════════════════════════════════════════╝\n')
    objetivo = int(input('Ingresa un número:\n'))
    epsilon = 0.01
    paso = epsilon ** 2
    respuesta = 0.0
    num_iteracion = 1

    while abs(respuesta ** 2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta ** 2 - objetivo),' | ',respuesta, '| num_iter--> ', num_iteracion,'\n')
        respuesta += paso
        num_iteracion += 1

    if abs(respuesta ** 2 - objetivo) >= epsilon:
        print('\n')
        print('═══════════════════════════════════════════════════════════════════════════════════════\n')
        print(f'\tNo se encontro la raiz cuadrada de {objetivo}.\n')
        print('═══════════════════════════════════════════════════════════════════════════════════════\n')
    else:
        print('\n')
        print('═══════════════════════════════════════════════════════════════════════════════════════\n')
        print(f'\tLa mejor aproximacion a la raiz cuadrada de {objetivo} es {respuesta}.\n')
        print('═══════════════════════════════════════════════════════════════════════════════════════\n')


def enumeracion_exa():
    print('╔═════════════════════════════════════════════════════════════════╗')
    print('║  ¤ ¤ ¤ ¤  BOT PARA CALCULO CON ENUMERACIÓN EXHAUSTIVA  ¤ ¤ ¤ ¤  ║')
    print('╚═════════════════════════════════════════════════════════════════╝\n')
    objetivo = int(input('Ingresa un número entero:\n'))
    respuesta = 0

    while respuesta**2 < objetivo:
        #print(respuesta)
        respuesta += 1

    if respuesta**2 == objetivo:
        print('═══════════════════════════════════════════════════════════════════════════════════════\n')
        print(f'\tLa raiz cuadrada de {objetivo} es {respuesta}.\n')
        print('═══════════════════════════════════════════════════════════════════════════════════════\n')
    else:
        print('═══════════════════════════════════════════════════════════════════════════════════════\n')
        print(f'\tEl número {objetivo} no tiene raiz cuadrada exacta.\n')
        print('═══════════════════════════════════════════════════════════════════════════════════════\n')


def main():
    fin = False
    while not fin:
        menu()
        opc = obtener_opciones('Escribe el número de opción que deseas:\n')
        if opc == 1:
            enumeracion_exa()
        elif opc == 2:
            aprox_soluciones()
        elif opc == 3:
            busqueda_binaria()
        elif opc == 4:
            limpiar_pantalla()
        elif opc == 5:
            print('╔═════════════════════════════════════════════════════╗')
            print('║      » P R O G R A M A  F I N A L I Z A D O «       ║')
            print('╚═════════════════════════════════════════════════════╝\n')
            fin = True
        elif opc == 0:
            print('╔═════════════════════════════════════════════════════╗')
            print('║         ERROR: » La opcion 0 no existe «            ║')
            print('╚═════════════════════════════════════════════════════╝\n')
        elif opc >= 5:
            print('╔═════════════════════════════════════════════════════╗')
            print('║   ERROR: » La opcion que escojiste no existe «      ║')
            print('╚═════════════════════════════════════════════════════╝\n')


if __name__ == '__main__':
    main()
