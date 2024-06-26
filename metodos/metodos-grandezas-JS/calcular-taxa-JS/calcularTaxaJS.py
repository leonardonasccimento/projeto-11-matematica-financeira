def calcularTaxaJS(J, c, n, M, opcao5):
    if opcao5 == 9:
        i = J / (c * n)
        return i
    if opcao5 == 8:
        i = (1 / n) * ((M-c) / c)
        return i
