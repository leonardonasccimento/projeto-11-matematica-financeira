def calcularMontanteSAF(n,i,parcelas):
    i/=100
    B=(1-(1+i)**(-n))
    T=(parcelas/i)*B
    
    return T
    