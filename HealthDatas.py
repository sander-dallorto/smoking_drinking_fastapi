# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:10:50 2024

@author: sande
"""

from pydantic import BaseModel
from pydantic import BaseModel, confloat, conint
from typing import Optional, Literal

class HealthData(BaseModel):
    sex: int
    age_group: int
    bmi: float
    waistline: float
    sight_left: float
    sight_right: float
    hear_left: float
    hear_right: float
    triglyceride: float
    hemoglobin: float
    urine_protein: float
    serum_creatinine: float
    sgot_ast: float
    sgot_alt: float
    gamma_gtp: float
    smk_stat_type_cd: int
    bp_ratio: float
    hdl_ratio: float
    ldl_ratio: float

