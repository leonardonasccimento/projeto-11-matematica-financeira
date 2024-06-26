from mensagens import *

from calcularJuros import calcularJuros

from calcularMontanteJC import calcularMontanteJC

from calculoDeCapitalJC import calculoDeCapitalJC
from calculoDeTempoJC import calculoDeTempoJC
from calculoDeTaxaJC import calculoDeTaxaJC

              
def calculoDeGrandezasJC():
  while True:
    opcao7 = int(input(opcoesGrandezas))
    
    if opcao7==0:break
    if opcao7==-9:exit(0)
    
    if opcao7 == 9:
        print()
        c = float(input(capitalInserido))
        i = float(input(taxaInserida))
        n = float(input(tempoInserido))

        if n < 0:
            print(tempoMaiorIgualZero)
            calculoDeGrandezasJC()
            break
        if c < 0:
            print(capitalMaiorIgualZero)
            calculoDeGrandezasJC()
            break
        if i < 0:
            print(taxaMaiorIgualZero)
            calculoDeGrandezasJC()
            break

        M = calcularMontanteJC(c, i, n)
        M = round(M, 4)

        print(f"Montante = {M}")
    elif opcao7 == 8:
        calculoDeCapitalJC()
    elif opcao7 == 7:
        calculoDeTaxaJC()
    elif opcao7 == 6:
        calculoDeTempoJC()
    elif opcao7 == 5:
        print()
        c = float(input(capitalInserido))
        M = float(input(montanteInserido))
        opcao4, i, n = 8, 1, 1

        if c < 0:
            print(capitalMaiorIgualZero)
            calculoDeGrandezasJC()
            break
        if M < 0:
            print(montanteMaiorIgualZero)
            calculoDeGrandezasJC()
            break

        J = calcularJuros(c, i, n, opcao4, M)
        J = round(J, 4)

        print(f"Juros = {J}")
    else:
        print(opcaoInvalida)
        calculoDeGrandezasJC()
        break
    



