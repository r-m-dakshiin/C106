import csv
import plotly.express as px

with open("Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x="Ice-cream Sales", y="Cold drink sales", color="Temperature")
    fig.show()