def calcularMontanteJC(c, i, n):
    i /= 100
    INT = int(n)
    Q = n - INT
    M = c * ((1 + i) ** INT) * (1 + i * Q)
    return M
