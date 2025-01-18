"""
My approach involves loading student data from an Excel file and validating the presence of necessary columns.
I then group the data by student ID, calculate the total and average scores for each student, and collect
the subject-wise scores. Using this data, I generate a personalized PDF report card that includes the student's
name, ID, total score, average score, and a table of subject-wise scores. The content is centered, the font
size is increased, and I apply styling such as bold headers and table adjustments to enhance
readability and presentation. This process ensures that each student receives a well-formatted, easy-to-read
report card summarizing their performance.

## Below is the python script:

Install the required libraries using pip:

Install the required libraries using pip:

   ```bash
   pip install pandas reportlab
   ```

Run the script:

   ```bash
   python main.py
   ```
"""


import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import os

def generate_report_cards(file_path):
    try:
        # Step 1: Load the excel file
        data = pd.read_excel(file_path)

        # Validate required columns
        required_columns = ['Student ID','Name','Subject','Score']
        if not all(col in data.columns for col in required_columns):
            raise ValueError("Excel file is missing required columns: 'Student ID','Name','Subject','Score'")

        # Step 2: Group and process the data
        grouped = data.groupby('Student ID')
        for student_id, group in grouped:
            student_name = group['Name'].iloc[0]
            total_score = group['Score'].sum()
            avg_score = group['Score'].mean()
            subject_scores = group[['Subject','Score']].values.tolist()

            # Step 3: Generate PDF report card
            pdf_file_name = f"report_card_{student_id}.pdf"
            pdf_path = os.path.join(os.getcwd(), pdf_file_name)

            doc = SimpleDocTemplate(pdf_path, pagesize=letter)
            elements = []

            # Add Student Information
            styles = getSampleStyleSheet()
            title_style = styles['Title']
            title_style.fontSize = 22 # Increase font size for the title
            normal_style = styles['Normal']
            normal_style.fontSize = 12 # Increase font size for normal text

            # Bold Style for Name
            bold_style = normal_style.clone('BoldStyle')
            bold_style.fontName = 'Helvetica-Bold'

            # Center-align Student Information - Use alignment=1 (center)
            student_info_style = normal_style
            student_info_style.alignment = 0 # Center-align the text

            elements.append(Paragraph(f"Report Card", title_style))
            elements.append(Spacer(1,24))
            elements.append(Paragraph(f"<b>Name:</b> { student_name}", student_info_style))
            elements.append(Spacer(1, 12))
            elements.append(Paragraph(f"<b>Student ID:</b> { student_id}", student_info_style))
            elements.append(Spacer(1, 12))
            elements.append(Paragraph(f"<b>Total Score:</b> {total_score}", student_info_style))
            elements.append(Spacer(1, 12))
            elements.append(Paragraph(f"<b>Average Score:</b> {avg_score:.2f}", student_info_style))
            elements.append(Spacer(1, 24))

            # Add Subject-wise scores as a table
            table_data = [['Subject', 'Score']] + subject_scores
            table = Table(table_data, colWidths=[120, 80], hAlign='LEFT')
            table.setStyle(TableStyle([
                ('BACKGROUND', (0,0),(-1,0), colors.grey),
                ("TEXTCOLOR",(0,0),(-1,0), colors.whitesmoke),
                ('ALIGN', (0,0),(-1,-1), 'LEFT'),
                ('FONTNAME', (0,0),(-1,0),'Helvetica-Bold'),
                ('BOTTOMPADDING', (0,0),(-1,0), 12),
                ('BACKGROUND', (0,1),(-1,-1), colors.beige),
                ('GRID', (0,0),(-1,-1),1, colors.black),
            ]))
            elements.append(table)

            # Build the PDF
            doc.build(elements)
            print(f"Report card generated: {pdf_path}")

    except FileNotFoundError:
        print("Error: The specified Excel file was not found")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occured: {e}")

# Run the script
file_path = 'student_data.xlsx'
generate_report_cards(file_path)


























