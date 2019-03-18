import fpdf

from fpdf import FPDF

new_pdf = FPDF(format='letter')

new_pdf.add_page()
new_pdf.set_font("Arial",size=12)

new_pdf.cell(200, 10, txt="Example", ln=1, align="C")
new_pdf.cell(200, 10, "Example_line2", 1 , "C")
new_pdf.cell(200, 10, "Example_line3", 1 , "L")

new_pdf.output("test1.pdf")
