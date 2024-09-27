import utils
print("Hundir la flota")

print()

# para colocar todos los barcos
flota = utils.flota
tablero= utils.tablero
print("Tus barcos son los siguientes:", flota)
print("Su posición en el tablero es:")
print(tablero)

print("Empieza el juego")
print("Le toca a la máquina")
disparo_1 = utils.disparar((1,2), tablero)
print(tablero)


