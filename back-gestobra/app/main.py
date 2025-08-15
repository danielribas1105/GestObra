from fastapi import FastAPI
from . import models, database, routes, auth
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

""" pip install -r requirements.txt """
""" uvicorn app.main:app --reload """

app = FastAPI(title="GestObra API", version="1.0.0")

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(routes.router)
app.include_router(auth.router)

# Libera acesso do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # endereço do frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "API GestObra está rodando 🚀"}

@app.get("/status")
def get_status():
    return {
        "status": "online",
        "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }
