import random
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def mostrarRandoms(randoms):
    mostrar = input("¿Desea mostrar los numeros aleatorios generados? (s/n): ").lower()
    if mostrar == "s":
        print("Numeros aleatorios generados:")
        for i in range(len(randoms)):
            print(f"{i+1}: {randoms[i]}")
        print("-----------------------------------")

def mostrarTablaFrecuencias(randoms, intervalos):
    frec, bordes = np.histogram(randoms, bins=intervalos)
    inter = [f"{round(bordes[i], 4)} - {round(bordes[i+1], 4)}" for i in range(len(bordes)-1)]

    tabla = pd.DataFrame({
        'Intervalo': inter,
        'Frecuencia': frec
    })

    print(tabla)
    print("-----------------------------------")

def mostrarHistograma(randoms, intervalos):
    plt.hist(randoms, bins=intervalos, edgecolor='black')
    plt.title("Histograma")
    plt.xlabel("Intervalos")
    plt.ylabel("Frecuencia")
    plt.grid(True)
    plt.show()


# Trabajo Practico 2 - Generacion de numeros aleatorios
print("TP2 generacion de numeros aleatorios")

opcion = -1
intervalos = 0

def frecuencia(opcion):
    match opcion:
        case 1:
           return 10
        
        case 2:
            return 15
        
        case 3:
            return 20
        
        case 4:
            return 25

def uniforme():

    muestra = int(input("Ingresar tamaño de la muestra: "))

    if muestra > 1000000:
        muestra = int(input("Ingresar muestra menor o igual a 1 millon: "))

    a = float(input("Ingrese el valor de a para la distribución uniforme[a,b]: "))
    b = float(input("Ingrese el valor de b para la distribución uniforme[a,b]: "))


    print(frecuencias)
    cantidad = int(input("Ingrese su eleccion: "))

    intervalos = frecuencia(cantidad)

    randoms = []
    for i in range (muestra):
        rnd = random.random()
        x = a + (b-a)*rnd
        randoms.append(round(x,4))

    # Randoms generados (opcional)
    mostrarRandoms(randoms)

    # Tabla de frecuencias
    mostrarTablaFrecuencias(randoms, intervalos)

    # Histograma
    mostrarHistograma(randoms, intervalos)



def exponencial():

    muestra = int(input("Ingresar tamaño de la muestra: "))

    if muestra > 1000000:
        muestra = int(input("Ingresar muestra menor o igual a 1 millon: "))

    lambda_val = float(input("Ingrese el valor de λ para la distribución exponencial: "))

    print(frecuencias)
    cantidad = int(input("Ingrese su eleccion: "))

    intervalos = frecuencia(cantidad)

    randoms = []
    for i in range (muestra):
        rnd = random.random()
        x = -math.log(1-rnd) / lambda_val
        randoms.append(round(x,4))

    # Randoms generados (opcional)
    mostrarRandoms(randoms)

    # Tabla de frecuencias
    mostrarTablaFrecuencias(randoms, intervalos)

    # Histograma
    mostrarHistograma(randoms, intervalos)

def normal():

    muestra = int(input("Ingresar tamaño de la muestra: "))

    if muestra > 1000000:
        muestra = int(input("Ingresar muestra menor o igual a 1 millon: "))


    print(frecuencias)
    cantidad = int(input("Ingrese su eleccion: "))

    intervalos = frecuencia(cantidad)

    media_val = float(input("Ingrese el valor de μ para la distribución normal: "))
    desv_val = float(input("Ingrese el valor de σ para la distribución normal: "))

    randoms = []
    for i in range (muestra):
        u1 = random.random()
        u2 = random.random()
        n1 = (math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)) * desv_val + media_val
        n2 = (math.sqrt(-2 * math.log(u1)) * math.sin(2 * math.pi * u2)) * desv_val + media_val
        randoms.append(round(n1, 4))
        randoms.append(round(n2, 4))

    # Randoms generados (opcional)
    mostrarRandoms(randoms)

    # Tabla de frecuencias
    mostrarTablaFrecuencias(randoms, intervalos)

    # Histograma
    mostrarHistograma(randoms, intervalos)

menu = " Seleccionar distribucion: \n" \
"       1 - Uniforme [a,b] \n" \
"       2 - exponencial \n" \
"       3 - normal \n" \
"       0 - salir"

frecuencias = " Seleccionar cantidad de intervalos: \n" \
"               1 - 10 \n" \
"               2 - 15 \n" \
"               3 - 20 \n" \
"               4 - 25"

while opcion != 0:
    
    print(menu)

    opcion = int(input("Ingrese su seleccion: "))

    match opcion:
        case 1:
            uniforme()
        
        case 2:
            exponencial()
        
        case 3:
            normal()
        