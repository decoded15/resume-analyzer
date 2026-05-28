from pydantic import BaseModel
from typing import List

class ScoreBreakdown(BaseModel):
    formatting: int
    skills: int
    keyword_optimization: int
    impact: int
    readability: int

class ATSAnalysis(BaseModel):
    overall_score: int
    score_breakdown: ScoreBreakdown
    strengths: List[str]
    weaknesses: List[str]
    improvement_suggestions: List[str]