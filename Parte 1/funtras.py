# Variables Globales importantes para las funciones
tol = 10 ** -8 # número entero positivo, que representa la cantidad de iteraciones máximas del motodo
iterMax = 2500 # número real positivo, que es el criterio de parada del error, donde |res(k+1)-res(k)| < tol
pi_t = 3.14159265358979323846 # cantidad de veces en la que la circunferencia de un círculo puede ser dividida por su diámetro

# La función factorial aproxima el valor de a!
# Sintáxis de la función: res = factorial (a)
# Parámetros de entrada:
#         a = número entero positivo
# Parámetros de salida:
#         res = aproximación del valor a!

def factorial (a):
    if a == 0: return 1
    else: return a * factorial(a - 1)

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
       
        res_n = res + a ** n * div_t((factorial(n)));
        
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
    while a < (-2 * pi_t) or a > (2 * pi_t):
        if a > (2 * pi_t): a -= (2 * pi_t) # Modificación de a entre ]0 , 2π]
        if a < (-2 * pi_t): a += (2 * pi_t) # Modificación de a entre [-2π , 0[
    
    res = 0

    for n in range(iterMax):
       
        res_n = res + ((-1) ** n * a ** (2 * n) * div_t(factorial(2 * n)))
        
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
    res = cos_t(a - pi_t * 0.5) 
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

# La función ln_t aproxima el valor de ln(a)
# Sintáxis de la función: res = ln_t (a)
# Parámetros de entrada:
#         a = número real mayor a cero
# Parámetros de salida:
#         res = aproximación del valor ln(a)

def ln_t (a):

    #Casos especiales
    if a <= 0: return False

    res = 0
    const = (a-1) * div_t(a+1)

    for n in range(iterMax):
       
        res_n = res + 2 * const * 1 * div_t(2 * n + 1) * const ** (2 * n);
        
        err = abs(res_n - res)
        res = res_n

        if err < tol:
            break

    return res

# La función log_t aproxima el valor de log_y(x)
# Sintáxis de la función: res = log_t (x, y)
# Parámetros de entrada:
#         x = número real mayor a cero
#         y = número entero mayor a 2
# Parámetros de salida:
#         res = aproximación del valor log_y(x)

def log_t (x , y):

    # Casos especiales
    if x <= 0: return False
    if y < 2 or not float.is_integer(y): return False

    res = ln_t(x) * div_t(ln_t(y))

    return res

# La función power_t aproxima el valor de x ^ y
# Sintáxis de la función: res = power_t (x, y)
# Parámetros de entrada:
#         x = número real
#         y = número real
# Parámetros de salida:
#         res = aproximación del valor x ^ y

def power_t (x , y):

    # Casos especiales
    if x <= 0 and not float.is_integer(y): return False
    elif x <= 0 and float.is_integer(y):
        if y % 2 == 0:
            res = exp_t(y * ln_t(x))
        else:
            res = -1 * exp_t(y * ln_t(-1 * x))
    else:
           res = exp_t(y * ln_t(x))     
    return res

# La función sinh_t aproxima el valor de sinh(a)
# Sintáxis de la función: res = sinh (a)
# Parámetros de entrada:
#         a = número real
# Parámetros de salida:
#         res = aproximación del valor sinh(a)

def sinh_t (a):

    res = 0;

    for n in range(iterMax):
       
        res_n = res + a ** (2 * n + 1) * div_t(factorial(2 * n + 1))
        
        err = abs(res_n - res)
        res = res_n

        if err < tol:
            break

    return res

# La función cosh_t aproxima el valor de cosh(a)
# Sintáxis de la función: res = cosh_t (a)
# Parámetros de entrada:
#         a = número real
# Parámetros de salida:
#         res = aproximación del valor cosh(a)

def cosh_t (a):
    
    res = 0

    for n in range(iterMax):
       
        res_n = res + a ** (2 * n) * div_t(factorial(2 * n))
        
        err = abs(res_n - res)
        res = res_n

        if err < tol:
            break

    return res

# La función tanh_t aproxima el valor de tanh(a)
# Sintáxis de la función: res = tanh_t (a)
# Parámetros de entrada:
#         a = número real
# Parámetros de salida:
#         res = aproximación del valor cosh(a)

