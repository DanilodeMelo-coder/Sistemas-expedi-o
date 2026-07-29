from enum import Enum



class Status_PedidoE(str, Enum):
    FILA = "fila"
    EM_SAIDA = "em saida"
    ENTREGUE = "entregue"
    LOCALIZACAO_PENDENTE = "localizacao pendente"
    CANCELADO = "cancelado"