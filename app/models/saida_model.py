from core.database import Base
from sqlalchemy import String, Column, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from app.models.enum_status_saida import Status_SaidaE
import uuid
from datetime import datetime

class Saida(Base):
    __tablename__ = "saidas"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    motoboy_id = Column(String, ForeignKey("motoboys.id"), nullable=False)
    status_saida = Column(Enum(Status_SaidaE), default=Status_SaidaE.SUGERIDA)
    horario_criacao = Column(DateTime, default=datetime.utcnow) 
    horario_confirmacao = Column(DateTime)
    horario_finalizacao = Column(DateTime)

    motoboy = relationship("Motoboy", back_populates="saidas")
    pedidos = relationship("Pedido", back_populates="saida", order_by="Pedido.ordem_na_saida")