def tanh_t (a):
    res = sinh_t(a) * div_t(cosh_t(a))
    return res

# La función sqrt_t aproxima el valor de raíz cuadrada de (a)
# Sintáxis de la función: res = sqrt_t (a)
# Parámetros de entrada:
#         a = número real
# Parámetros de salida:
#         res = aproximación del valor (a) ** (1/2)

def sqrt_t (a):
    # Casos especiales
    if a < 0 : return False
    if a == 0: return 0 

    res = a / 2

    for n in range(iterMax):

        res_n = res - (res ** 2 - a) * div_t(2 * res)

        err = abs(res_n - res)
        res = res_n

        if err < tol:
            break

    return res

# La función root_t aproxima el valor de raíz y de (x)
# Sintáxis de la función: res = root_t (x, y)
# Parámetros de entrada:
#         x = número real
#         y = número entero positivo mayor a 2
# Parámetros de salida:
#         res = aproximación del valor (x) ** (1/y)

def root_t (x, y):
    # Casos especiales
    if not float.is_integer(y) or y < 2: return False
    if y % 2 == 0 and x < 0 : return False

    res = x * 0.5

    for n in range(iterMax):

        res_n = res - (res ** y - x) * div_t(y * res ** (y - 1))

        err = abs(res_n - res)
        res = res_n

        if err < tol:
            break

    return res

# La función asin_t aproxima el valor de arcsin(a)
# Sintáxis de la función: res = asin_t (a)
# Parámetros de entrada:
#         a = número real entre -1 y 1
# Parámetros de salida:
#         res = aproximación del valor arcsin(a)

def asin_t (a):
    # Casos especiales
    if a > 1 or a < -1: return False
    if a == 1: return pi_t * div_t(2)
    if a == -1: return - pi_t * div_t(2)

    res = 0

    for n in range(iterMax):
       
        res_n = res + a ** (2 * n + 1) * factorial(2 * n) * div_t(4 ** n * factorial(n) ** 2 * (2 * n + 1))
        
        err = abs(res_n - res)
        res = res_n

        if err < tol:
            break

    return res

# La función atan_t aproxima el valor de arctan(a)
# Sintáxis de la función: res = atan_t (a)
# Parámetros de entrada:
#         a = número real
# Parámetros de salida:
#         res = aproximación del valor arctan(a)

def atan_t (a):

    res = 0

    for n in range(iterMax):
        if a > 1: 
            res_n = res + (-1) ** n * 1 * div_t ((2 * n + 1) * a ** (2 * n + 1))
        elif a < -1:
            res_n = res + (-1) ** n * 1 * div_t ((2 * n + 1) * a ** (2 * n + 1))
        else: 
            res_n = res + (-1) ** n * a ** (2 * n + 1) * div_t(2 * n + 1)
        
        err = abs(res_n - res)
        res = res_n;

        if err < tol:
            break

    if a > 1:
            res = -1 * res + pi_t * div_t(2)
    
    if a < -1:
            res = -1 * res - pi_t* div_t(2)

    return res

# La función acos_t aproxima el valor de arccos(a)
# Sintáxis de la función: res = acos_t (a)
# Parámetros de entrada:
#         a = número real entre -1 y 1
# Parámetros de salida:
#         res = aproximación del valor arcsin(a)

def acos_t (a):
    res = pi_t * div_t(2) - asin_t(a)
    return res

# La función sec_t aproxima el valor de sec(a)
# Sintáxis de la función: res = sec_t (a)
# Parámetros de entrada:
#         a = número real
# Parámetros de salida:
#         res = aproximación del valor sec(a)

def sec_t (a):
    res = div_t(cos_t(a))
    return res

# La función cot_t aproxima el valor de cot(a)
# Sintáxis de la función: res = cot_t (a)
# Parámetros de entrada:
#         a = número real
# Parámetros de salida:
#         res = aproximación del valor cot(a)

def cot_t (a):
    res = cos_t(a) / div_t(sen_t(a))
    return res

# La función csc_t aproxima el valor de csc(a)
# Sintáxis de la función: res = csc_t (a)
# Parámetros de entrada:
#         a = número real
# Parámetros de salida:
#         res = aproximación del valor csc(a)

def csc_t (a):
    res = div_t(sen_t(a))
    return res

