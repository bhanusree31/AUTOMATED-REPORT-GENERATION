import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from matplotlib.backends.backend_pdf import PdfPages

def generate_sample_data():
    """Creates a sample DataFrame."""
    data = {
        "Category": ["A", "B", "C", "D"],
        "Value1": [10, 20, 30, 40],
        "Value2": [5, 15, 25, 35]
    }
    return pd.DataFrame(data)

def analyze_data(df):
    """Performs basic data analysis and returns summary statistics."""
    return df.describe()

def generate_plot(df):
    """Generates a plot and saves it as an image."""
    plt.figure()
    plt.plot(df['Value1'], label='Value1')
    plt.plot(df['Value2'], label='Value2')
    plt.title('Sample Data Plot')
    plt.xlabel('Index')
    plt.ylabel('Values')
    plt.legend()
    plt.savefig('report_plot.png')
    plt.close()

def generate_pdf_report(summary, output_path):
    """Generates a PDF report with the summary statistics and a plot."""
    with PdfPages(output_path) as pdf:
        plt.figure()
        plt.plot(summary.loc['mean'], label='Mean')
        plt.title('Summary Statistics Plot')
        plt.xlabel('Metrics')
        plt.ylabel('Values')
        plt.legend()
        pdf.savefig()
        plt.close()
        
        c = canvas.Canvas(output_path.replace('.pdf', '_text.pdf'), pagesize=letter)
        c.setFont("Helvetica", 12)
        c.drawString(100, 750, "Automated Report Generation")
        c.drawString(100, 730, "Summary Statistics:")
        
        y_position = 710
        for index, row in summary.iterrows():
            for col in summary.columns:
                text = f"{col} ({index}): {row[col]:.2f}"
                c.drawString(100, y_position, text)
                y_position -= 20
                if y_position < 50:
                    c.showPage()
                    c.setFont("Helvetica", 12)
                    y_position = 750
        c.save()
    print(f"Report generated: {output_path}")

# Example usage
output_pdf = https://private-user-images.githubusercontent.com/87653798/402273506-ea1e2d0e-ad31-41f8-9638-ed0f82e75f2a.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDc4MDMzMDgsIm5iZiI6MTc0NzgwMzAwOCwicGF0aCI6Ii84NzY1Mzc5OC80MDIyNzM1MDYtZWExZTJkMGUtYWQzMS00MWY4LTk2MzgtZWQwZjgyZTc1ZjJhLmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MjElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTIxVDA0NTAwOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTdkZWZmMzZiNDljNmQxMzU5M2Y2MDk5ZWEwOWY5ZGEzYTM1MjM1YTgxZTUxNjM0YjVjNTJmY2EyMTcxZjg0MGUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.722JtoIIWFLtlVtXNPPiM05-oind7KYfgWdVEp70XtM
df = generate_sample_data()
summary = analyze_data(df)
generate_plot(df)
generate_pdf_report(summary, output_pdf)
