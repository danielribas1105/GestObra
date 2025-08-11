from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI(title="GestObra API", version="1.0.0")

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
