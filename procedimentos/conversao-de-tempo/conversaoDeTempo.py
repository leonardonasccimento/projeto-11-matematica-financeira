from mensagens import *

from converterTempo import converterTempo
from imprimirPalavraUnidadeEmSingularOuPlural import (
    imprimirPalavraUnidadeEmSingularOuPlural,
)
from verificarNumeroInteiro import verificarNumeroInteiro
from imprimirPalavraMesEmSingularOuPlural import imprimirPalavraMesEmSingularOuPlural


def conversaoDeTempo():
  while True:
    print(MensagemPeriodoDeTempo2)
    print()
    
    n1 = float(input(tempoInserido))
    p1 = float(input(f"Digite o período do tempo a ser convertido: "))
    p2 = float(input(f"Digite o período ao qual o tempo será convertido: "))

    p1Int = verificarNumeroInteiro(p1)
    p2Int = verificarNumeroInteiro(p2)

    if n1 < 0:
        print(tempoMaiorIgualZero)
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

    n2 = converterTempo(n1, p1, p2)
    n2 = round(n2, 4)

    mensagemMes = imprimirPalavraMesEmSingularOuPlural(p2)
    mensagemUnidade=imprimirPalavraUnidadeEmSingularOuPlural(n2)

    print(f"Tempo = {n2} ({mensagemUnidade} de tempo com período de ({p2} {mensagemMes}))")
    break
