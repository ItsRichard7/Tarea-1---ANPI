from funtras import *

def test():
    nom = root_t(cos_t(3 * div_t(7)) + ln_t(2),3)
    print(nom)
    den = sinh_t(sqrt_t(2))
    print(den)
    sum = atan_t(exp_t(-1))
    print(sum)

    res = nom * div_t(den) + sum
    return res

print(test())