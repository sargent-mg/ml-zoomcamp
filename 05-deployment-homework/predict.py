import pickle
import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Literal
from typing import Dict, Any

# Request
class Record(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float


# Response
class PredictResponse(BaseModel):
    probability: float = Field(..., gt=0, lt=1)


app = FastAPI(title="Score Prediction")


with open('pipeline_v1.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)


def predict_single(record):
    result = pipeline.predict_proba(record)[0, 1]
    return float(result)


@app.post("/predict")
def predict(record: Record) -> PredictResponse:
    prob = predict_single(record.model_dump())

    return PredictResponse(
        probability=prob
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)