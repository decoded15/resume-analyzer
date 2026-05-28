from pydantic import BaseModel
from typing import List, Optional


class Experience(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    dates: Optional[str] = None
    description: Optional[List[str]] = []


class Education(BaseModel):
    degree: Optional[str] = None
    institution: Optional[str] = None
    location: Optional[str] = None
    dates: Optional[str] = None


class ResumeData(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None

    skills: Optional[List[str]] = []

    experience: Optional[List[Experience]] = []

    education: Optional[List[Education]] = []

    projects: Optional[List[str]] = []

    certifications: Optional[List[str]] = []