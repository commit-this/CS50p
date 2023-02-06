from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 20)
        self.cell(0, None, "CS50 Shirtificate", align="C")


def main():
    shirtificate(input("Name: "))


def shirtificate(name):
    """outputs pdf with shirt image and input name as text on shirt"""
    pdf = PDF()
    pdf.add_page()
    # assemble image onto pdf
    pdf.image("shirtificate.png", x=0.5, y=40)
    # set new font size
    pdf.set_font("helvetica", size=14)
    # font color white
    pdf.set_text_color(255, 255, 255)
    # move cursor down
    pdf.ln(100)
    # print text onto image
    pdf.cell(0, None, f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
