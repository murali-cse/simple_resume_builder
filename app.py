from model import EducationDetails, ProjectDetails
from builder import ResumeBuilder
from model import ExpericeDetails, UserDetails, ContactDetails, Company, Duration


if __name__ == "__main__":

    contact_details = ContactDetails(
        email="sarah.anderson@email.com",
        phone="+1-415-892-3456",
        linkedin="linkedin.com/in/sarah-anderson-dev",
        github="github.com/sanderson-dev",
    )

    details = UserDetails(name="Sarah Anderson".upper(), contact=contact_details)

    experience: list[ExpericeDetails] = [
        ExpericeDetails(
            company=Company(
                name="TechVision Solutions",
                role="Senior Software Engineer",
                duration=Duration(start_year=2021, end_year="Present"),
                location="San Francisco, CA",
            ),
            achievements=[
                "Led development of microservices architecture serving 2M+ daily active users, reducing API response time by 45%",
                "Architected and implemented CI/CD pipeline using Jenkins and Docker, decreasing deployment time from 2 hours to 15 minutes",
                "Mentored team of 5 junior developers and conducted code reviews to maintain high code quality standards",
                "Designed and built real-time analytics dashboard using React and WebSocket, improving data visibility for stakeholders",
            ],
        ),
        ExpericeDetails(
            company=Company(
                name="DataStream Analytics",
                role="Software Engineer",
                duration=Duration(start_year=2019, end_year=2021),
                location="Austin, TX",
            ),
            achievements=[
                "Developed RESTful APIs using Python Flask and PostgreSQL, handling 500K+ requests per day",
                "Implemented automated testing suite with 85% code coverage, reducing production bugs by 60%",
                "Optimized database queries and indexing strategies, improving query performance by 3x",
                "Collaborated with product team to deliver 12+ features across web and mobile platforms",
            ],
        ),
        ExpericeDetails(
            company=Company(
                name="CloudNet Systems",
                role="Junior Software Developer",
                duration=Duration(start_year=2017, end_year=2019),
                location="Seattle, WA",
            ),
            achievements=[
                "Built responsive web applications using React, Redux, and Node.js for enterprise clients",
                "Integrated third-party payment APIs (Stripe, PayPal) processing $2M+ in transactions monthly",
                "Participated in Agile development process with daily standups and bi-weekly sprint planning",
                "Created comprehensive technical documentation for internal APIs and development workflows",
            ],
        ),
    ]

    education: list[EducationDetails] = [
        EducationDetails(
            college_name="Stanford University",
            duration=Duration(start_year=2015, end_year=2017),
            degree="Master of Science in Computer Science",
            gpa="3.9",
        ),
        EducationDetails(
            college_name="University of California, Berkeley",
            duration=Duration(start_year=2011, end_year=2015),
            degree="Bachelor of Science in Computer Engineering",
            gpa="3.7",
        ),
    ]

    projects: list[ProjectDetails] = [
        ProjectDetails(
            name="E-Commerce Platform",
            technologies=["React", "Node.js", "PostgreSQL", "Redis", "AWS"],
            duration=Duration(start_year="2023", end_year="2024"),
            highlights=[
                "Built scalable e-commerce platform handling 100K+ daily transactions with 99.9% uptime",
                "Implemented real-time inventory management system reducing stock discrepancies by 80%",
                "Integrated Stripe payment gateway with fraud detection, processing $5M+ in annual revenue",
            ],
        ),
        ProjectDetails(
            name="Open Source Contribution - Django REST Framework",
            technologies=["Python", "Django", "REST APIs"],
            highlights=[
                "Contributed 15+ pull requests to Django REST Framework, improving API serialization performance by 20%",
                "Authored documentation for authentication middleware used by 10K+ developers",
            ],
        ),
    ]

    resume = ResumeBuilder(
        details=details,
        education=education,
        experience=experience,
        skills=[
            "Python (Django, Flask, FastAPI)",
            "JavaScript/TypeScript (React, Node.js, Express)",
            "Database Systems (PostgreSQL, MongoDB, Redis)",
            "Cloud Platforms (AWS, Google Cloud, Azure)",
            "DevOps (Docker, Kubernetes, Jenkins, GitHub Actions)",
            "System Design & Microservices Architecture",
            "RESTful APIs & GraphQL",
            "Agile/Scrum Methodologies",
        ],
        certifications=[
            "AWS Certified Solutions Architect - Associate",
            "Google Cloud Professional Developer",
            "Certified Kubernetes Application Developer (CKAD)",
            "MongoDB Certified Developer",
        ],
        projects=projects,
    )

    resume.generate_pdf("resume.pdf")
