def imprimirPalavraMesEmSingularOuPlural(periodo):
    mensagemMes = "meses"
    if periodo == 1:
        mensagemMes = "mês"
        return mensagemMes
    elif periodo > 1:
        mensagemMes = "meses"
        return mensagemMes
    else:
        mensagemMes = ""
        return mensagemMes
