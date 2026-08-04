from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.pedidos_service import criar_pedido_service, listar_pedidos_service
from app.schemas.schema_pedido import PedidoSchema_Request, PedidoSchema_Response
from core.database import get_session


router = APIRouter(
    prefix="/pedidos",
    tags=["Pedidos"]
)


@router.post("/", response_model=PedidoSchema_Response)
def criar_pedido(dados: PedidoSchema_Request, db: Session = Depends(get_session)):
    return criar_pedido_service(db, dados)  

@router.get("/", response_model=list[PedidoSchema_Response])
def listar_pedidos(db: Session = Depends(get_session)):
    return listar_pedidos_service(db)