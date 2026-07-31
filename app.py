# Run this app with `python app.py` 


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

df = pd.read_csv("output.csv")
df = df.sort_values("Date")

fig = px.line(df, x="Date", y="Sales", title="Pink Morsel Sales Over Time")
fig.update_layout(xaxis_title="Date", yaxis_title="Sales ($)")


app = Dash(__name__)
app.layout = html.Div([
    html.H1("Soul Foods: Pink Morsel Sales Visualiser"),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)