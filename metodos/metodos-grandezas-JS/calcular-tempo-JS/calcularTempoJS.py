def calcularTempoJS(J, c, i, M, opcao6):
    i /= 100
    if opcao6 == 9:
        n = J / (c * i)
        return n
    if opcao6 == 8:
        n = (1 / i) * ((M-c) / c)
        return n
