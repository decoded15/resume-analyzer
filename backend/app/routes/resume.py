from fastapi import APIRouter, UploadFile, File
import shutil
from pathlib import Path
from app.parsers.pdf_parser import extract_text_from_pdf
from app.utils.text_cleaner import clean_resume_text
from app.services.resume_service import extract_resume_data
from app.services.ats_service import analyze_ats_score

router = APIRouter()

UPLOAD_DIR = "uploads"

Path(UPLOAD_DIR).mkdir(exist_ok=True)


@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    extracted_text = extract_text_from_pdf(file_path)
    cleaned_text = clean_resume_text(extracted_text)
    structured_data = extract_resume_data(cleaned_text)
    ats_analysis = analyze_ats_score(structured_data)

    return {
        "message": "Resume analyzed successfully",
        "structured_data": structured_data,
        "ats_analysis": ats_analysis
    }