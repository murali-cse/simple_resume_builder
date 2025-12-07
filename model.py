class ContactDetails:
    def __init__(self, email, phone, linkedin, github: str | None = None):
        self.email: str = email
        self.phone: str = phone
        self.linkedin: str = linkedin
        self.github: str | None = github

    @staticmethod
    def fromJson(json_data: dict):
        return ContactDetails(
            email=json_data["email"],
            phone=json_data["phone"],
            linkedin=json_data["linkedin"],
            github=json_data["github"],
        )


class Duration:
    def __init__(self, start_year, end_year):
        self.start_year: str = start_year
        self.end_year: str = end_year

    @staticmethod
    def fromJson(json_data: dict):
        return Duration(
            start_year=json_data["start_year"],
            end_year=json_data["end_year"],
        )


class Company:
    def __init__(self, name: str, location: str, role: str, duration: Duration):
        self.name: str = name
        self.location: str = location
        self.role: str = role
        self.duration: Duration = duration

    @staticmethod
    def fromJson(json_data: dict):
        return Company(
            name=json_data["name"],
            location=json_data["location"],
            role=json_data["role"],
            duration=Duration.fromJson(json_data["duration"]),
        )


class ExpericeDetails:
    def __init__(self, company: Company, achievements):
        self.company: Company = company
        self.achievements: list[str] = achievements

    @staticmethod
    def fromJson(json_data: dict):
        return ExpericeDetails(
            company=Company.fromJson(json_data["company"]),
            achievements=json_data["achievements"],
        )


class EducationDetails:
    def __init__(
        self,
        college_name: str,
        duration: Duration,
        degree: str,
        gpa: str | None = None,
    ):
        self.college_name: str = college_name
        self.duration: Duration = duration
        self.degree: str = degree
        self.gpa: str | None = gpa

    @staticmethod
    def fromJson(json_data: dict):
        return EducationDetails(
            college_name=json_data["college_name"],
            duration=Duration.fromJson(json_data["duration"]),
            degree=json_data["degree"],
            gpa=json_data["gpa"],
        )


class ProjectDetails:
    def __init__(
        self,
        name: str,
        technologies: list[str],
        duration: Duration | None = None,
        highlights: list[str] = [],
    ):
        self.name: str = name
        self.technologies: list[str] = technologies
        self.duration: Duration | None = duration
        self.highlights: list[str] = highlights

    @staticmethod
    def fromJson(json_data: dict):
        return ProjectDetails(
            name=json_data["name"],
            technologies=json_data["technologies"],
            duration=Duration.fromJson(json_data["duration"]),
            highlights=json_data["highlights"],
        )


class UserDetails:
    def __init__(self, name, contact: ContactDetails):
        self.name: str = name
        self.contact: ContactDetails = contact

    @staticmethod
    def fromJson(json_data: dict):
        return UserDetails(
            name=json_data["name"],
            contact=ContactDetails.fromJson(json_data["contact"]),
        )


class ResumeDetails:
    def __init__(
        self,
        details: UserDetails,
        education: list[EducationDetails],
        experience: list[ExpericeDetails],
        skills: list[str],
        certifications: list[str],
        projects: list[ProjectDetails],
    ):
        self.details: UserDetails = details
        self.education: list[EducationDetails] = education
        self.experience: list[ExpericeDetails] = experience
        self.skills: list[str] = skills
        self.certifications: list[str] = certifications
        self.projects: list[ProjectDetails] = projects

    @staticmethod
    def fromJson(json_data: dict):
        return ResumeDetails(
            details=UserDetails.fromJson(json_data["details"]),
            education=[
                EducationDetails.fromJson(edu) for edu in json_data["education"]
            ],
            experience=[
                ExpericeDetails.fromJson(exp) for exp in json_data["experience"]
            ],
            skills=json_data["skills"],
            certifications=json_data["certifications"],
            projects=[ProjectDetails.fromJson(proj) for proj in json_data["projects"]],
        )
