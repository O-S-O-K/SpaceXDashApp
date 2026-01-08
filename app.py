import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
import os

# Load dataset
df = pd.read_csv("spacex_launch_dash.csv")

# Initialize Dash app
app = dash.Dash(__name__)
server = app.server

# Example scatter plot
fig = px.scatter(
    df,
    x="FlightNumber",
    y="PayloadMass",
    color="BoosterVersion",
    title="SpaceX Launches Dashboard"
)

# Layout
app.layout = html.Div([
    html.H1("SpaceX Falcon 9 Launch Dashboard"),
    dcc.Graph(figure=fig)
])

# Run server
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))
    app.run_server(debug=False, host="0.0.0.0", port=port)
