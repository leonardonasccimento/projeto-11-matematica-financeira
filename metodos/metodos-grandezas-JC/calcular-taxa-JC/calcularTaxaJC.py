def calcularTaxaJC(J, c, n, M, opcao9):
    if opcao9 == 9:
        i = (((c + J) / c) ** (1 / n)) - 1
        return i
    if opcao9 == 8:
        i = ((M / c) ** (1 / n)) - 1
        return i
