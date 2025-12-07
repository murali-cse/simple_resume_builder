class ContactDetails:
    def __init__(self, email, phone, linkedin, github: str | None = None):
        self.email: str = email
        self.phone: str = phone
        self.linkedin: str = linkedin
        self.github: str | None = github


class Duration:
    def __init__(self, start_year, end_year):
        self.start_year: str = start_year
        self.end_year: str = end_year


class Company:
    def __init__(self, name: str, location: str, role: str, duration: Duration):
        self.name: str = name
        self.location: str = location
        self.role: str = role
        self.duration: Duration = duration


class ExpericeDetails:
    def __init__(self, company: Company, achievements):
        self.company: Company = company
        self.achievements: list[str] = achievements


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


class UserDetails:
    def __init__(self, name, contact: ContactDetails):
        self.name: str = name
        self.contact: ContactDetails = contact
