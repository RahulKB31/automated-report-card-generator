---

# Student Report Card Generator

This project automates the generation of personalized report cards for students. It reads student data from an Excel file, processes the data, and generates PDF report cards for each student. The generated report cards include the student's name, student ID, total score, average score, and a table of subject-wise scores.

![Report Card](https://github.com/RahulKB31/automated-report-card-generator/blob/main/report_card.jpg)


## Features
- Loads student data from an Excel file.
- Validates the presence of required columns: `Student ID`, `Name`, `Subject`, `Score`.
- Groups data by `Student ID` to calculate total and average scores.
- Generates personalized PDF report cards for each student.
- Applies formatting with centered content, bold headers, increased font sizes, and styled tables for readability.

## Requirements
- Python 3.x
- `pandas` library for data handling
- `reportlab` library for generating PDF files

## Installation

1. Install the required libraries using pip:

   ```bash
   pip install pandas reportlab
   ```

2. Ensure you have the Excel file containing student data with the required columns: `Student ID`, `Name`, `Subject`, and `Score`.

## Usage

1. Save the script to a Python file (e.g., `generate_report_cards.py`).
2. Place your Excel file (e.g., `student_scores.xlsx`) in the same directory as the script or provide the correct path.
3. Run the script:

   ```bash
   python main.py
   ```

4. The script will generate a PDF report card for each student and save them in the current directory with filenames like `report_card_<Student ID>.pdf`.

## Script Overview

### 1. Data Loading and Validation
The script reads the student data from an Excel file and checks for the presence of necessary columns: `Student ID`, `Name`, `Subject`, and `Score`.

### 2. Data Processing
It groups the data by `Student ID`, calculates the total and average scores, and collects subject-wise scores for each student.

### 3. PDF Generation
The script generates a personalized PDF report card for each student. The report card includes:
- The student's name (bold)
- The student’s ID
- Total and average score
- A table displaying subject-wise scores

### 4. Styling and Formatting
The PDF content is centered, the font size is increased, and the table is styled with bold headers and clear spacing for better readability.

## Example

An example of the generated PDF report card:

- Title: "Report Card"
- Student Information (Centered):
  - Name: `John Doe`
  - Student ID: `12345`
  - Total Score: `450`
  - Average Score: `90.00`
- Subject-wise Scores:
  - Subject 1: `Math`, Score: `95`
  - Subject 2: `Science`, Score: `90`
  - Subject 3: `English`, Score: `85`

## License
This project is open-source and available under the MIT License.

---
