def calcularCapitalJS(i, n, opcao3, M, J):
    i /= 100
    if opcao3==9:
        c=M-J
        return c
    if opcao3 == 8:
        c = M / (1 + i * n)
        return c
    if opcao3 == 7:
        c = J / (i * n)
        return c
