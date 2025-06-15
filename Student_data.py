import csv
from fpdf import FPDF

# 💡 Step 1: Load data from CSV file
filename = 'student_data.csv'  # Make sure this file exists in the same directory
students = []

with open(filename, newline='') as file:
    reader = csv.reader(file)
    headers = next(reader)  # Skip header row
    for row in reader:
        name, marks = row[0], int(row[1])
        students.append((name, marks))

# 📊 Step 2: Analyze data (calculate average marks)
total_marks = sum(marks for _, marks in students)
average_marks = total_marks / len(students)

# 📝 Step 3: Generate PDF using FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, "📋 Student Performance Report", ln=True, align='C')
pdf.ln(10)

# Table headers
pdf.set_font("Arial", 'B', 12)
pdf.cell(100, 10, "Student Name", border=1)
pdf.cell(40, 10, "Marks", border=1)
pdf.ln()

# Student data rows
pdf.set_font("Arial", size=12)
for name, marks in students:
    pdf.cell(100, 10, name, border=1)
    pdf.cell(40, 10, str(marks), border=1)
    pdf.ln()

# Summary
pdf.ln(10)
pdf.set_font("Arial", 'B', 12)
pdf.cell(100, 10, "📈 Average Marks:", border=0)
pdf.cell(40, 10, f"{average_marks:.2f}", border=0)

# Save the PDF
report_name = "student_report.pdf"
pdf.output(report_name)

print(f"✅ PDF Report '{report_name}' generated successfully!")
