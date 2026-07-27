from enum import Enum



class Status_PedidoE(str, Enum):
    FILA = "fila"
    EM_SAIDA = "em saida"
    ENTREGUE = "entregue"
    LOCALIZACAO_PENDENTE = "localizacao pendente"
    CANCELADO = "cancelado"


class Status_SaidaE(str, Enum):
    SUGERIDA = "sugerida"
    CONFIRMADA = "confirmada"
    EM_ANDAMENTO = "em andamento"
    FINALIZADA = "finalizada"