def calcularFatorDeAmortizacaoSAF(n,i):
    i/=100
    A=(1-(1+i)**(-n))/i
    return A