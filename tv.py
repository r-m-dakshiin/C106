import csv
import plotly.express as px

with open("Size of TV,_Average time spent watching TV in a week (hours).csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x="Size of TV", y="Average time spent watching TV in a week (hours)")
    fig.show()