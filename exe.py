from sys import path

path.insert(1, "./metodos/metodos-genericos/calcular-juros")
path.insert(1, "./metodos/metodos-grandezas-JS/calcular-capital-JS")
path.insert(1, "./metodos/metodos-grandezas-JS/calcular-taxa-JS")
path.insert(1, "./metodos/metodos-grandezas-JS/calcular-tempo-JS")
path.insert(1, "./metodos/metodos-grandezas-JS/calcular-montante-JS")

path.insert(1, "./metodos/metodos-grandezas-JC/calcular-capital-JC")
path.insert(1, "./metodos/metodos-grandezas-JC/calcular-montante-JC")
path.insert(1, "./metodos/metodos-grandezas-JC/calcular-taxa-JC")
path.insert(1, "./metodos/metodos-grandezas-JC/calcular-tempo-JC")

path.insert(1, "./metodos/metodos-grandezas-SAF/calcular-montante-SAF")
path.insert(1, "./metodos/metodos-grandezas-SAF/calcular-parcelas-SAF")
path.insert(1, "./metodos/metodos-grandezas-SAF/calcular-fator-de-amortizacao-SAF")

path.insert(1, "./metodos/metodos-genericos/calcular-taxa-proporcional")
path.insert(1, "./metodos/metodos-genericos/calcular-taxa-equivalente")
path.insert(1, "./metodos/metodos-genericos/converter-tempo")

path.insert(1, "./metodos/metodos-genericos/imprimir-palavra-mes-em-singular-ou-plural")
path.insert(1, "./metodos/metodos-genericos/imprimir-palavra-unidade-em-singular-ou-plural")
path.insert(1, "./metodos/metodos-genericos/verificar-numero-inteiro")

path.insert(1, "./procedimentos/calculo-de-grandezas-JS")
path.insert(1, "./procedimentos/calculo-de-grandezas-JC")
path.insert(1, "./procedimentos/conversao-de-tempo")
path.insert(1, "./procedimentos/taxa-proporcional")
path.insert(1, "./procedimentos/taxa-equivalente")
path.insert(1, "./procedimentos/calculo-de-grandezas-SAF")

path.insert(1, "./procedimentos/calculo-de-grandezas-JS/calculo-de-capital-JS")
path.insert(1, "./procedimentos/calculo-de-grandezas-JS/calculo-de-taxa-JS")
path.insert(1, "./procedimentos/calculo-de-grandezas-JS/calculo-de-tempo-JS")
path.insert(1, "./procedimentos/calculo-de-grandezas-JS/calculo-de-juros-JS")

path.insert(1, "./procedimentos/calculo-de-grandezas-JC/calculo-de-capital-JC")
path.insert(1, "./procedimentos/calculo-de-grandezas-JC/calculo-de-taxa-JC")
path.insert(1, "./procedimentos/calculo-de-grandezas-JC/calculo-de-tempo-JC")

path.insert(1, "./variaveis-mensagens")

from mensagens import *

from calculoDeGrandezasJS import calculoDeGrandezasJS
from calculoDeGrandezasJC import calculoDeGrandezasJC
from taxaProporcional import taxaProporcional
from taxaEquivalente import taxaEquivalente
from conversaoDeTempo import conversaoDeTempo
from calculoDeGrandezasSAF import calculoDeGrandezasSAF


while True:
    opcao = int(input(f"\nDigite:\n    (1) para cálculo de juros, capital, taxa, tempo ou montante (Juros simples)\n ou (2) para cálculo de taxas proporcionais (Juros simples)\n ou (3) para cálculo de juros, capital, taxa, tempo ou montante (juros compostos)\n ou (4) para cálculo de taxas equivalentes (juros compostos)\n ou (5) para conversão de tempo\n ou (6) para cálculo de montante, parcela ou fator de armotização (SAF)\n ou (0) para sair: "))
    if opcao==0:break
    
    if opcao == 1:
        calculoDeGrandezasJS()
    elif opcao == 2:
        taxaProporcional()
    elif opcao == 3:
        calculoDeGrandezasJC()
    elif opcao == 4:
        taxaEquivalente()
    elif opcao == 5:
        conversaoDeTempo()
    elif opcao == 6:
        print("\nSistema de amortização francês (SAF):\n - Parcelas iguais\n - Mesmo intervalo de tempo entre as parcelas\n - Taxa de juros compostos\n - Não existe pagamento de entrada")
        calculoDeGrandezasSAF()
    else:
        print(opcaoInvalida)
        


