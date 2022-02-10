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

pdf = FPDF()
jsonPDF = "pdfResume.json"

#Name and Picture
class PDF(FPDF):
    def header(me):
        me.set_font('helvetica', 'B', 28.5)
        me.cell(0, 30, 'JELEN KRIZ ANGEL P. MAMPUSTI', align = 'R', ln=1)
        me.ln(3)

    def image(self):
        self.image('RESUME_PIC.jpg', 10, 8, 40)

# Personal Information
for information in Base_info:
    


pdf.output('MAMPUSTI_JELEN KRIZ ANGEL.pdf')