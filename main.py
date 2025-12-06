# main.py
from fastapi import FastAPI, HTTPException, Query
from finance_calculator import FinanceCalculator
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="API - Finanças Pessoais")

@app.get("/juros_simples")
def juros_simples(capital: float = Query(...), taxa: float = Query(...), tempo: int = Query(...)):
    try:
        return FinanceCalculator.juros_simples(capital, taxa, tempo)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/juros_compostos")
def juros_compostos(capital: float = Query(...), taxa: float = Query(...), tempo: int = Query(...), periodos_por_ano: int = Query(1)):
    try:
        return FinanceCalculator.juros_compostos(capital, taxa, tempo, periodos_por_ano)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/valor_futuro")
def valor_futuro(valor_presente: float = Query(...), taxa: float = Query(...), n_periodos: int = Query(...), contribuicao_periodica: Optional[float] = Query(0.0)):
    try:
        return FinanceCalculator.valor_futuro(valor_presente, taxa, n_periodos, contribuicao_periodica)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/valor_presente")
def valor_presente(valor_futuro: float = Query(...), taxa: float = Query(...), n_periodos: int = Query(...)):
    try:
        return FinanceCalculator.valor_presente(valor_futuro, taxa, n_periodos)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
