from mensagens import *

from calcularCapitalJC import calcularCapitalJC


def calculoDeCapitalJC():
    while True:
        opcao8 = int(input(mensagemCapital))
        
        if opcao8==0:break
        if opcao8==-9:exit(0)

        if opcao8 == 9:
            print()
            M = float(input(montanteInserido))
            J = float(input(jurosInserido))
            i, n = 1, 1

            if M < 0:
                print(montanteMaiorIgualZero)
                calculoDeCapitalJC()
                break
            if J < 0:
                print(jurosMaiorIgualZero)
                calculoDeCapitalJC()
                break

            c = calcularCapitalJC(i, n, opcao8, M, J)
            c = round(c, 4)

            print(f"Capital = {c}")
        elif opcao8 == 8:
            print()
            i = float(input(taxaInserida))
            n = float(input(tempoInserido))
            M = float(input(montanteInserido))
            J = 1

            if n < 0:
                print(tempoMaiorIgualZero)
                calculoDeCapitalJC()
                break
            if M < 0:
                print(montanteMaiorIgualZero)
                calculoDeCapitalJC()
                break
            if i < 0:
                print(taxaMaiorIgualZero)
                calculoDeCapitalJC()
                break

            c = calcularCapitalJC(i, n, opcao8, M, J)
            c = round(c, 4)

            print(f"Capital = {c}")
        elif opcao8 == 7:
            print()
            i = float(input(taxaInserida))
            n = float(input(tempoInserido))
            J = float(input(jurosInserido))
            M = 1

            if n <= 0:
                print(tempoMaiorQueZero)
                calculoDeCapitalJC()
                break
            if J < 0:
                print(jurosMaiorIgualZero)
                calculoDeCapitalJC()
                break
            if i <= 0:
                print(taxaMaiorQueZero)
                calculoDeCapitalJC()
                break

            c = calcularCapitalJC(i, n, opcao8, M, J)

            if c == -1:
                print("\nO resultado não pode ser calculado. Rever a taxa e/ou o tempo.")

            c = round(c, 4)

            print(f"Capital = {c}")
        else:
            print(opcaoInvalida)
            calculoDeCapitalJC()
            break
