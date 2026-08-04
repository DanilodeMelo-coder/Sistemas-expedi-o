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


