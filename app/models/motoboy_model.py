from core.database import Base
from sqlalchemy import String, Boolean, Integer, Column
from sqlalchemy.orm import relationship
import uuid


class Motoboy(Base):
    __tablename__ = "motoboys"


    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    nome = Column(String, nullable=False)
    ativo = Column(Boolean, nullable=True)
    disponivel = Column(Boolean, nullable=True)

    saidas = relationship("Saida", back_populates="motoboy")