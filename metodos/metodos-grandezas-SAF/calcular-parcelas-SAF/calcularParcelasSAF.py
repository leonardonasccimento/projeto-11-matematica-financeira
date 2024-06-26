def calcularParcelasSAF(i, n, T):
    i/=100
    B=(1-(1+i)**(-n))
    parcelas=(T*i)/B
    return parcelas