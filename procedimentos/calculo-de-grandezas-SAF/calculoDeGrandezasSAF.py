from mensagens import *

from calcularMontanteSAF import calcularMontanteSAF
from calcularParcelasSAF import calcularParcelasSAF
from calcularFatorDeAmortizacaoSAF import calcularFatorDeAmortizacaoSAF
from verificarNumeroInteiro import verificarNumeroInteiro
from imprimirPalavraMesEmSingularOuPlural import imprimirPalavraMesEmSingularOuPlural


def calculoDeGrandezasSAF():
  while True:
    opcao11=int(input("\nDigite (9) para calcular o montante(T)\n    ou (8) para calcular as parcelas(P)\n    ou (7) para calcular o fator de amortização(A)\n    ou (0) para voltar\n    ou (-9) para encerrar: "))
    
    if opcao11==0:break
    if opcao11==-9:exit(0)
    
    if opcao11==9:
        print()
        i = float(input(taxaInserida))
        n = float(input(tempoInserido))
        parcelas=float(input(parcelaInserida))
        
        if n < 0:
            print(tempoMaiorIgualZero)
            calculoDeGrandezasSAF()
            break
        
        if parcelas < 0:
            print(parcelaMaiorIgualZero)
            calculoDeGrandezasSAF()
            break
        if i <= 0:
            print(taxaMaiorQueZero)
            calculoDeGrandezasSAF()
            break
        
        T=calcularMontanteSAF(n, i, parcelas)
        T=round(T,4)
        
        print(f"Montante = {T}")
    elif opcao11==8:
        print(MensagemPeriodoDeTempo)
        
        periodo = float(input(periodoTaxaInserido))
        i = float(input(taxaInserida))
        n = float(input(tempoInserido))
        T = float(input(montanteInserido))
        
        periodoInt = verificarNumeroInteiro(periodo)
        tempoInt = verificarNumeroInteiro(n)

        if not periodoInt:
            print(periodoInteiro)
            calculoDeGrandezasSAF()
            break
        if periodo <= 0:
            print(periodoMaiorQueZero)
            calculoDeGrandezasSAF()
            break 
        if not tempoInt:
            print(tempoInteiro)
            calculoDeGrandezasSAF()
            break
        if n <= 0:
            print(tempoMaiorQueZero)
            calculoDeGrandezasSAF()
            break
        if T < 0:
            print(montanteMaiorIgualZero)
            calculoDeGrandezasSAF()
            break
        if i <= 0:
            print(taxaMaiorQueZero)
            calculoDeGrandezasSAF()
            break
        
        parcelas=calcularParcelasSAF(i,n,T)
        parcelas=round(parcelas,4)
        
        mensagemMes = imprimirPalavraMesEmSingularOuPlural(periodo)
        
        print(f"Parcelas = {n}x de {parcelas} (a cada {periodo} {mensagemMes})")
    elif opcao11==7:
        print()
        i = float(input(taxaInserida))
        n = float(input(tempoInserido))
        
        if n < 0:
            print(tempoMaiorIgualZero)
            calculoDeGrandezasSAF()
            break
        if i <= 0:
            print(taxaMaiorQueZero)
            calculoDeGrandezasSAF()
            break
            
        A=calcularFatorDeAmortizacaoSAF(n, i)
        A=round(A,4)
        
        print(f"Fator de amortização = {A}")
    else:
        print(opcaoInvalida)
        calculoDeGrandezasSAF()
        break
        
    
