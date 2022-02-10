#Assignment 9

#PDF Resume Creator
#	- Create a python program that will create your personal resume in PDF format
#	- All personal details are stored in a JSON file
#	- Your program should read the JSON file and write the details in the PDF
#	- The output file should be: LASTNAME_FIRSTNAME.pdf

#Note:
#	- Search for available PDF library that you can use
#	- Search how data is structured using JSON format
#	- Search how to read JSON file
#	- You will create the JSON file manually

from fpdf import FPDF
import json
from ctypes import alignment

#Header
class PDF(FPDF):
    def header(self):
        self.image('RESUME_PIC', 10, 8, 40)
        self.ln(3)

#Format
pdf = FPDF('P','mm', 'Legal')
pdf.set_auto_page_break(auto=1, margin=55.4)
pdf.add_page()

#Short
jsonPDF = open('pdfResume.json', 'r')
Create = jsonPDF.read()
Info = json.loads(Create)


# Personal Information
for information in Info:
    pdf.set_font('helvetica', "B", 12)
    pdf.cell(0,5, f"{information['Name']}", align='L', ln=1)
    pdf.set_font('helvetica', "", 12)
    pdf.cell(0,5, f"{information['Address']}", align='L', ln=1)
    pdf.cell(0,5, f"{information['E-mail']}", align='L', ln=1)
    pdf.cell(0,5, f"{information['Contact No.']}", align='L', ln=1)
    pdf.ln(12)

    pdf.set_font('helvetica', "B", 15)
    pdf.cell(0, 10, f"{information['head1']}", 'BI', ln=1)
    pdf.ln(3)
    pdf.set_font('helvetica', "I", 12)
    pdf.multi_cell(0, 5, f"{information['Job_Obj']}", 'BI', align='L', ln=1)
    pdf.ln(10)

    pdf.set_font('helvetica', "B", 15)
    pdf.cell(0, 10, f"{information['head2']}", ln=1)
    pdf.ln(5)
    pdf.set_font('helvetica', "", 12)





    


pdf.output('MAMPUSTI_JELEN KRIZ ANGEL.pdf')