# app/main.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import uuid

from app.schema.model import ResumeDetails
from builder.builder import ResumeBuilder
from pathlib import Path

app = FastAPI(title="Resume Generator API")

BASE_DIR = Path(__file__).parent
STATIC_DIR = BASE_DIR / "static"

app.mount(
    "/assets",
    StaticFiles(directory=STATIC_DIR / "assets"),
    name="assets",
)

@app.get("/{full_path:path}")
def serve_react_app(full_path: str):
    index_file = STATIC_DIR / "index.html"
    if index_file.exists():
        return FileResponse(index_file)
    return {"error": "React build not found"}


@app.post("/api/generate_resume")
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
