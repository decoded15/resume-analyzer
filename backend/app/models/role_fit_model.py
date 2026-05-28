from pydantic import BaseModel
from typing import List


class RoleFitAnalysis(BaseModel):
    role_fit_score: int
    matching_skills: List[str]
    missing_skills: List[str]
    role_fit_summary: str
    improvement_recommendations: List[str]