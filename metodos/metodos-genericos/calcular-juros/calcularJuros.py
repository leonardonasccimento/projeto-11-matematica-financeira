def calcularJuros(c, i, n, opcao4, M):
    i /= 100
    if opcao4 == 9:
        J = c * i * n
        return J
    if opcao4 == 8:
        J = M - c
        return J


