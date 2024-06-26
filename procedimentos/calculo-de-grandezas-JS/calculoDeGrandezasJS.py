from mensagens import *

from calcularMontanteJS import calcularMontanteJS

from calculoDeCapitalJS import calculoDeCapitalJS
from calculoDeJurosJS import calculoDeJurosJS
from calculoDeTaxaJS import calculoDeTaxaJS
from calculoDeTempoJS import calculoDeTempoJS


def calculoDeGrandezasJS():
  while True:
    opcao2 = int(input(opcoesGrandezas))
    
    if opcao2==0:break
    if opcao2==-9:exit(0)
    
    if opcao2 == 9:
        print()
        c = float(input(capitalInserido))
        i = float(input(taxaInserida))
        n = float(input(tempoInserido))
        
        if n < 0:
            print(tempoMaiorIgualZero)
            calculoDeGrandezasJS()
            break
        if c < 0:
            print(capitalMaiorIgualZero)
            calculoDeGrandezasJS()
            break
        if i < 0:
            print(taxaMaiorIgualZero)
            calculoDeGrandezasJS()
            break

        M = calcularMontanteJS(c, i, n)
        M = round(M, 4)

        print(f"Montante = {M}")
    elif opcao2 == 8:
        calculoDeCapitalJS()
    elif opcao2 == 7:
        calculoDeTaxaJS()
    elif opcao2 == 6:
        calculoDeTempoJS()
    elif opcao2 == 5:
        calculoDeJurosJS()
    else:
        print(opcaoInvalida)
        calculoDeGrandezasJS()
        break
