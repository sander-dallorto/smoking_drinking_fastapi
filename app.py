# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:08:01 2024

@author: sande
"""

# 1. Importando libs
import uvicorn
from fastapi import FastAPI
from HealthDatas import HealthData
import numpy as np
import pickle
import pandas as pd
import nest_asyncio
# 2. Criando o objeto app
app = FastAPI()
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)
nest_asyncio.apply()


# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To Krish Youtube Channel': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_healthdata(data: HealthData):
    # Convertendo os dados para dicionário
    data = data.dict()
    
    # Extraindo os dados relevantes
    sex = data['sex']
    age = data['age']
    height = data['height']
    weight = data['weight']
    waistline = data['waistline']
    sight_left = data['sight_left']
    sight_right = data['sight_right']
    hear_left = data['hear_left']
    hear_right = data['hear_right']
    SBP = data['SBP']
    DBP = data['DBP']
    BLDS = data['BLDS']
    tot_chole = data['tot_chole']
    HDL_chole = data['HDL_chole']
    LDL_chole = data['LDL_chole']
    triglyceride = data['triglyceride']
    hemoglobin = data['hemoglobin']
    urine_protein = data['urine_protein']
    serum_creatinine = data['serum_creatinine']
    SGOT_AST = data['SGOT_AST']
    SGOT_ALT = data['SGOT_ALT']
    gamma_GTP = data['gamma_GTP']
    SMK_stat_type_cd = data['SMK_stat_type_cd']
    DRK_YN = 1 if data['DRK_YN'] == 'Y' else 0  # Convertendo DRK_YN para 1 ou 0
    age_group_encoded = data['age_group_encoded']
    bmi = data['bmi']
    BP_ratio = data['BP_ratio']
    HDL_ratio = data['HDL_ratio']
    LDL_ratio = data['LDL_ratio']
    High_Blood_Pressure = data['High_Blood_Pressure']
    High_Total_Cholesterol = data['High_Total_Cholesterol']
    High_LDL_Cholesterol = data['High_LDL_Cholesterol']
    print("Hello!")
    # Fazendo a previsão
    prediction = classifier.predict([[age, height, weight, waistline, sight_left, sight_right,
                                      hear_left, hear_right, SBP, DBP, BLDS, tot_chole,
                                      HDL_chole, LDL_chole, triglyceride, hemoglobin,
                                      urine_protein, serum_creatinine, SGOT_AST, SGOT_ALT,
                                      gamma_GTP, SMK_stat_type_cd, DRK_YN]])
    
    # Interpretando a previsão
    if prediction[0] > 0.5:
        result = "Risk of Health Issues"
    else:
        result = "Healthy"

    return {
        'prediction': prediction
    }
# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload
