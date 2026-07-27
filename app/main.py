from fastapi import FastAPI






app = FastAPI()



@app.get("/")
def olamundo():
    return {"message": "Olá Mundo!"}