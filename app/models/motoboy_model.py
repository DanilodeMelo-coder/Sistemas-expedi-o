from core.database import Base
from sqlalchemy import String, Boolean, Column
from sqlalchemy.orm import relationship
import uuid


class Motoboy(Base):
    __tablename__ = "motoboys"


    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    nome = Column(String, nullable=False)
    ativo = Column(Boolean, nullable=False)
    disponivel = Column(Boolean, nullable=False)

    saidas = relationship("Saida", back_populates="motoboy")