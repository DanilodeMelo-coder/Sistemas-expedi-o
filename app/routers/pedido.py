from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.pedidos_service import atualizar_pedido_service, cancelar_pedido_service, criar_pedido_service, listar_pedidos_service
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

@router.put("/{pedido_id}", response_model=PedidoSchema_Response)
def atualizar_pedido(pedido_id: str, dados: PedidoSchema_Request, db: Session = Depends(get_session)):
    return atualizar_pedido_service(db, pedido_id, dados)

@router.get("/{pedido_id}/cancelar", response_model=PedidoSchema_Response)
def cancelar_pedido(pedido_id: str, db: Session = Depends(get_session)):
    return cancelar_pedido_service(db, pedido_id)