from app.schemas.Schema_motoboy import MotoboySchema_request;
from app.models.motoboy_model import Motoboy
from sqlalchemy.orm import Session



#criação de um novo motoboy
def criar_motoboy(db: Session, dados: MotoboySchema_request):

    motoboy_novo = Motoboy(
        nome=dados.nome,
        ativo=dados.ativo,
        disponivel=dados.disponivel
    )

    db.add(motoboy_novo)
    db.commit()
    db.refresh(motoboy_novo)

    return motoboy_novo




#listar motoboys
def listar_motoboys_service(db: Session):
    motoboys = db.query(Motoboy).all()
    return motoboys


#deletar motoboy
def deletar_motoboy_service(db: Session, motoboy_id: str):

    motoboy = db.query(Motoboy).filter(Motoboy.id == motoboy_id).first()
    if not motoboy:
        return {"status": "erro",
        "mensagem": "Motoboy não encontrado",
        "data": None}

    db.delete(motoboy)
    db.commit()
    
    return motoboy