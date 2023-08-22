import funtras

def test():
    nom = funtras.root_t(funtras.cos_t(3 * funtras.div_t(7)) + funtras.ln_t(2),3)
    print(nom)
    den = funtras.sinh_t(funtras.sqrt_t(2))
    print(den)
    sum = funtras.atan_t(funtras.exp_t(-1))
    print(sum)

    res = nom * funtras.div_t(den) + sum
    return res

print(test())