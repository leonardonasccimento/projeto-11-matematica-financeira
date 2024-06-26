def imprimirPalavraUnidadeEmSingularOuPlural(tempo):
        if tempo < 2:
            mensagemUnidade = "unidade"
            return mensagemUnidade
        if tempo >= 2:
            mensagemUnidade = "unidades"
            return mensagemUnidade