# -*- coding: utf-8 -*-
"""Compute_Statistics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jcKmrgsBEkoyJ8rLzzy9WhkyvoislNRf
"""

pip install pylint

!jupyter nbconvert --to script Compute_Statistics.ipynb

!pylint Compute_Statistics.ipynb

from google.colab import drive
drive.mount('/content/drive')

import os
DIR = "/content/drive/MyDrive/Maestría Inteligencia Artificial Aplicada/PS y AC"
os.chdir(DIR)

# PROCESADO DE ARCHIVOS-----------------------------------------------------------------------------------------------------------------
def procesar_archivo(tc):
    try:
        with open(tc, 'r') as archivo:
            leer_archivo = archivo.read()
            print(leer_archivo)
    except FileNotFoundError:
        print(f"Error existente = No se encontró el archivo: {tc}")
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")

tc_seleccionado = 'TC1.txt'  #'TC2.txt'   'TC3.txt'  'TC4.txt'  'TC5.txt'   'TC6.txt'   'TC7.txt'
procesar_archivo(tc_seleccionado)

# ESTADÍSTICAS Y GUARDADO DE RESULTADOS
def calcular_estadisticas(datos):
    # Media ---------------------------------------------------------------
    media = sum(datos) / len(datos)

    # Mediana -------------------------------------------------------------
    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)
    mediana = (datos_ordenados[n // 2] + datos_ordenados[(n - 1) // 2]) / 2

    # Moda ----------------------------------------------------------------
    conteo_numeros = {}
    for num in datos:
        conteo_numeros[num] = conteo_numeros.get(num, 0) + 1
    moda = max(conteo_numeros, key=conteo_numeros.get)

    # Varianza ------------------------------------------------------------
    varianza = sum((x - media) ** 2 for x in datos) / len(datos)

    # Desviación Estándar -------------------------------------------------
    desviacion_estandar = varianza ** 0.5

    return media, mediana, moda, varianza, desviacion_estandar


# Guardado de resultados en StatisticsResults.txt
def imprimir_resultados(resultados):
    for nombre, valor in resultados.items():
        print(f"{nombre.capitalize()}: {valor}")


def guardar_resultados(resultados, tc_seleccionado='StatisticsResults.txt'):
    with open(tc_seleccionado, 'w') as archivo:
        for nombre, valor in resultados.items():
            archivo.write(f"{nombre.capitalize()}: {valor}\n")

# IMPRESIÓN DE ESTADÍSTICAS
# ESTADÍSTICAS ARCHIVO TC1
nombre_del_archivo = 'TC1.txt'
with open(nombre_del_archivo, 'r') as archivo:
    datos_del_archivo = [float(line.strip()) for line in archivo.readlines()]

# Realizado de cálculos
resultados_estadisticos = calcular_estadisticas(datos_del_archivo)

# Impresión de resultados y guardado en el archivo
resultados_dict = dict(zip(["media", "mediana", "moda", "varianza", "desviacion_estandar"], resultados_estadisticos))
imprimir_resultados(resultados_dict)
guardar_resultados(resultados_dict)

# IMPRESIÓN DE ESTADÍSTICAS
# ESTADÍSTICAS ARCHIVO TC2
nombre_del_archivo = 'TC2.txt'
with open(nombre_del_archivo, 'r') as archivo:
    datos_del_archivo = [float(line.strip()) for line in archivo.readlines()]

# Realizado de cálculos
resultados_estadisticos = calcular_estadisticas(datos_del_archivo)

# Impresión de resultados y guardado en el archivo
resultados_dict = dict(zip(["media", "mediana", "moda", "varianza", "desviacion_estandar"], resultados_estadisticos))
imprimir_resultados(resultados_dict)
guardar_resultados(resultados_dict)

# IMPRESIÓN DE ESTADÍSTICAS
# ESTADÍSTICAS ARCHIVO TC3
nombre_del_archivo = 'TC3.txt'
with open(nombre_del_archivo, 'r') as archivo:
    datos_del_archivo = [float(line.strip()) for line in archivo.readlines()]

# Realizado de cálculos
resultados_estadisticos = calcular_estadisticas(datos_del_archivo)

# Impresión de resultados y guardado en el archivo
resultados_dict = dict(zip(["media", "mediana", "moda", "varianza", "desviacion_estandar"], resultados_estadisticos))
imprimir_resultados(resultados_dict)
guardar_resultados(resultados_dict)

# IMPRESIÓN DE ESTADÍSTICAS
# ESTADÍSTICAS ARCHIVO TC4
nombre_del_archivo = 'TC4.txt'
with open(nombre_del_archivo, 'r') as archivo:
    datos_del_archivo = [float(line.strip()) for line in archivo.readlines()]

# Realizado de cálculos
resultados_estadisticos = calcular_estadisticas(datos_del_archivo)

# Impresión de resultados y guardado en el archivo
resultados_dict = dict(zip(["media", "mediana", "moda", "varianza", "desviacion_estandar"], resultados_estadisticos))
imprimir_resultados(resultados_dict)
guardar_resultados(resultados_dict)

# IMPRESIÓN DE ESTADÍSTICAS
# ESTADÍSTICAS ARCHIVO TC5
nombre_del_archivo = 'TC5.txt'
with open(nombre_del_archivo, 'r') as archivo:
    datos_del_archivo = [float(line.strip()) for line in archivo.readlines()]

# Realizado de cálculos
resultados_estadisticos = calcular_estadisticas(datos_del_archivo)

# Impresión de resultados y guardado en el archivo
resultados_dict = dict(zip(["media", "mediana", "moda", "varianza", "desviacion_estandar"], resultados_estadisticos))
imprimir_resultados(resultados_dict)
guardar_resultados(resultados_dict)

# IMPRESIÓN DE ESTADÍSTICAS
# ESTADÍSTICAS ARCHIVO TC6
nombre_del_archivo = 'TC6.txt'
with open(nombre_del_archivo, 'r') as archivo:
    datos_del_archivo = [float(line.strip()) for line in archivo.readlines()]

# Realizado de cálculos
resultados_estadisticos = calcular_estadisticas(datos_del_archivo)

# Impresión de resultados y guardado en el archivo
resultados_dict = dict(zip(["media", "mediana", "moda", "varianza", "desviacion_estandar"], resultados_estadisticos))
imprimir_resultados(resultados_dict)
guardar_resultados(resultados_dict)

# IMPRESIÓN DE ESTADÍSTICAS
# ESTADÍSTICAS ARCHIVO TC7
nombre_del_archivo = 'TC7.txt'
with open(nombre_del_archivo, 'r') as archivo:
    datos_del_archivo = [float(line.strip()) for line in archivo.readlines()]

# Realizado de cálculos
resultados_estadisticos = calcular_estadisticas(datos_del_archivo)

# Impresión de resultados y guardado en el archivo
resultados_dict = dict(zip(["media", "mediana", "moda", "varianza", "desviacion_estandar"], resultados_estadisticos))
imprimir_resultados(resultados_dict)
guardar_resultados(resultados_dict)

