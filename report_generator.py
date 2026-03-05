import pandas as pd
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4

data = pd.read_csv("data.csv")

average = data["Marks"].mean()

plt.bar(data["Name"], data["Marks"])
plt.savefig("chart.png")
plt.close()

pdf = SimpleDocTemplate("Report.pdf", pagesize=A4)
elements = []

styles = getSampleStyleSheet()
elements.append(Paragraph("Student Report", styles['Title']))
elements.append(Spacer(1, 0.5 * inch))
elements.append(Paragraph(f"Average Marks: {average}", styles['Normal']))
elements.append(Spacer(1, 0.5 * inch))
elements.append(Image("chart.png", width=4*inch, height=3*inch))

pdf.build(elements)

print("Report Created Successfully!")