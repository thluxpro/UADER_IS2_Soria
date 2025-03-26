#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

# Función para calcular el factorial
def factorial(n):
    if n < 0:
        return "Error: El factorial de un número negativo no está definido."
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

# Obtener el argumento desde la línea de comandos o solicitar entrada manualmente
if len(sys.argv) < 2:
    entrada = input("Ingrese un número o un rango (ejemplo: 4-8, -10, 5-): ")
else:
    entrada = sys.argv[1]

# Procesar el argumento para admitir rangos
if '-' in entrada:
    partes = entrada.split('-')
    desde = int(partes[0]) if partes[0] else 1  # Si está vacío, asumir 1
    hasta = int(partes[1]) if partes[1] else 60  # Si está vacío, asumir 60
else:
    desde = hasta = int(entrada)  # Si no hay rango, tomar un solo número

# Calcular y mostrar los factoriales en el rango
for i in range(desde, hasta + 1):
    print(f"Factorial de {i}! es {factorial(i)}")

