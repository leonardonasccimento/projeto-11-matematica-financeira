from math import e, log

def calcularTempoJC(J, c, i, M, opcao10):
    i /= 100
    if opcao10 == 9:
        n = log((c + J) / c) / log(1 + i)
        return n
    if opcao10 == 8:
        n = log(M / c) / log(1 + i)
        return n
