from mensagens import *

from calcularCapitalJS import calcularCapitalJS

def calculoDeCapitalJS():
    while True:
        opcao3 = int(input(mensagemCapital))
        
        if opcao3==0:break
        if opcao3==-9:exit(0)

        if opcao3 == 9:
            print()
            M = float(input(montanteInserido))
            J = float(input(jurosInserido))
            i, n = 1, 1
            
            if M < 0:
                print(montanteMaiorIgualZero)
                calculoDeCapitalJS()
                break
            if J < 0:
                print(jurosMaiorIgualZero)
                calculoDeCapitalJS()
                break

            c = calcularCapitalJS(i, n, opcao3, M, J)
            c = round(c, 4)

            print(f"Capital = {c}")
        elif opcao3 == 8:
            print()
            i = float(input(taxaInserida))
            n = float(input(tempoInserido))
            M = float(input(montanteInserido))
            J = 1
            
            if n < 0:
                print(tempoMaiorIgualZero)
                calculoDeCapitalJS()
                break
            if i < 0:
                print(taxaMaiorIgualZero)
                calculoDeCapitalJS()
                break
            if M < 0:
                print(montanteMaiorIgualZero)
                calculoDeCapitalJS()
                break

            c = calcularCapitalJS(i, n, opcao3, M, J)
            c = round(c, 4)

            print(f"Capital = {c}")
        elif opcao3 == 7:
            print()
            i = float(input(taxaInserida))
            n = float(input(tempoInserido))
            J = float(input(jurosInserido))
            M = 1
            
            if n <= 0:
                print(tempoMaiorQueZero)
                calculoDeCapitalJS()
                break
            if i <= 0:
                print(taxaMaiorQueZero)
                calculoDeCapitalJS()
                break
            if J < 0:
                print(jurosMaiorIgualZero)
                calculoDeCapitalJS()
                break

            c = calcularCapitalJS(i, n, opcao3, M, J)
            c = round(c, 4)

            print(f"Capital = {c}")
        else:
            print(opcaoInvalida)
            calculoDeCapitalJS()
            break
  