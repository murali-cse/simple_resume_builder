# app/main.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import uuid

from app.schema.model import ResumeDetails
from builder.builder import ResumeBuilder

app = FastAPI(title="Resume Generator API")


@app.post("/generate_resume")
async def generate_resume(resume_data: ResumeDetails):
    """
    Generate a PDF resume from JSON data.
    Returns the PDF file.
    """
    try:
        file_name = f"resume_{uuid.uuid4().hex}.pdf"

        resume_builder = ResumeBuilder(
            details=resume_data.details,
            education=resume_data.education,
            experience=resume_data.experience,
            skills=resume_data.skills,
            certifications=resume_data.certifications,
            projects=resume_data.projects,
        )

        resume_builder.generate_pdf(file_name)

        return FileResponse(
            path=file_name, filename="resume.pdf", media_type="application/pdf"
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
