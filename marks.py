import csv
import plotly.express as px

with open("Student Marks vs Days Present.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x="Marks In Percentage", y="Days Present", color="Roll No")
    fig.show()