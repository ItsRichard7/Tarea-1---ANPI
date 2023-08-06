# Variables Globales importantes para las funciones
tol = 10 ** -8 # número entero positivo, que representa la cantidad de iteraciones moximas del motodo
iterMax = 2500 # número real positivo, que es el criterio de parada del error, donde |res(k+1)-res(k)| < tol
pi = 3.1415926535897932 # cantidad de veces en la que la circunferencia de un círculo puede ser dividida por su diámetro

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
# Sintáxis de la función: epsilon ** n = get_epsilon (a)
# Parámetros de entrada:
#         a = número real positivo
# Parámetros de salida:
#         epsilon ** n = valor inicial de la serie

def get_epsilon (a):

    epsilon = 2.2204 * 10 ** -16

    if a > 0 and a < 1: return epsilon
    elif a > factorial(0) and a <= factorial(20): return epsilon ** 2
    elif a > factorial(20) and a <= factorial(40): return epsilon ** 4
    elif a > factorial(40) and a <= factorial(60): return epsilon ** 8
    elif a > factorial(60) and a <= factorial(80): return epsilon ** 11
    elif a > factorial(80) and a <= factorial(100): return epsilon ** 15
    else: return 0

# La función div_t aproxima el valor de 1/a
# Sintáxis de la función: res = div_t (a)
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

    for n in range(iterMax): # Inicio de la serie recursiva
       
        res_n = res * (2 - a * res)
        
        err = abs(res_n - res)
        res = res_n

        if err == 0:
            break

    if negative == False: return res
    else: return -1 * res

# La función exp aproxima el valor de e^a
# Sintáxis de la función: res = exp_t (a)
# Parámetros de entrada:
#         a = número real
# Parámetros de salida:
#         res = aproximación del valor e^a

def exp_t (a):

    res = 0

    for n in range(iterMax):
       
        res_n = res + a ** n * div_t(factorial(n));
        
        err = abs(res_n - res)
        res = res_n

        if err < tol:
            break

    return res

# La función cos aproxima el valor de cos(a)
# Sintáxis de la función: res = cos_t (a)
# Parámetros de entrada:
#         a = número real
# Parámetros de salida:
#         res = aproximación del valor cos(a)

def cos_t (a):
    # Casos especiales
    if a == 0: return 1
    if a > 0 : a = a - (2 * pi * int(a * div_t(2 * pi)))
    else: a = a + (2 * pi * abs(int(a * div_t(2 * pi))))

    res = 0
    for n in range(iterMax):
       
        res_n = res + (-1) ** n * a ** (2 * n) * div_t(factorial(2 * n))
        
        err = abs(res_n - res)
        res = res_n

        if err < tol:
            break

    return res

# La función sen_t aproxima el valor de sen(a)
# Sintáxis de la función: res = sen_t (a)
# Parámetros de entrada:
#         a = número real
# Parámetros de salida:
#         res = aproximación del valor sen(a)

def sen_t (a):
    if a == 0: return 0
    res = cos_t(a - pi * div_t(2)) 
    return res

# La función tan_t aproxima el valor de tan(a)
# Sintáxis de la función: res = tan_t (a)
# Parámetros de entrada:
#         a = número real
# Parámetros de salida:
#         res = aproximación del valor tan(a)

def tan_t (a):
    res = sen_t(a) * div_t(cos_t(a))
    return res
