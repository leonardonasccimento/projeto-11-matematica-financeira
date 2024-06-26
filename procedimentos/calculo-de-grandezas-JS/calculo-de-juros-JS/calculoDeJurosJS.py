from mensagens import *

from calcularJuros import calcularJuros


def calculoDeJurosJS():
    while True:
        opcao4 = int(
            input(
                f"\nDigite (9) para calcular juros utilizando capital, taxa e tempo\n    ou (8) para calcular juros utilizando capital e montante\n    ou (0) para voltar\n    ou (-9) para encerrar: "
            )
        )
        
        if opcao4==0:break
        if opcao4==-9:exit(0)

        if opcao4 == 9:
            print()
            c = float(input(capitalInserido))
            i = float(input(taxaInserida))
            n = float(input(tempoInserido))
            M = 1
            
            if c < 0:
                print(capitalMaiorIgualZero)
                calculoDeJurosJS()
                break
            if n < 0:
                print(tempoMaiorIgualZero)
                calculoDeJurosJS()
                break
            if i < 0:
                print(taxaMaiorIgualZero)
                calculoDeJurosJS()
                break

            J = calcularJuros(c, i, n, opcao4, M)
            J = round(J, 4)

            print(f"Juros = {J}")
        elif opcao4 == 8:
            print()
            c = float(input(capitalInserido))
            M = float(input(montanteInserido))
            i, n = 1, 1
            
            if c < 0:
                print(capitalMaiorIgualZero)
                calculoDeJurosJS()
                break
            if M < 0:
                print(montanteMaiorIgualZero)
                calculoDeJurosJS()
                break

            J = calcularJuros(c, i, n, opcao4, M)
            J = round(J, 4)

            print(f"Juros = {J}")
        else:
            print(opcaoInvalida)
            calculoDeJurosJS()
            break 
  