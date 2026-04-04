from fastapi import FastAPI, HTTPException

from src.predict import prever_pd
from src.schemas import ClienteInput, PredicaoOutput


app = FastAPI(
    title="API de Predição de PD",
    description="Serviço de inferência para modelo de regressão logística de probabilidade de default.",
    version="1.0.0",
)


@app.get("/")
def home():
    return {"status": "ok"}

@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict", response_model=PredicaoOutput)
def predict(cliente: ClienteInput):
    try:
        prob = prever_pd(cliente.model_dump())
        return PredicaoOutput(probabilidade_inadimplencia=prob)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")