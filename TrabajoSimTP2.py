import random
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import chi2, uniform as uniform_dist, expon as expon_dist, norm as norm_dist

# === MENÚS ===
menu = (
    "Seleccionar distribución, marque el número de la opción a la que desea ingresar desde su teclado:\n"
    "Marque 1 en el teclado: Trabajar con una Distribución Uniforme [a,b]\n"
    "Marque 2 en el teclado: Trabajar con una Distribución Exponencial\n"
    "Marque 3 en el teclado: Trabajar con una Distribución Normal\n"
    "Marque 0 en el teclado: Si desea salir al menú principal\n"
    "De marcar una opción distinta, se le volverá a preguntar por la distribución con la cual desea trabajar."
)

frecuencias = (
    "Seleccionar cantidad de intervalos, marque la opción de acuerdo a la cantidad de intervalos con los que desea trabajar:\n"
    "Marque 1 en el teclado: 10 intervalos\n"
    "Marque 2 en el teclado: 15 intervalos\n"
    "Marque 3 en el teclado: 20 intervalos\n"
    "Marque 4 en el teclado: 25 intervalos\n"
    "Marque 0 en el teclado: Si desea salir al menú principal\n"
    "De marcar una opción distinta, se le volverá a preguntar por la cantidad de intervalos."
)


# === FUNCIONES AUXILIARES ===
def validar_opcion_menu():
    while True:
        try:
            opcion = int(input("Ingrese su selección: "))
            if 0 <= opcion <= 3:
                return opcion
            else:
                print("Opción inválida. Por favor, marque un número entre 0 y 3.")
        except ValueError:
            print("Debe ingresar un número válido.")


def validar_cantidad_intervalos():
    while True:
        try:
            cantidad = int(input("Ingrese su elección: "))
            if cantidad == 0:
                print("Regresando al menú principal...")
                return None
            elif 1 <= cantidad <= 4:
                return cantidad
            else:
                print("Opción inválida. Por favor, marque un número entre 1 y 4.")
        except ValueError:
            print("Debe ingresar un número válido.")

def validar_numero(texto_input):
    while True:
        try:
            x = float(input(texto_input))
            return x
        except ValueError:
            print("Debe ingresar un número válido.")


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
        case _:
            print("Opción no válida. Se usará 10 intervalos por defecto.")
            return 10


# === FUNCIONES DE GENERACIÓN ===
def tomarMuestra():
    while True:
        try:
            muestra = int(input("Ingresar tamaño de la muestra: "))
            if muestra > 1_000_000:
                print("Tamaño máximo permitido: 1 millón.")
            elif muestra <= 0:
                print("Debe ingresar un número positivo.")
            else:
                return muestra
        except ValueError:
            print("Debe ingresar un número entero válido.")


def mostrarRandoms(randoms):
    mostrar = input("¿Desea mostrar los números aleatorios generados? (s/n): ").lower()
    if mostrar == "s":
        print("Números aleatorios generados:")
        for i in range(len(randoms)):
            print(f"{i + 1}: {randoms[i]}")
        print("-----------------------------------")


def mostrarTablaFrecuencias(randoms, intervalos):
    frec, bordes = np.histogram(randoms, bins=intervalos)
    inter = [f"{round(bordes[i], 4)} - {round(bordes[i + 1], 4)}" for i in range(len(bordes) - 1)]
    tabla = pd.DataFrame({'Intervalo': inter, 'Frecuencia': frec})
    print(tabla)
    print("-----------------------------------")


def mostrarHistograma(randoms, intervalos):
    plt.hist(randoms, bins=intervalos, edgecolor='black', density=True)
    plt.title("Histograma")
    plt.xlabel("Intervalos")
    plt.ylabel("Frecuencia")
    plt.grid(True)
    plt.show()


# === DISTRIBUCIÓN UNIFORME ===
def uniforme():
    print("\n--- Distribución Uniforme [a,b] ---")
    muestra = tomarMuestra()

    a = validar_numero("Ingrese el valor de a para la distribución uniforme [a,b]: ")

    b = validar_numero("Ingrese el valor de b para la distribución uniforme [a,b]: ")


    print(frecuencias)
    cantidad = validar_cantidad_intervalos()
    if cantidad is None:
        return  # Volver al menú principal

    intervalos = frecuencia(cantidad)

    randoms = [round(a + (b - a) * random.random(), 4) for _ in range(muestra)]

    realizar_chi = input("¿Desea realizar prueba Chi-cuadrado? (s/n): ").lower()

    mostrarRandoms(randoms)
    mostrarTablaFrecuencias(randoms, intervalos)
    if realizar_chi == "s":
        prueba_chi_cuadrado(randoms, intervalos, "uniforme", (a, b))
    mostrarHistograma(randoms, intervalos)


