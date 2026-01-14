from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import joblib

app = FastAPI(title="House Price Prediction")

templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("model_pipeline.pkl")

@app.get("/", response_class=HTMLResponse)
def ui(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request}
    )

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return {"prediction": float(prediction)}








# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# import pandas as pd
# import joblib

# # Create FastAPI app
# app = FastAPI(title="House Price Prediction API")

# # Allow frontend to call backend (VERY IMPORTANT)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],   # In production, restrict this
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Load trained model
# model = joblib.load("model_pipeline.pkl")

# @app.get("/")
# def health_check():
#     return {"status": "API is running"}

# @app.post("/predict")
# def predict_price(data: dict):
#     """
#     Expected JSON:
#     {
#         "YearBuilt": 2005,
#         "TotalBsmtSF": 850,
#         "TotRmsAbvGrd": 6,
#         "GarageArea": 460,
#         "PoolArea": 0,
#         "Neighborhood": "NAmes",
#         "Heating": "GasA",
#         "KitchenQual": "Gd"
#     }
#     """

#     # Convert input JSON to DataFrame
#     df = pd.DataFrame([data])

#     # Predict
#     prediction = model.predict(df)[0]

#     return {
#         "prediction": float(prediction)
#     }
