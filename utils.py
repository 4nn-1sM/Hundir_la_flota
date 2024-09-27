import numpy as np
import random

# Para crear tablero base
tablero = np.full((10, 10),"_")

#def crear_tablero():
#    tablero = np.full((10, 10),"_")
#    return tablero


#tablero_usuario_show = crear_tablero()
#tablero_usuario_hidden= crear_tablero()
#tablero_machine_show = crear_tablero()
#tablero_machine_hidden = crear_tablero()


# Crear barco
def crear_barco(eslora):
    while True:
        casilla_0 = (random.randint(0,9), random.randint(0,9))
        orientacion = random.choice(["Vertical", "Horizontal"])
        barco = [casilla_0]
        casilla = casilla_0
        while len(barco) < eslora and casilla[0] > 0 and casilla[-1] > 0:
            if orientacion == "Vertical":
                if 9 - casilla_0[0]  >= eslora:
                    casilla = (casilla[0]+1, casilla[1])
                    barco.append(casilla) # Vertical
                else:
                    casilla = (casilla[0]-1, casilla[1])
                    barco.append(casilla) # Vertical               
            elif orientacion == "Horizontal":
                if 9 - casilla_0[1]  >= eslora:
                    casilla = (casilla[0], casilla[1]+1)
                    barco.append(casilla) # Vertical
                else:
                    casilla = (casilla[0], casilla[1]-1)
                    barco.append(casilla) # Vertical              
        if len(barco) == eslora:
            return barco
    # para crear lista con todos los barcos
esloras = [2,2,2,3,3,4]
flota = []
for valor in esloras:
        crear_barco(valor)
        flota.append(crear_barco(valor))

# Para colocar los barcos. En el jupyter funciona, aquí no.
def colocar_barcos(flota, tablero):
    for barco in flota:
        for casilla in barco:
            tablero[casilla] = "O"
    return tablero

# Parece que esta sí funciona 
barco_1 = flota[0] 
barco_2 = flota[1]
barco_3 = flota[2]
barco_4 = flota[3]
barco_5 = flota[4]
barco_6 = flota[5]

def colocar_barcos(barco, tablero):
    for casilla in barco_1:
        tablero[casilla] = "O"
    for casilla in barco_2:
        tablero[casilla] = "O"
    for casilla in barco_3:
        tablero[casilla] = "O"
    for casilla in barco_4:
        tablero[casilla] = "O"
    for casilla in barco_5:
        tablero[casilla] = "O"
    for casilla in barco_6:
        tablero[casilla] = "O"
    return tablero

print(tablero)
colocar_barcos(barco_1, tablero)
print(tablero)

# Para disparar
def disparar(casilla, tablero):
    if tablero[casilla] == "O":
        print("Tocado")
        tablero[casilla] = "X"
    else:
        print("Agua")
        tablero[casilla] = "A"
    return tablero