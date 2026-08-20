# # from fastapi import FastAPI
# # import joblib

# # app = FastAPI()

# # model = joblib.load("food_delivery_time_model.pkl")


# # @app.get("/")
# # def home():
# #     return {
# #         "message": "Food Delivery Time Prediction API is running"
# #     }

# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel, Field
# import pandas as pd
# import joblib


# # --------------------------------------------------
# # 1. Load trained ML pipeline
# # --------------------------------------------------

# MODEL_PATH = "food_delivery_time_model.pkl"

# try:
#     model = joblib.load(MODEL_PATH)
#     print("Model loaded successfully!")

# except Exception as e:
#     raise RuntimeError(f"Model loading failed: {e}")


# # --------------------------------------------------
# # 2. Create FastAPI application
# # --------------------------------------------------

# app = FastAPI(
#     title="Food Delivery Time Prediction API",
#     description="API for predicting food delivery time using Machine Learning.",
#     version="1.0.0"
# )


# # --------------------------------------------------
# # 3. Input Schema
# # --------------------------------------------------

# class DeliveryInput(BaseModel):

#     Order_Hour: int = Field(..., ge=0, le=23)

#     Day_of_Week: str

#     Is_Weekend: int = Field(..., ge=0, le=1)

#     Is_Festival: int = Field(..., ge=0, le=1)

#     Weather: str
    
#     Pickup_Zone: str

#     Dropoff_Zone: str

#     Vehicle_Type: str

#     Rider_Experience_Years: float = Field(..., ge=0)

#     Rider_Rating: float = Field(..., ge=0)

#     Restaurant_Rating: float = Field(..., ge=0)

#     Cuisine_Type: str

#     Order_Items: int = Field(..., ge=1)

#     Restaurant_Load: str

#     Preparation_Time_Min: float = Field(..., ge=0)

#     Road_Distance_km: float = Field(..., ge=0)

#     Delivery_Distance_Category: str

#     Traffic_Level: str

#     Number_of_Signals: int = Field(..., ge=0)

#     Average_Speed_kmph: float = Field(..., gt=0)

#     Delivery_Priority: str

#     Order_Year: int

#     Order_Month: int = Field(..., ge=1, le=12)

#     Order_Day: int = Field(..., ge=1, le=31)


# # --------------------------------------------------
# # 4. Root Endpoint
# # --------------------------------------------------

# @app.get("/")
# def home():

#     return {
#         "message": "Food Delivery Time Prediction API",
#         "status": "running",
#         "docs": "/docs"
#     }


# # --------------------------------------------------
# # 5. Health Check
# # --------------------------------------------------

# @app.get("/health")
# def health_check():

#     return {
#         "status": "healthy",
#         "model_loaded": True
#     }


# # --------------------------------------------------
# # 6. Prediction Endpoint
# # --------------------------------------------------

# @app.post("/predict")
# def predict_delivery_time(data: DeliveryInput):

#     try:

#         # Convert Pydantic object into dictionary
#         input_data = data.model_dump()

#         # Convert dictionary into DataFrame
#         input_df = pd.DataFrame([input_data])

#         # Make prediction
#         prediction = model.predict(input_df)[0]

#         # Return prediction
#         return {
#             "predicted_delivery_time_minutes": round(
#                 float(prediction),
#                 2
#             )
#         }

#     except Exception as e:

#         raise HTTPException(
#             status_code=500,
#             detail=f"Prediction failed: {str(e)}"
#         )












# ``````````````````````````````````````````````````````````````````````````````````````````````````````````````
# from fastapi import FastAPI, HTTPException
# from fastapi.staticfiles import StaticFiles
# from fastapi.responses import FileResponse
# from pydantic import BaseModel, Field
# import pandas as pd
# import joblib
# import os


# # --------------------------------------------------
# # 1. Load trained ML pipeline
# # --------------------------------------------------

# MODEL_PATH = "food_delivery_time_model.pkl"

# try:
#     model = joblib.load(MODEL_PATH)
#     print("Model loaded successfully!")

# except Exception as e:
#     raise RuntimeError(f"Model loading failed: {e}")


# # --------------------------------------------------
# # 2. Create FastAPI application
# # --------------------------------------------------

# app = FastAPI(
#     title="Food Delivery Time Prediction API",
#     description="ML-powered food delivery time prediction API.",
#     version="1.0.0"
# )


# # --------------------------------------------------
# # 3. Serve static files
# # --------------------------------------------------

# app.mount(
#     "/static",
#     StaticFiles(directory="static"),
#     name="static"
# )


# # --------------------------------------------------
# # 4. Pydantic Input Schema
# # --------------------------------------------------

# class DeliveryInput(BaseModel):

#     Order_Hour: int = Field(..., ge=0, le=23)

#     Day_of_Week: str

#     Is_Weekend: int = Field(..., ge=0, le=1)

#     Is_Festival: int = Field(..., ge=0, le=1)

#     Weather: str

#     Pickup_Zone: str

#     Dropoff_Zone: str

#     Vehicle_Type: str

#     Rider_Experience_Years: float = Field(..., ge=0)

#     Rider_Rating: float = Field(..., ge=0, le=5)

#     Restaurant_Rating: float = Field(..., ge=0, le=5)

#     Cuisine_Type: str

#     Order_Items: int = Field(..., ge=1)

#     Restaurant_Load: str

#     Preparation_Time_Min: float = Field(..., ge=0)

