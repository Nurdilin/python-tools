import fpdf

from fpdf import FPDF

new_pdf = FPDF(format='letter')

new_pdf.add_page()
new_pdf.set_font("Arial",size=12)

new_pdf.cell(200, 10, txt="Example_line1", border=0,  ln=1, align="C")
new_pdf.cell(200, 10, "Example_line2", 0, 1 , "L")
new_pdf.cell(200, 10, "Example_line3", 1, 1 , "L")

new_pdf.cell(80) #move 80 to right
new_pdf.cell(10, 10, "Example_text1", 0, 1)
new_pdf.cell(0, 300, "Going down", 0, 1)

# ln    Indicates where the current position should go after the call. Possible values are:
#            0: to the right
#            1: to the beginning of the next line
#            2: below



new_pdf.set_x(20)
new_pdf.set_y(20)
new_pdf.write(5, "1", "www.google.com")

new_pdf.set_x(140)
new_pdf.set_y(20)
new_pdf.write(5, "2", "www.google.com")

new_pdf.set_x(140)
new_pdf.set_y(40)
new_pdf.write(5, "3", "www.google.com")

new_pdf.set_x(20)
new_pdf.set_y(40)
new_pdf.write(5, "4", "www.google.com")

new_pdf.text(50,50,"test")

new_pdf.output("test1.pdf")
