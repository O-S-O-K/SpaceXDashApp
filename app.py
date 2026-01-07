# app.py
import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

# ---------------------------
# Load your dataset
# ---------------------------
df = pd.read_csv("spacex_launch_dash.csv")  # Make sure this CSV is in the same folder

# Example: simple scatter plot
fig = px.scatter(
    df,
    x="FlightNumber",
    y="PayloadMass",
    color="BoosterVersion",
    title="SpaceX Launches Dashboard"
)

# ---------------------------
# Initialize Dash app
# ---------------------------
app = dash.Dash(__name__)
server = app.server  # Needed for Render/Heroku

app.layout = html.Div([
    html.H1("SpaceX Falcon 9 Launch Dashboard"),
    dcc.Graph(figure=fig)
])

# ---------------------------
# Run server (local testing)
# ---------------------------
if __name__ == "__main__":
    app.run_server(debug=True)
