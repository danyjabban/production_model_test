from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import get_keywords

app = FastAPI()

class TextIn(BaseModel):
    text1:str
    text2:str

class PredictionOut(BaseModel):
    keywords:list


@app.get("/")
def home():
    return {"health check":"OK"}

@app.post("/predict", response_model=PredictionOut)
def predict(payload:TextIn):
    keywords = get_keywords(payload.text1, payload.text2)
    return {"keywords":keywords}
