# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:10:50 2024

@author: sande
"""

from pydantic import BaseModel
from pydantic import BaseModel, confloat, conint
from typing import Optional, Literal

class HealthData(BaseModel):
    sex: Optional[confloat(ge=0, le=1)]  
    age: Optional[float]
    height: Optional[float]
    weight: Optional[float]
    waistline: Optional[float]
    sight_left: Optional[float]
    sight_right: Optional[float]
    hear_left: Optional[float]
    hear_right: Optional[float]
    SBP: Optional[float]  # Systolic Blood Pressure
    DBP: Optional[float]  # Diastolic Blood Pressure
    BLDS: Optional[float]  # Blood Sugar
    tot_chole: Optional[float]  # Total Cholesterol
    HDL_chole: Optional[float]  # HDL Cholesterol
    LDL_chole: Optional[float]  # LDL Cholesterol
    triglyceride: Optional[float]
    hemoglobin: Optional[float]
    urine_protein: Optional[float]
    serum_creatinine: Optional[float]
    SGOT_AST: Optional[float]  # AST (Aspartate Aminotransferase)
    SGOT_ALT: Optional[float]  # ALT (Alanine Aminotransferase)
    gamma_GTP: Optional[float]
    SMK_stat_type_cd: Optional[float]  # Smoking Status
    DRK_YN: Optional[Literal['Y', 'N']]  # Drinking (Yes/No)
    age_group: Optional[Literal['0-18', '19-35', '36-50', '51-65', '65+']] 
    bmi: Optional[float]  # Body Mass Index
    BP_ratio: Optional[float]  # Blood Pressure ratio
    HDL_ratio: Optional[float]  # HDL Cholesterol ratio
    LDL_ratio: Optional[float]  # LDL Cholesterol ratio
    High_Blood_Pressure: Optional[float]
    High_Total_Cholesterol: Optional[float]
    High_LDL_Cholesterol: Optional[float]
    age_group_encoded: Optional[conint(ge=0)] 

    class Config:
        # Exemplo para realizar predição
        schema_extra = {
            "example": {
                "sex": 1.0,
                "age": 45.0,
                "height": 170.0,
                "weight": 75.0,
                "waistline": 90.0,
                "sight_left": 1.0,
                "sight_right": 1.0,
                "hear_left": 0.5,
                "hear_right": 0.5,
                "SBP": 120.0,
                "DBP": 80.0,
                "BLDS": 90.0,
                "tot_chole": 200.0,
                "HDL_chole": 50.0,
                "LDL_chole": 100.0,
                "triglyceride": 150.0,
                "hemoglobin": 13.5,
                "urine_protein": 0.0,
                "serum_creatinine": 1.0,
                "SGOT_AST": 30.0,
                "SGOT_ALT": 25.0,
                "gamma_GTP": 20.0,}}

