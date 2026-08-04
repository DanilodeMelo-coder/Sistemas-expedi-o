from fastapi import FastAPI
from app.routers.motoboys import router as motoboys_router



from app import models  # dispara o __init__.py, registra as 3 classes


app = FastAPI()

app.include_router(motoboys_router)



@app.get("/")
def olamundo():
    return {"message": "Olá Mundo!"}