# === DISTRIBUCIÓN EXPONENCIAL ===
def exponencial():
    print("\n--- Distribución Exponencial ---")
    muestra = tomarMuestra()

    lambda_val = validar_numero("Ingrese el valor de λ (lambda) para la distribución exponencial: ")
    
    print(frecuencias)
    cantidad = validar_cantidad_intervalos()
    if cantidad is None:
        return  # Volver al menú principal

    intervalos = frecuencia(cantidad)

    randoms = []
    for _ in range(muestra):
        rnd = random.random()
        x = -math.log(1 - rnd) / lambda_val
        randoms.append(round(x, 4))

    realizar_chi = input("¿Desea realizar prueba Chi-cuadrado? (s/n): ").lower()

    mostrarRandoms(randoms)
    mostrarTablaFrecuencias(randoms, intervalos)
    if realizar_chi == "s":
        prueba_chi_cuadrado(randoms, intervalos, "exponencial", ([lambda_val]))
    mostrarHistograma(randoms, intervalos)


# === DISTRIBUCIÓN NORMAL (Box-Muller) ===
def normal():
    print("\n--- Distribución Normal (Box-Muller) ---")
    muestra = tomarMuestra()

    media_val = validar_numero("Ingrese el valor de μ (mu) para la distribución normal: ")

    desv_val = validar_numero("Ingrese el valor de σ (sigma) para la distribución normal: ")

    print(frecuencias)
    cantidad = validar_cantidad_intervalos()
    if cantidad is None:
        return  # Volver al menú principal

    intervalos = frecuencia(cantidad)

    randoms = []
    while len(randoms) < muestra:
        u1 = random.random()
        u2 = random.random()

        n1 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
        n2 = math.sqrt(-2 * math.log(u1)) * math.sin(2 * math.pi * u2)

        # Aplicar media y desviación
        n1 = round(n1 * desv_val + media_val, 4)
        n2 = round(n2 * desv_val + media_val, 4)

        randoms.append(n1)
        if len(randoms) < muestra:
            randoms.append(n2)
    
    realizar_chi = input("¿Desea realizar prueba Chi-cuadrado? (s/n): ").lower()

    mostrarRandoms(randoms)
    mostrarTablaFrecuencias(randoms, intervalos)
    if realizar_chi == "s":
        prueba_chi_cuadrado(randoms, intervalos, "normal", (media_val, desv_val)) 
    mostrarHistograma(randoms, intervalos)


# === PRUEBA DE BONDAD ===
def prueba_chi_cuadrado(randoms, intervalos, tipo, params):
    print("Realizando prueba de bondad Chi-cuadrado...")

    frec_obs, bordes = np.histogram(randoms, bins=intervalos)
    frec_esp = []

    for i in range(len(bordes) - 1):
        a, b = bordes[i], bordes[i + 1]

        match tipo:
            case "uniforme":
                a_, b_ = params
                prob = uniform_dist.cdf(b, loc=a_, scale=b_ - a_) - uniform_dist.cdf(a, loc=a_, scale=b_ - a_)
            case "exponencial":
                λ = params[0]
                prob = expon_dist.cdf(b, scale=1 / λ) - expon_dist.cdf(a, scale=1 / λ)
            case "normal":
                μ, σ = params
                prob = norm_dist.cdf(b, loc=μ, scale=σ) - norm_dist.cdf(a, loc=μ, scale=σ)
            case _:
                print("Distribución no soportada.")
                return

        frec_esp.append(prob * len(randoms))

    chi_stat = sum((o - e) ** 2 / e for o, e in zip(frec_obs, frec_esp) if e > 0)
    grados_libertad = intervalos - 1 - len(params)
    valor_critico = chi2.ppf(0.95, df=grados_libertad)

    print(f"Chi-cuadrado calculado: {chi_stat:.4f}")
    print(f"Valor crítico (α=0.05, gl={grados_libertad}): {valor_critico:.4f}")
    if chi_stat < valor_critico:
        print("✅ No se rechaza H0: Los datos siguen la distribución teórica.")
    else:
        print("❌ Se rechaza H0: Los datos no siguen la distribución teórica.")
    print("-----------------------------------")

# === BUCLE PRINCIPAL ===
while True:
    print(menu)
    opcion = validar_opcion_menu()

    match opcion:
        case 0:
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        case 1:
            uniforme()
        case 2:
            exponencial()
        case 3:
            normal()