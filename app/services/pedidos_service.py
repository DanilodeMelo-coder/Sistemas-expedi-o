from fastapi import HTTPException

from app.models.enum_status_pedido import Status_PedidoE
from app.schemas.schema_pedido import PedidoSchema_Request
from app.models.pedido_model import Pedido
from sqlalchemy.orm import Session 


#criar pedido
def criar_pedido_service(db: Session, dados: PedidoSchema_Request): 

    pedido_novo = Pedido(
        cliente=dados.cliente,
        endereco=dados.endereco,
        numero=dados.numero,
        complemento=dados.complemento,
        bairro=dados.bairro,
        cidade=dados.cidade,
        cep=dados.cep,
        horario_limite=dados.horario_limite,
        forma_pagamento=dados.forma_pagamento,
        observacao=dados.observacao,
        valor_total=dados.valor_total
    )

    db.add(pedido_novo)
    db.commit()
    db.refresh(pedido_novo)

    return pedido_novo


#listar pedidos
def listar_pedidos_service(db: Session):
    pedidos = db.query(Pedido).all()
    return pedidos



#atualizar pedido
def atualizar_pedido_service(db: Session, pedido_id: str, dados: PedidoSchema_Request):
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")

    pedido.cliente = dados.cliente
    pedido.endereco = dados.endereco
    pedido.numero = dados.numero
    pedido.complemento = dados.complemento
    pedido.bairro = dados.bairro
    pedido.cidade = dados.cidade
    pedido.cep = dados.cep
    pedido.horario_limite = dados.horario_limite
    pedido.forma_pagamento = dados.forma_pagamento
    pedido.observacao = dados.observacao
    pedido.valor_total = dados.valor_total

    db.commit()
    db.refresh(pedido)

    return pedido


def cancelar_pedido_service(db: Session, pedido_id: str):
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")

    pedido.status = Status_PedidoE.CANCELADO
    db.commit()
    db.refresh(pedido)

    return pedido