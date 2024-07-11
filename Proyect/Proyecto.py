#!/usr/bin/env python3

"""
Módulo para simular la evolución temporal de un sistema cuántico utilizando el método de Runge-Kutta de cuarto orden 
y paralelización mediante hilos.
"""

import numpy as np
import time
from concurrent.futures import ThreadPoolExecutor

def estado_inicial(N):
    """
    Función para crear el estado inicial (grilla).

    Args:
        N (int): Tamaño de la grilla.

    Returns:
        numpy.ndarray: Arreglo NumPy que representa el estado inicial con un fermión en la posición central.
    """
    estado_inicial = np.zeros(N)
    estado_inicial[N//2] = 1
    return estado_inicial

def matriz_ham(t_i, epsilon):
    """
    Función para crear la matriz Hamiltoniana.

    Args:
        t_i (numpy.ndarray): Elementos fuera de la diagonal de la matriz Hamiltoniana.
        epsilon (numpy.ndarray): Valores de la diagonal de la matriz Hamiltoniana.

    Returns:
        numpy.ndarray: Matriz Hamiltoniana generada.
    """
    N = epsilon.size
    matriz = np.zeros((N, N))
    matriz[np.diag_indices(N)] = epsilon
    np.fill_diagonal(matriz[:,1:], t_i)
    np.fill_diagonal(matriz[1:,:], t_i)
    return matriz

def ecu_schrodinger_rk4(matriz_ham, grilla_actual, dt):
    """
    Función para la evolución temporal según la ecuación de Schrödinger con el método de Runge-Kutta de cuarto orden.

    Args:
        matriz_ham (numpy.ndarray): Matriz Hamiltoniana que define el sistema físico.
        grilla_actual (numpy.ndarray): Estado actual de la función de onda.
        dt (float): Paso de tiempo.

    Returns:
        numpy.ndarray: Nuevo estado de la grilla después de la evolución temporal.
    """
    k1 = dt * ecu_sch_paralelo(matriz_ham, grilla_actual)
    k2 = dt * ecu_sch_paralelo(matriz_ham, grilla_actual + 0.5 * k1)
    k3 = dt * ecu_sch_paralelo(matriz_ham, grilla_actual + 0.5 * k2)
    k4 = dt * ecu_sch_paralelo(matriz_ham, grilla_actual + k3)
    grilla_nueva = grilla_actual + (k1 + 2*k2 + 2*k3 + k4) / 6
    return grilla_nueva

def parte_ecu_sch(matriz_ham, grilla_actual, start, end):
    """
    Función para dividir el trabajo entre varios hilos para la ecuación de Schrödinger.

    Args:
        matriz_ham (numpy.ndarray): Matriz Hamiltoniana que define el sistema físico.
        grilla_actual (numpy.ndarray): Estado actual de la función de onda.
        start (int): Índice de inicio para la porción de trabajo del hilo.
        end (int): Índice de fin para la porción de trabajo del hilo.

    Returns:
        numpy.ndarray: Resultado de la parte de la ecuación de Schrödinger calculada por el hilo.
    """
    return -1j * matriz_ham[start:end, :] @ grilla_actual

def ecu_sch_paralelo(matriz_ham, grilla_actual, num_hilos=1):
    """
    Función para paralelizar el cálculo de la ecuación de Schrödinger.

    Args:
        matriz_ham (numpy.ndarray): Matriz Hamiltoniana que define el sistema físico.
        grilla_actual (numpy.ndarray): Estado actual de la función de onda.
        num_hilos (int, optional): Número de hilos a utilizar para la paralelización. Default es 1.

    Returns:
        numpy.ndarray: Resultado de la ecuación de Schrödinger después de la paralelización.
    """
    N = len(grilla_actual)
    step = N // num_hilos
    resultados = np.zeros_like(grilla_actual, dtype=complex)

    with ThreadPoolExecutor(max_workers=num_hilos) as executor:
        futuros = []
        for i in range(num_hilos):
            start = i * step
            end = (i + 1) * step if i != num_hilos - 1 else N
            futuros.append(executor.submit(parte_ecu_sch, matriz_ham, grilla_actual, start, end))
        
        for future in futuros:
            resultado = future.result()
            start = futuros.index(future) * step
            end = (start + step) if futuros.index(future) != num_hilos - 1 else N
            resultados[start:end] = resultado
    
    return resultados

def inicio(t_i, epsilon, tiempos):
    """
    Función principal para evolucionar la grilla en el tiempo.

    Args:
        t_i (numpy.ndarray): Elementos fuera de la diagonal de la matriz Hamiltoniana.
        epsilon (numpy.ndarray): Valores de la diagonal de la matriz Hamiltoniana.
        tiempos (numpy.ndarray): Tiempos para los cuales se evaluará la función de onda.

    Returns:
        tuple: Tupla con la forma de la función de onda al cuadrado en cada tiempo y el estado final de la grilla.
    """
    dt = tiempos[1] - tiempos[0]
    N = epsilon.size
    grilla_actual = estado_inicial(N)
    matriz_hamiltoniana = matriz_ham(t_i, epsilon)
    shape = [0.0 for i in range(len(tiempos))]
    shape[0] = np.abs(grilla_actual)**2
    for t in range(1, tiempos.size):
        shape[t] = np.abs(grilla_actual)**2
        grilla_actual = ecu_schrodinger_rk4(matriz_hamiltoniana, grilla_actual, dt)
        
    return shape, grilla_actual

if __name__ == "__main__":
    # Ejemplo de uso
    N = 100
    epsilon_val = 0.5 * np.ones(N)
    t_i_val = 1 * np.ones(N)
    tiempos_val = np.linspace(0.0, 25, 200)

    num_hilos_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    for num_hilos in num_hilos_lista:
        print(f"Ejecutando con {num_hilos} hilo(s)...")
        start_time = time.time()
        s, g = inicio(t_i_val, epsilon_val, tiempos_val)
        elapsed_time = time.time() - start_time
        print(f"Tiempo de ejecución: {elapsed_time:.4f} segundos")
        print()



