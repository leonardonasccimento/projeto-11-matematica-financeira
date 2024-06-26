from mensagens import *

from calcularTaxaProporcional import calcularTaxaProporcional
from verificarNumeroInteiro import verificarNumeroInteiro
from imprimirPalavraMesEmSingularOuPlural import imprimirPalavraMesEmSingularOuPlural


def taxaProporcional():
  while True:
    print(
        mensagemTaxaMenorMaior
    )
    print(MensagemPeriodoDeTempo)
    i1 = float(
        input(taxaASerConvertidaInserida)
    )
    p1 = float(input(periodo1DaTaxaInserido))
    p2 = float(input(periodo2DaTaxaInserido))

    p1Int = verificarNumeroInteiro(p1)
    p2Int = verificarNumeroInteiro(p2)

    if i1 < 0:
        print(taxaMaiorIgualZero)
        break
    if not p1Int:
        print(periodoInteiro)
        break
    if p1 <= 0:
        print(periodoMaiorQueZero)
        break
    if not p2Int:
        print(periodoInteiro)
        break
    if p2 <= 0:
        print(periodoMaiorQueZero)
        break

    i2 = calcularTaxaProporcional(i1, p1, p2)

    if not i2:
        print(
            mensagemPeriodosIncompativeis
        )
        break

    i2 *= 100
    i2 = round(i2, 4)

    mensagemMes = imprimirPalavraMesEmSingularOuPlural(p2)

    print(f"Taxa convertida = {i2}% (a cada {p2} {mensagemMes})")
    break
