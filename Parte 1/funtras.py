# Variables Globales importantes para las funciones
tol = 10 ** -8
iterMax = 2500

# La función factorial aproxima el valor de a!
# Sintáxis de la función: res = factorial (a)
# Parámetros de entrada:
#         a = número entero positivo
# Parámetros de salida:
#         res = aproximación del valor a!

def factorial (a):
    if a == 0: return 1
    else: return a * factorial(a-1)

# La funcion get_epsilon calcula el valor inicial para la serie recursiva del inverso multiplicativo de un número
def get_epsilon (a):

    epsilon = 2.2204 * 10 ** -16

    if a > 0 and a < 1: return epsilon
    elif a > factorial(0) and a <= factorial(20): return epsilon ** 2
    elif a > factorial(20) and a <= factorial(40): return epsilon ** 4
    elif a > factorial(40) and a <= factorial(60): return epsilon ** 8
    elif a > factorial(60) and a <= factorial(80): return epsilon ** 11
    elif a > factorial(80) and a <= factorial(100): return epsilon ** 15

# La función div_t aproxima el valor de 1/a
# Sintáxis de la función: res = inv (a)
# Parámetros de entrada:
#         a = número real
# Parámetros de salida:
#         res = aproximación del valor arcsin(a)

def div_t (a):

    # Casos especiales
    if a == 1: return 1
    if a == 0: return 0

    # Indicador de si el número ingresado es negativo
    negative = False 
    if a < 0: 
        negative = True
        a *= -1

    res = get_epsilon(a) # Calculo del valor inicial para iniciar la serie recursiva

    for iter in range(iterMax): # Inicio de la serie recursiva
       
        res_n = res * (2 - a * res)
        
        err = abs(res_n - res)
        res = res_n

        if err < 10**-32:
            break
    if negative == False: return res
    else: return -1 * res