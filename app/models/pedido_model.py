from core.database import Base
from sqlalchemy import String, Boolean, Column
from sqlalchemy.orm import relationship
import uuid


class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    cliente = Column(String, nullable= True)
    endereço = Column(String, nullable=True)
    numero = Column(String, nullable=True)
    complemento = Column(String, nullable=False)
    bairro= Column(String, nullable=False)
    cidade = Column(String, nullable=True)