from mensagens import *

from calcularTaxaJC import calcularTaxaJC
from verificarNumeroInteiro import verificarNumeroInteiro
from imprimirPalavraMesEmSingularOuPlural import imprimirPalavraMesEmSingularOuPlural


def calculoDeTaxaJC():
    while True:
        opcao9 = int(
            input(mensagemTaxa)
        )
        
        if opcao9==0:break
        if opcao9==-9:exit(0)

        if opcao9 == 9:
            print(
            "\nCaso valor do tempo flutuante, convém converter para um valor inteiro."
            )
            print(MensagemPeriodoDeTempo) 
            periodo = float(input(periodoTaxaInserido))
            c = float(input(capitalInserido))
            n = float(input(tempoInserido))
            J = float(input(jurosInserido))
            M = 1

            periodoInt = verificarNumeroInteiro(periodo)
            tempoInt = verificarNumeroInteiro(n)

            if not periodoInt:
                print(periodoInteiro)
                calculoDeTaxaJC()
                break
            if periodo <= 0:
                print(periodoMaiorQueZero)
                calculoDeTaxaJC()
                break
                
            if c <= 0:
                print(capitalMaiorQueZero)
                calculoDeTaxaJC()
                break
            if not tempoInt:
                print(tempoInteiro)
                calculoDeTaxaJC()
                break
            if n <= 0:
                print(tempoMaiorQueZero)
                calculoDeTaxaJC()
                break
            if J < 0:
                print(jurosMaiorIgualZero)
                calculoDeTaxaJC()
                break

            i = calcularTaxaJC(J, c, n, M, opcao9)
            i = round(i, 4)

            mensagemMes = imprimirPalavraMesEmSingularOuPlural(periodo)

            print(f"Taxa = ({i} ou {i*100}%) (a cada {periodo} {mensagemMes})")
        elif opcao9 == 8:
            print(
            "\nCaso valor do tempo flutuante, convém converter para um valor inteiro."
            )
            print(MensagemPeriodoDeTempo) 
            periodo = float(input(periodoTaxaInserido))
            c = float(input(capitalInserido))
            n = float(input(tempoInserido))
            M = float(input(montanteInserido))
            J = 1

            periodoInt = verificarNumeroInteiro(periodo)
            tempoInt = verificarNumeroInteiro(n)

            if not periodoInt:
                print(periodoInteiro)
                calculoDeTaxaJC()
                break
            if periodo <= 0:
                print(periodoMaiorQueZero)
                calculoDeTaxaJC()
                break
            if c <= 0:
                print(capitalMaiorQueZero)
                calculoDeTaxaJC()
                break
            if not tempoInt:
                print(tempoInteiro)
                calculoDeTaxaJC()
                break
            if n <= 0:
                print(tempoMaiorQueZero)
                calculoDeTaxaJC()
                break
            if M < 0:
                print(montanteMaiorIgualZero)
                calculoDeTaxaJC()
                break

            i = calcularTaxaJC(J, c, n, M, opcao9)
            i = round(i, 4)

            mensagemMes = imprimirPalavraMesEmSingularOuPlural(periodo)

            print(f"Taxa = ({i} ou {i*100}%) (a cada {periodo} {mensagemMes})")
        else:
            print(opcaoInvalida)
            calculoDeTaxaJC()
            break
  