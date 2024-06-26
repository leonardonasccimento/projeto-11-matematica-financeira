from mensagens import *

from calcularTempoJC import calcularTempoJC
from verificarNumeroInteiro import verificarNumeroInteiro
from imprimirPalavraMesEmSingularOuPlural import imprimirPalavraMesEmSingularOuPlural
from imprimirPalavraUnidadeEmSingularOuPlural import imprimirPalavraUnidadeEmSingularOuPlural


def calculoDeTempoJC():
    while True:
        opcao10 = int(
            input(
                mensagemTempo
            )
        )
        
        if opcao10==0:break
        if opcao10==-9:exit(0)
        
        if opcao10 == 9:
            print(MensagemPeriodoDeTempo)
            periodo=float(input(periodoTaxaInserido))
            i = float(input(taxaInserida))
            c = float(input(capitalInserido))
            J = float(input(jurosInserido))
            M = 1
            
            periodoInt = verificarNumeroInteiro(periodo)
            
            if not periodoInt:
                print(periodoInteiro)
                calculoDeTempoJC()
                break
            if periodo <= 0:
                print(periodoMaiorQueZero)
                calculoDeTempoJC()
                break
                
            if c <= 0:
                print(capitalMaiorQueZero)
                calculoDeTempoJC()
                break
            if i <= 0:
                print(taxaMaiorQueZero)
                calculoDeTempoJC()
                break
            if J < 0:
                print(jurosMaiorIgualZero)
                calculoDeTempoJC()
                break

            n = calcularTempoJC(J, c, i, M, opcao10)
            n = round(n, 4)
            
            mensagemUnidade=imprimirPalavraUnidadeEmSingularOuPlural(n)
            mensagemMes = imprimirPalavraMesEmSingularOuPlural(periodo)

            print(f"Tempo = {n} ({mensagemUnidade} de tempo com período de ({periodo} {mensagemMes}))")
        elif opcao10 == 8:
            print(MensagemPeriodoDeTempo)
            periodo=float(input(periodoTaxaInserido))
            c = float(input(capitalInserido))
            i = float(input(taxaInserida))
            M = float(input(montanteInserido))
            J = 1
            
            periodoInt = verificarNumeroInteiro(periodo)
            
            if not periodoInt:
                print(periodoInteiro)
                calculoDeTempoJC()
                break
            if periodo <= 0:
                print(periodoMaiorQueZero)
                calculoDeTempoJC()
                break

            if c <= 0:
                print(capitalMaiorQueZero)
                calculoDeTempoJC()
                break
            if i <= 0:
                print(taxaMaiorQueZero)
                calculoDeTempoJC()
                break
            if M < 0:
                print(montanteMaiorIgualZero)
                calculoDeTempoJC()
                break

            n = calcularTempoJC(J, c, i, M, opcao10)
            n = round(n, 4)
            
            m=abs(n)
            mensagemUnidade=imprimirPalavraUnidadeEmSingularOuPlural(m)
            mensagemMes = imprimirPalavraMesEmSingularOuPlural(periodo)

            print(f"Tempo = {n} ({mensagemUnidade} de tempo com período de ({periodo} {mensagemMes}))")
        else:
            print(opcaoInvalida)
            calculoDeTempoJC()
            break
 