from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.motoboy_service import criar_motoboy, listar_motoboys_service, deletar_motoboy_service
from app.schemas.Schema_motoboy import MotoboySchema_request, MotoboySchema_response
from core.database import get_session






router = APIRouter(
    prefix="/motoboys",
    tags=["Motoboys"]
)


@router.post("/", response_model=MotoboySchema_response)
def criar_motoboy_endpoint(dados: MotoboySchema_request, db: Session = Depends(get_session)):
    return criar_motoboy(db, dados)


@router.get("/", response_model=list[MotoboySchema_response])
def listar_motoboys(db: Session = Depends(get_session)):
    return listar_motoboys_service(db)


@router.delete("/{motoboy_id}", response_model=MotoboySchema_response)
def deletar_motoboy(motoboy_id: str, db: Session = Depends(get_session)):
    motoboy = deletar_motoboy_service(db, motoboy_id)
    
    return motoboy