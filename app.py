# Run this app with `python app.py` 
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

df = pd.read_csv("output.csv")
df = df.sort_values("Date")

app = Dash(__name__)

app.layout = html.Div(style={"fontFamily": "Arial", "backgroundColor": "#f9f9f9", "padding": "20px"}, children=[
    html.H1("Soul Foods: Pink Morsel Sales Visualiser",
            style={"textAlign": "center", "color": "#333"}),

    dcc.RadioItems(
        id="region-filter",
        options=[
            {"label": "North", "value": "north"},
            {"label": "East", "value": "east"},
            {"label": "South", "value": "south"},
            {"label": "West", "value": "west"},
            {"label": "All", "value": "all"},
        ],
        value="all",
        inline=True,
        style={"marginBottom": "20px", "textAlign": "center"}
    ),

    dcc.Graph(id="sales-chart")
])

@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    filtered_df = df if selected_region == "all" else df[df["Region"] == selected_region]
    fig = px.line(filtered_df, x="Date", y="Sales", title="Pink Morsel Sales Over Time")
    fig.update_layout(xaxis_title="Date", yaxis_title="Sales ($)")
    return fig

if __name__ == "__main__":
    app.run(debug=True)