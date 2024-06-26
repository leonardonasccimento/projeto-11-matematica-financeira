def calcularTaxaEquivalente(i1, p1, p2):
    i1 /= 100
    if p1 < p2:
        if p2 % p1 != 0:
            return False
        k = p2 / p1
        i2 = ((1 + i1) ** k) - 1
        return i2
    if p1 > p2:
        if p1 % p2 != 0:
            return False
        k = p1 / p2
        i2 = ((1 + i1) ** (1 / k)) - 1
        return i2
    if p1 == p2:
        return i1
