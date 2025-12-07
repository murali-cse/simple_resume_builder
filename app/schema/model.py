from pydantic import BaseModel
from typing import List, Optional


class ContactDetails(BaseModel):
    email: str
    phone: str
    linkedin: str
    github: Optional[str] = None


class Duration(BaseModel):
    start_year: str | int
    end_year: str | int


class Company(BaseModel):
    name: str
    location: str
    role: str
    duration: Duration


class ExperienceDetails(BaseModel):
    company: Company
    achievements: List[str]


class EducationDetails(BaseModel):
    college_name: str
    duration: Duration
    degree: str
    gpa: Optional[str] = None


class ProjectDetails(BaseModel):
    name: str
    technologies: List[str]
    duration: Optional[Duration] = None
    highlights: List[str] = []


class UserDetails(BaseModel):
    name: str
    contact: ContactDetails


class ResumeDetails(BaseModel):
    details: UserDetails
    education: List[EducationDetails]
    experience: List[ExperienceDetails]
    skills: List[str]
    certifications: List[str]
    projects: List[ProjectDetails]
