from fastapi import FastAPI
from pydantic import BaseModel
from amka_service import lookup_amka

app = FastAPI()

class AMKARequest(BaseModel):
    amka: str

@app.post("/amka/lookup")
async def amka_lookup(req: AMKARequest):
    result = await lookup_amka(req.amka)
    return result

@app.get("/health")
async def health():
    return {"status": "ok"}
