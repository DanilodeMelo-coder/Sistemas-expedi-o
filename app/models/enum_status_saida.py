from enum import Enum



class Status_SaidaE(str, Enum):
    SUGERIDA = "sugerida"
    CONFIRMADA = "confirmada"
    EM_ANDAMENTO = "em andamento"
    FINALIZADA = "finalizada"