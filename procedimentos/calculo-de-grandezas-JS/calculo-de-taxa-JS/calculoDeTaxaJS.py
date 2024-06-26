from mensagens import *

from calcularTaxaJS import calcularTaxaJS
from verificarNumeroInteiro import verificarNumeroInteiro
from imprimirPalavraMesEmSingularOuPlural import imprimirPalavraMesEmSingularOuPlural

def calculoDeTaxaJS():
    while True:
        opcao5 = int(
            input(mensagemTaxa)
        )
        
        if opcao5==0:break
        if opcao5==-9:exit(0)

        if opcao5 == 9:
            print(MensagemPeriodoDeTempo)
            periodo = float(input(periodoTaxaInserido))
            c = float(input(capitalInserido))
            n = float(input(tempoInserido))
            J = float(input(jurosInserido))
            M = 1
            
            periodoInt = verificarNumeroInteiro(periodo)

            if not periodoInt:
                print(periodoInteiro)
                calculoDeTaxaJS()
                break
            if periodo <= 0:
                print(periodoMaiorQueZero)
                calculoDeTaxaJS()
                break
                
            if c <= 0:
                print(capitalMaiorQueZero)
                calculoDeTaxaJS()
                break
            if n <= 0:
                print(tempoMaiorQueZero)
                calculoDeTaxaJS()
                break
            if J < 0:
                print(jurosMaiorIgualZero)
                calculoDeTaxaJS()
                break

            i = calcularTaxaJS(J, c, n, M, opcao5)
            i = round(i, 4)

            mensagemMes = imprimirPalavraMesEmSingularOuPlural(periodo)

            print(f"Taxa = ({i} ou {i*100}%) (a cada {periodo} {mensagemMes})")
        elif opcao5 == 8:
            print(MensagemPeriodoDeTempo)
            periodo = float(input(periodoTaxaInserido))
            c = float(input(capitalInserido))
            n = float(input(tempoInserido))
            M = float(input(montanteInserido))
            J = 1
            
            periodoInt = verificarNumeroInteiro(periodo)

            if not periodoInt:
                print(periodoInteiro)
                calculoDeTaxaJS()
                break
            if periodo <= 0:
                print(periodoMaiorQueZero)
                calculoDeTaxaJS()
                break
                
            if c <= 0:
                print(capitalMaiorQueZero)
                calculoDeTaxaJS()
                break
            if n <= 0:
                print(tempoMaiorQueZero)
                calculoDeTaxaJS()
                break
            if M < 0:
                print(montanteMaiorIgualZero)
                calculoDeTaxaJS()
                break

            i = calcularTaxaJS(J, c, n, M, opcao5)
            i = round(i, 4)

            mensagemMes = imprimirPalavraMesEmSingularOuPlural(periodo)

            print(f"Taxa = ({i} ou {i*100}%) (a cada {periodo} {mensagemMes})")
        else:
            print(opcaoInvalida)
            calculoDeTaxaJS()
            break
