# Imports
import plotly.express as px
import pandas as pd
from dash import html, callback, dcc, Output, Input, Dash

# Reading Data
air_passengers = pd.read_csv('data/AirPassengers.csv')
air_passengers['month_start'] = pd.to_datetime(air_passengers['Month'])
air_passengers['year'] = air_passengers['month_start'].dt.year

app = Dash(__name__)

# Defining App Layout
app.layout = html.Div([
    html.H1(children='# Air Passengers Over Time', style={'textAlign':'center'}),
    dcc.Dropdown(options=air_passengers['year'].unique(),
                 value=None,
                 id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

# Update Plot
@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    if value is not None:
        data = air_passengers[air_passengers['year']==value]
    else:
        data = air_passengers

    plot = px.scatter(data, x='month_start', y='#Passengers', trendline='ols')

    return plot

if __name__ == '__main__':
    app.run_server(debug=True)    