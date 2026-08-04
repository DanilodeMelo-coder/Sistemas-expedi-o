from pydantic import BaseModel
from datetime import datetime

from app.models.enum_status_pedido import Status_PedidoE

class PedidoSchema_Request(BaseModel):
    cliente: str
    endereco: str
    numero: str
    complemento: str | None = None
    bairro: str
    cidade: str | None = None
    cep: str | None = None
    horario_limite: datetime | None = None
    forma_pagamento: str
    observacao: str | None = None
    valor_total: float


class PedidoSchema_Response(BaseModel):
    id: str
    cliente: str
    endereco: str
    numero: str
    complemento: str | None = None
    bairro: str
    cidade: str | None = None
    cep: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    horario_limite: datetime | None = None
    forma_pagamento: str
    observacao: str | None = None
    valor_total: float
    status: Status_PedidoE
    saida_id: str | None = None
    ordem_na_saida: int | None = None

    class Config:
        from_attributes = True