#     Road_Distance_km: float = Field(..., ge=0)

#     Delivery_Distance_Category: str

#     Traffic_Level: str

#     Number_of_Signals: int = Field(..., ge=0)

#     Average_Speed_kmph: float = Field(..., gt=0)

#     Delivery_Priority: str

#     Order_Year: int

#     Order_Month: int = Field(..., ge=1, le=12)

#     Order_Day: int = Field(..., ge=1, le=31)


# # --------------------------------------------------
# # 5. Frontend
# # --------------------------------------------------

# @app.get("/", include_in_schema=False)
# def home():
#     return FileResponse("templates/index.html")


# # --------------------------------------------------
# # 6. Health Check
# # --------------------------------------------------

# @app.get("/health")
# def health_check():

#     return {
#         "status": "healthy",
#         "model_loaded": True
#     }


# # --------------------------------------------------
# # 7. Prediction Endpoint
# # --------------------------------------------------

# @app.post("/predict")
# def predict_delivery_time(data: DeliveryInput):

#     try:

#         # Convert Pydantic object into dictionary
#         input_data = data.model_dump()

#         # Convert input into DataFrame
#         input_df = pd.DataFrame([input_data])

#         # Make prediction
#         prediction = model.predict(input_df)[0]

#         return {
#             "predicted_delivery_time_minutes": round(
#                 float(prediction),
#                 2
#             )
#         }

#     except Exception as e:

#         raise HTTPException(
#             status_code=500,
#             detail=f"Prediction failed: {str(e)}"
#         )
# ````````````````````````````````````````````````````````````````````````````````````````````````````````````
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

import pandas as pd
import joblib


# ==================================================
# 1. Project Paths
# ==================================================

# Current project directory
BASE_DIR = Path(__file__).resolve().parent

# Frontend directories
STATIC_DIR = BASE_DIR / "static"
TEMPLATES_DIR = BASE_DIR / "templates"

# ML model path
MODEL_PATH = BASE_DIR / "food_delivery_time_model.pkl"


# ==================================================
# 2. Load Trained ML Pipeline
# ==================================================

try:

    model = joblib.load(MODEL_PATH)

    print("Model loaded successfully!")

except Exception as e:

    raise RuntimeError(
        f"Model loading failed: {e}"
    )


# ==================================================
# 3. Create FastAPI Application
# ==================================================

app = FastAPI(
    title="Food Delivery Time Prediction API",
    description="ML-powered food delivery time prediction API.",
    version="1.0.0"
)


# ==================================================
# 4. Serve Static Frontend Files
# ==================================================

app.mount(
    "/static",
    StaticFiles(
        directory=str(STATIC_DIR)
    ),
    name="static"
)


# ==================================================
# 5. Pydantic Input Schema
# ==================================================

class DeliveryInput(BaseModel):

    Order_Hour: int = Field(
        ...,
        ge=0,
        le=23
    )

    Day_of_Week: str

    Is_Weekend: int = Field(
        ...,
        ge=0,
        le=1
    )

    Is_Festival: int = Field(
        ...,
        ge=0,
        le=1
    )

    Weather: str

    Pickup_Zone: str

    Dropoff_Zone: str

    Vehicle_Type: str

    Rider_Experience_Years: float = Field(
        ...,
        ge=0
    )

    Rider_Rating: float = Field(
        ...,
        ge=0,
        le=5
    )

    Restaurant_Rating: float = Field(
        ...,
        ge=0,
        le=5
    )

    Cuisine_Type: str

    Order_Items: int = Field(
        ...,
        ge=1
    )

    Restaurant_Load: str

    Preparation_Time_Min: float = Field(
        ...,
        ge=0
    )

    Road_Distance_km: float = Field(
        ...,
        ge=0
    )

    Delivery_Distance_Category: str

    Traffic_Level: str

    Number_of_Signals: int = Field(
        ...,
        ge=0
    )

    Average_Speed_kmph: float = Field(
        ...,
        gt=0
    )

    Delivery_Priority: str

    Order_Year: int

    Order_Month: int = Field(
        ...,
        ge=1,
        le=12
    )

    Order_Day: int = Field(
        ...,
        ge=1,
        le=31
    )


# ==================================================
# 6. Frontend Home Page
# ==================================================

@app.get(
    "/",
    include_in_schema=False
)
def home():

    return FileResponse(
        str(TEMPLATES_DIR / "index.html")
    )


# ==================================================
# 7. Health Check
# ==================================================

@app.get("/health")
def health_check():

    return {
        "status": "healthy",
        "model_loaded": True
    }


# ==================================================
# 8. Prediction Endpoint
# ==================================================

@app.post("/predict")
def predict_delivery_time(
    data: DeliveryInput
):

    try:

        # --------------------------------------------------
        # Convert Pydantic object into dictionary
        # --------------------------------------------------

        input_data = data.model_dump()


        # --------------------------------------------------
        # Convert dictionary into DataFrame
        # --------------------------------------------------

        input_df = pd.DataFrame(
            [input_data]
        )


        # --------------------------------------------------
        # Make prediction using trained ML pipeline
        # --------------------------------------------------

        prediction = model.predict(
            input_df
        )[0]


        # --------------------------------------------------
        # Return prediction
        # --------------------------------------------------

        return {
            "predicted_delivery_time_minutes": round(
                float(prediction),
                2
            )
        }


    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )