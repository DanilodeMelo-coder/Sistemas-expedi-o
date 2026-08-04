from pydantic import BaseModel



class MotoboySchema_request(BaseModel):
    nome: str
    ativo: bool
    disponivel: bool


class MotoboySchema_response(BaseModel):
    id: str
    nome: str
    ativo: bool
    disponivel: bool

    class Config:
        from_attributes = True