from funtras import *

# Método para verificar el correcto funcionamiento de las funciones trascendentes
def test():
    nom = root_t(cos_t(3.0 * div_t(7.0)) + ln_t(2.0),3.0) # Nominador de la prueba
    den = sinh_t(sqrt_t(2.0)) # Denominados de la prueba
    sum = atan_t(exp_t(-1.0)) # Sumando de la prueba
    res = nom * div_t(den) + sum # Resultado operación completa
    return res

print(test()) # Resultado en consola