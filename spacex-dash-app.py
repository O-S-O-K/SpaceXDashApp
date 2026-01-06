# ----------------------------
# Import required libraries
# ----------------------------
import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# ----------------------------
# Read the SpaceX data into pandas dataframe
# ----------------------------
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

launch_sites = spacex_df['Launch Site'].unique()

# ----------------------------
# Create a dash application
# ----------------------------
app = dash.Dash(__name__)

# ----------------------------
# Create an app layout
# ----------------------------
app.layout = html.Div(children=[
    
    # Header
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36',
                   'font-size': 40}),
    
    # ----------------------------
    # TASK 1: Dropdown for Launch Site
    # ----------------------------
    html.Div([
        html.Label('Select Launch Site:'),
        dcc.Dropdown(
            id='site-dropdown',
            options=[{'label': 'All Sites', 'value': 'ALL'}] +
                    [{'label': site, 'value': site} for site in launch_sites],
            value='ALL',
            placeholder="Select a Launch Site here",
            searchable=True
        )
    ]),
    
    html.Br(),
    
    # ----------------------------
    # TASK 2: Success Pie Chart
    # ----------------------------
    html.Div(dcc.Graph(id='success-pie-chart')),
    
    html.Br(),
    
    # ----------------------------
    # TASK 3: Payload Range Slider
    # ----------------------------
    html.P("Payload range (Kg):"),
    dcc.RangeSlider(
        id='payload-slider',
        min=min_payload,
        max=max_payload,
        step=1000,
        marks={0: '0', 2500: '2500', 5000: '5000', 7500: '7500', 10000: '10000'},
        value=[min_payload, max_payload]
    ),
    
    html.Br(),
    
    # ----------------------------
    # TASK 4: Success vs Payload Scatter Chart
    # ----------------------------
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])

# ----------------------------
# TASK 2: Callback for Pie Chart
# ----------------------------
@app.callback(
    Output('success-pie-chart', 'figure'),
    Input('site-dropdown', 'value')
)
def update_pie_chart(selected_site):
    if selected_site == 'ALL':
        # Total success launches by site
        fig = px.pie(spacex_df,
                     names='Launch Site',
                     values='class',
                     title='Total Success Launches by Site')
    else:
        # Success vs failure for selected site
        filtered_df = spacex_df[spacex_df['Launch Site'] == selected_site]
        counts = filtered_df['class'].value_counts().reset_index()
        counts.columns = ['class', 'count']
        fig = px.pie(counts,
                     names='class',
                     values='count',
                     title=f'Success vs Failure for {selected_site}')
    return fig

# ----------------------------
# TASK 4: Callback for Scatter Chart
# ----------------------------
@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    [Input('site-dropdown', 'value'),
     Input('payload-slider', 'value')]
)
def update_scatter_chart(selected_site, payload_range):
    low, high = payload_range
    df_filtered = spacex_df[(spacex_df['Payload Mass (kg)'] >= low) &
                             (spacex_df['Payload Mass (kg)'] <= high)]
    
    if selected_site != 'ALL':
        df_filtered = df_filtered[df_filtered['Launch Site'] == selected_site]
    
    fig = px.scatter(df_filtered,
                     x='Payload Mass (kg)',
                     y='class',
                     color='Booster Version Category',
                     title='Payload vs Success for selected site(s)')
    return fig

# ----------------------------
# Run the app
# ----------------------------
if __name__ == '__main__':
    app.run(debug=True)
