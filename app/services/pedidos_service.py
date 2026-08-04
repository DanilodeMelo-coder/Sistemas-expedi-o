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


#listar motoboys
def listar_pedidos_service(db: Session):
    pedidos = db.query(Pedido).all()
    return pedidos