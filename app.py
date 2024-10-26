# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:08:01 2024

@author: sande
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel  
import numpy as np
import pickle
import pandas as pd
import nest_asyncio
from HealthDatas import HealthData

# 2. Create the app object
app = FastAPI()
pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)
nest_asyncio.apply()

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
@app.get('/{name}')
def get_name(name: str):
    return {'Bem Vindo ao FastAPI': f'{name}'}

# 5. Expose the prediction functionality
@app.post('/predict')
def predict_healthdata(data: HealthData):
    # Convertendo os dados para dicionário
    data_dict = data.dict()
    
    # Extracting relevant data
    features = [
        data_dict['sex'],
        data_dict['age_group'],
        data_dict['bmi'],
        data_dict['waistline'],
        data_dict['sight_left'],
        data_dict['sight_right'],
        data_dict['hear_left'],
        data_dict['hear_right'],
        data_dict['triglyceride'],
        data_dict['hemoglobin'],
        data_dict['urine_protein'],
        data_dict['serum_creatinine'],
        data_dict['sgot_ast'],
        data_dict['sgot_alt'],
        data_dict['gamma_gtp'],
        data_dict['smk_stat_type_cd'],
        data_dict['bp_ratio'],
        data_dict['hdl_ratio'],
        data_dict['ldl_ratio']
    ]
    
    print("Dados recebidos para predição:", data_dict)

    # Making the prediction
    prediction_proba = classifier.predict_proba([features])[0]

    # Interpretando a previsão
    if prediction_proba[1] > 0.5:  # Assuming the second index is for the risk class
        result = "Risco de Sáude"
    else:
        result = "Saudável"

    return {
        'prediction': prediction_proba[1],  # Probability of the health risk
        'result': result
    }

# 6. Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
