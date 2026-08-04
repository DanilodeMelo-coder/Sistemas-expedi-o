from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.motoboy_service import criar_motoboy
from app.schemas.Schema_motoboy import MotoboySchema_request, MotoboySchema_response
from core.database import get_session






router = APIRouter(
    prefix="/motoboys",
    tags=["Motoboys"]
)


@router.post("/", response_model=MotoboySchema_response)
def criar_motoboy_endpoint(dados: MotoboySchema_request, db: Session = Depends(get_session)):

    motoboy_novo = criar_motoboy(db, dados)

    return motoboy_novo




