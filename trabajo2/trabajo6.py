from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load
import numpy as np

class Car(BaseModel):
    modelo: int
    año: int
    precio: float
    kilometraje: float
    impuesto: float
    mpg: float
    

app = FastAPI()

@app.on_event("startup")
def load_model():
    global model
    model = load('modelo_1_precios_toyotas.pkl')

@app.post("/predict")
def predict_price(car: Car):
    # Convert the car features to a numpy array and make a prediction
    data = np.array([list(car.dict().values())])
    prediction = model.predict(data)
    return {"predicted_price": prediction[0]}