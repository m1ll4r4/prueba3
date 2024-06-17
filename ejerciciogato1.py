import random


def mostrar_bienvenida():
    print("Bienvenido al juego de GATO!!!!!!")


def mostrar_menu():
    print("...Menú...:")
    print("1. Nueva partida (Player 1 VS COM)")
    print("2. Versus (P1 VS P2)")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion     #DEVUELVE LA OPCION QUE SELECCIONO EL USUARIO 


def inicializar_tablero():
    return [' ' for _ in range(9)]     #


def mostrar_tablero(tablero):
    print(f"""
     {tablero[0]} | {tablero[1]} | {tablero[2]}
    -----------
     {tablero[3]} | {tablero[4]} | {tablero[5]}
    -----------
     {tablero[6]} | {tablero[7]} | {tablero[8]}
    """)


def realizar_movimiento(tablero, posicion, jugador):
    if tablero[posicion] == ' ':
        tablero[posicion] = jugador
        return True                      # SOLO SI LA POSICION ESTA DISPONIBLE
    return False                         # CUANDO NO ES NUM DEL 0-8 O ESTA OCUPADO EL ESPACIO


def verificar_ganador(tablero, jugador):
    combinaciones_ganadoras = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6)              
    ]
    for comb in combinaciones_ganadoras:             #POSIBLE COMBINACION DISPONIBLE GANADORA, Y ALMACENA EN LA LISTA COMBINACIONES GANADORAS 
        if all(tablero[i] == jugador for i in comb): #VERIFICACION DE POSICIONES EN LA COMBINACION ACTUAL,CONTIENE EL SIMBOLO DEL JUGADOR ACTUAL
            return True                              #JUGADOR ACTUAL GANA
    return False                                     #JUGADOR ACTUAL NO GANA



def verificar_empate(tablero):
    return all(espacio != ' ' for espacio in tablero)  #


def movimiento_computadora(tablero):                  #POSICION ALEATORIA MIENTRAS LA POSICION ESTE DISPONIBLE.
    posiciones_libres = [i for i in range(9) if tablero[i] == ' ']
    return random.choice(posiciones_libres)            #


def jugar_partida(jugadores):
    tablero = inicializar_tablero()
    turno = 0
    while True:
        mostrar_tablero(tablero)
        jugador_actual = jugadores[turno % 2]
        if jugador_actual == 'COM':
            posicion = movimiento_computadora(tablero)
        else:
            posicion = int(input(f"Turno de {jugador_actual}, ingrese posición (0-8): "))
        if realizar_movimiento(tablero, posicion, jugador_actual):
            if verificar_ganador(tablero, jugador_actual):
                mostrar_tablero(tablero)
                print(f"¡{jugador_actual} ha ganado!")
                break
            elif verificar_empate(tablero):
                mostrar_tablero(tablero)
                print("¡Es un empate!")
                break
            turno += 1
        else:
            print("Posición no válida, intente de nuevo.")


def main():        #FUNCION PRINCIPAL DEL COMIENZO DE JUEGO
    mostrar_bienvenida()
    while True:
        opcion = mostrar_menu()
        if opcion == '1':
            jugar_partida(['P1', 'COM'])
        elif opcion == '2':
            jugar_partida(['P1', 'P2'])
        elif opcion == '3':
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción no válida, por favor seleccione nuevamente.")

# Ejecutar el juego
if __name__ == "__main__":    #
    main()