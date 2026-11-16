import csv
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Report Title
        self.set_font("Arial", 'B', 16)
        self.set_text_color(0, 0, 128)
        self.cell(0, 10, "Student Marks Report", ln=True, align="C")
        self.ln(5)

def read_data(file_path):
    data = []
    with open(file_path, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def generate_report(data, output_path):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Table Header
    pdf.set_fill_color(173, 216, 230)  # Light blue background
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(60, 10, "Name", 1, 0, "C", fill=True)
    pdf.cell(60, 10, "Subject", 1, 0, "C", fill=True)
    pdf.cell(60, 10, "Marks", 1, 1, "C", fill=True)

    # Table Data
    total = 0
    count = 0
    pdf.set_font("Arial", size=12)
    for row in data:
        name = row["Name"]
        subject = row["Subject"]
        marks = int(row["Marks"])
        total += marks
        count += 1

        pdf.cell(60, 10, name, 1, 0, "C")
        pdf.cell(60, 10, subject, 1, 0, "C")
        pdf.cell(60, 10, str(marks), 1, 1, "C")

    # Summary Section
    average = total / count if count > 0 else 0
    pdf.ln(5)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, f"Total Students: {count}", ln=True)
    pdf.cell(0, 10, f"Total Marks: {total}", ln=True)
    pdf.cell(0, 10, f"Average Marks: {average:.2f}", ln=True)

    # Save PDF
    pdf.output(output_path)
    print(f"Report generated successfully: {output_path}")

# -------------------------
# Main Program
# -------------------------
if __name__ == "__main__":
    input_file = "sample_data.csv"   # Make sure this file exists in the same folder
    output_file = "student_report.pdf"

    data = read_data(input_file)
    generate_report(data, output_file)