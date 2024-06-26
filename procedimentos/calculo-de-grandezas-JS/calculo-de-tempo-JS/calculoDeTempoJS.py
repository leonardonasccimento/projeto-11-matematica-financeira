from mensagens import *

from calcularTempoJS import calcularTempoJS
from verificarNumeroInteiro import verificarNumeroInteiro
from imprimirPalavraMesEmSingularOuPlural import imprimirPalavraMesEmSingularOuPlural
from imprimirPalavraUnidadeEmSingularOuPlural import imprimirPalavraUnidadeEmSingularOuPlural

def calculoDeTempoJS():
    while True:
        opcao6 = int(
            input(
                mensagemTempo
            )
        )
        
        if opcao6==0:break
        if opcao6==-9:exit(0)
        
        if opcao6 == 9:
            print(MensagemPeriodoDeTempo)
            periodo=float(input(periodoTaxaInserido))
            c = float(input(capitalInserido))
            i = float(input(taxaInserida))
            J = float(input(jurosInserido))
            M = 1
            
            periodoInt = verificarNumeroInteiro(periodo)
            
            if not periodoInt:
                print(periodoInteiro)
                calculoDeTempoJS()
                break
            if periodo <= 0:
                print(periodoMaiorQueZero)
                calculoDeTempoJS()
                break
                
            if c <= 0:
                print(capitalMaiorQueZero)
                calculoDeTempoJS()
                break
            if J < 0:
                print(jurosMaiorIgualZero)
                calculoDeTempoJS()
                break
            if i <= 0:
                print(taxaMaiorQueZero)
                calculoDeTempoJS()
                break

            n = calcularTempoJS(J, c, i, M, opcao6)
            n = round(n, 4)

            mensagemUnidade=imprimirPalavraUnidadeEmSingularOuPlural(n)
            mensagemMes = imprimirPalavraMesEmSingularOuPlural(periodo)

            print(f"Tempo = {n} ({mensagemUnidade} de tempo com período de ({periodo} {mensagemMes}))")
        elif opcao6 == 8:
            print(MensagemPeriodoDeTempo)
            periodo=float(input(periodoTaxaInserido))
            c = float(input(capitalInserido))
            i = float(input(taxaInserida))
            M = float(input(montanteInserido))
            J = 1
            
            periodoInt = verificarNumeroInteiro(periodo)
            
            if not periodoInt:
                print(periodoInteiro)
                calculoDeTempoJS()
                break
            if periodo <= 0:
                print(periodoMaiorQueZero)
                calculoDeTempoJS()
                break
            
            if c <= 0:
                print(capitalMaiorQueZero)
                calculoDeTempoJS()
                break
            if M < 0:
                print(montanteMaiorIgualZero)
                calculoDeTempoJS()
                break
            if i <= 0:
                print(taxaMaiorQueZero)
                calculoDeTempoJS()
                break

            n = calcularTempoJS(J, c, i, M, opcao6)
            n = round(n, 4)

            m=abs(n)
            mensagemUnidade=imprimirPalavraUnidadeEmSingularOuPlural(m)
            mensagemMes = imprimirPalavraMesEmSingularOuPlural(periodo)

            print(f"Tempo = {n} ({mensagemUnidade} de tempo com período de ({periodo} {mensagemMes}))")
        else:
            print(opcaoInvalida)
            calculoDeTempoJS()
            break
  