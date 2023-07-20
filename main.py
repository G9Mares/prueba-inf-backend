from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import login

#python -m uvicorn main:app --reload --port 4000 

app = FastAPI()
origins = ["*"] 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los encabezados en las solicitudes
)

app.include_router(login.router)

@app.get("/")
async def raiz():
    return{"Hola mundo"}