from core.database import Base
from sqlalchemy import DateTime, Float, Integer, String, Column, Enum, ForeignKey
from sqlalchemy.orm import relationship
import uuid
from models.enum_status_pedido import Status_PedidoE


class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    cliente = Column(String, nullable= False)
    endereco = Column(String, nullable=False)
    numero = Column(String, nullable=False)
    complemento = Column(String, nullable=True)
    bairro= Column(String, nullable=False)
    cidade = Column(String, nullable=True)
    cep = Column(String, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    horario_limite = Column(DateTime) 
    forma_pagamento = Column(String, nullable=False)
    observacao = Column(String, nullable=True)
    valor_total = Column(Float, nullable=False)
    status = Column(Enum(Status_PedidoE), default=Status_PedidoE.FILA)
    saida_id = Column(String, ForeignKey("saidas.id"), nullable=True)
    ordem_na_saida = Column(Integer, nullable=True)
    saida = relationship("Saida", back_populates="pedidos")