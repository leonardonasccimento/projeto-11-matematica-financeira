def calcularCapitalJC(i, n, opcao8, M, J):
    i /= 100
    INT = int(n)
    Q = n - INT
    if opcao8 == 9:
        c = M - J
        return c
    if opcao8 == 8:
        c = M / (((1 + i) ** INT) * (1 + i * Q))
        return c
    if opcao8 == 7:
        P = ((1 + i) ** INT) * (1 + i * Q)
        if P==1:
            return -1
        c = J / (P - 1)
        return c
