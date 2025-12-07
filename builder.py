from model import Duration
from fpdf import FPDF, XPos, YPos, Align
from model import UserDetails, ExpericeDetails, EducationDetails, ProjectDetails


class ResumeBuilder:
    def __init__(
        self,
        details: UserDetails,
        education: list[EducationDetails],
        experience: list[ExpericeDetails],
        skills: list[str],
        certifications: list[str] | None = None,
        projects: list[ProjectDetails] | None = None,
    ):
        self.pdf = FPDF()
        self.details: UserDetails = details
        self.education = education
        self.experience: list[ExpericeDetails] = experience
        self.skills: list[str] = skills
        self.certifications: list[str] | None = certifications
        self.projects: list[ProjectDetails] | None = projects
        # add arial font
        self.pdf.add_font("arial", "", "./fonts/arial.ttf", uni=True)

    def generate_pdf(self, filename):
        self.pdf.add_page()

        self.user_details()

        self.experience_details()

        self.education_details()

        self.skills_details()

        self.pdf.ln(3)

        self.projects_details()

        self.pdf.ln(3)

        self.certification_details()

        self.save_pdf(filename)

    # name section
    def user_details(self):
        # Name
        self.pdf.set_font("arial", "B", 20)
        self.pdf.cell(
            200, 4, text=self.details.name, new_x="LMARGIN", new_y="NEXT", align="C"
        )

        # Contact Info
        self.pdf.set_font("arial", size=10)

        contact = f"{self.details.contact.email} | {self.details.contact.phone} | {self.details.contact.linkedin}"

        if self.details.contact.github is not None:
            contact += f" | {self.details.contact.github}"

        self.pdf.multi_cell(
            w=0,
            h=10,
            text=contact,
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
        )

    def education_details(self):

        self.title(title="Education")

        for edu in self.education:
            self.pdf.set_font("arial", size=12, style="B")
            self.pdf.cell(200, 5, text=edu.degree, new_x="LMARGIN", new_y="NEXT")
            self.pdf.set_font("arial", size=12)
            self.edu_row(edu, gap=6)
            self.pdf.set_font("arial", size=12)
            self.pdf.cell(200, 5, text=f"GPA: {edu.gpa}", new_x="LMARGIN", new_y="NEXT")
            self.pdf.ln(3)

    def experience_details(self):

        # title
        self.title(title="Experience")

        for exp in self.experience:
            self.pdf.set_font("arial", size=14, style="B")
            self.pdf.cell(0, 6, text=exp.company.role, new_x="LMARGIN", new_y="NEXT")
            gap = 6
            self.experience_row(exp, gap)
            self.pdf.ln(1)
            self.pdf.set_font("arial", size=12)
            for achievement in exp.achievements:
                self.pdf.set_x(13)
                self.pdf.multi_cell(
                    w=0,  # 0 means use full width from current x position to right margin
                    h=6,
                    text=f"• {achievement}",
                    new_x=XPos.LMARGIN,
                    new_y=YPos.NEXT,
                )
            self.pdf.ln(2)

    def skills_details(self):

        self.title(title="Skills")

        self.pdf.set_font("arial", size=12)
        for skill in self.skills:
            self.pdf.cell(0, 6, text=f"• {skill}", new_x="LMARGIN", new_y="NEXT")

    def projects_details(self):

        if self.projects is None or len(self.projects) == 0:
            return

        self.title(title="Projects")

        for project in self.projects:
            self.pdf.set_font("arial", size=12, style="B")
            self.pdf.cell(0, 6, text=project.name, new_x="LMARGIN", new_y="NEXT")

            # Technologies and Duration row
            gap = 6
            border = 0
            self.pdf.set_font("arial", size=11)

            tech_str = ", ".join(project.technologies)
            self.pdf.cell(
                None,
                gap,
                text=f"Technologies: {tech_str}",
                border=border,
            )

            # Add duration if available
            if project.duration is not None:
                self.pdf.cell(
                    0,
                    gap,
                    text=f"{project.duration.start_year} - {project.duration.end_year}",
                    align=Align.R,
                    new_y=YPos.NEXT,
                    new_x="LMARGIN",
                    border=border,
                )
            else:
                self.pdf.ln()

            # Highlights
            self.pdf.ln(1)
            self.pdf.set_font("arial", size=12)
            for highlight in project.highlights:
                self.pdf.set_x(13)
                self.pdf.multi_cell(
                    w=0,
                    h=6,
                    text=f"• {highlight}",
                    new_x=XPos.LMARGIN,
                    new_y=YPos.NEXT,
                )
            self.pdf.ln(2)

    def certification_details(self):

        if self.certifications is None:
            return

        self.title(title="Cerfitications")

        self.pdf.set_font("arial", size=12)
        for certificate in self.certifications:
            self.pdf.cell(0, 6, text=f"• {certificate}", new_x="LMARGIN", new_y="NEXT")

    def divider(self):
        self.pdf.set_draw_color(0, 0, 0)
        self.pdf.set_line_width(0.2)
        self.pdf.line(x1=10, y1=self.pdf.get_y(), x2=200, y2=self.pdf.get_y())
        self.pdf.ln(3)

    def title(self, title: str):
        # Check if there's enough space on the page for the title and some content
        # If less than 30mm remaining, start a new page
        page_height = self.pdf.h - self.pdf.b_margin  # Total usable height
        current_y = self.pdf.get_y()
        remaining_space = page_height - current_y

        # If less than 30mm of space, add a new page
        if remaining_space < 30:
            self.pdf.add_page()

        self.pdf.set_font("arial", "B", 14)
        self.pdf.cell(200, 7, text=title.upper(), new_x="LMARGIN", new_y="NEXT")
        self.divider()

    def experience_row(self, experience: ExpericeDetails, gap: int):
        font_size = 12
        border = 0
        self.pdf.set_font("arial", size=font_size, style="B")
        self.pdf.cell(
            None,
            gap,
            text=experience.company.name + "," + experience.company.location,
            border=border,
        )
        self.pdf.set_font("arial", size=font_size)

        self.pdf.cell(
            0,
            gap,
            text=f"{experience.company.duration.start_year} - {experience.company.duration.end_year}",
            align=Align.R,
            new_y=YPos.NEXT,
            new_x="LMARGIN",
            border=border,
        )

    def edu_row(self, education: EducationDetails, gap: int):
        font_size = 11
        border = 0
        self.pdf.set_font("arial", size=font_size)
        self.pdf.cell(
            None,
            gap,
            text=education.college_name,
            border=border,
        )
        self.pdf.set_font("arial", size=font_size)
        self.pdf.cell(
            0,
            gap,
            text=f"{education.duration.start_year} - {education.duration.end_year}",
            align=Align.R,
            new_y=YPos.NEXT,
            new_x="LMARGIN",
            border=border,
        )

    # Save PDF to file
    def save_pdf(self, filename):
        self.pdf.output(filename)
