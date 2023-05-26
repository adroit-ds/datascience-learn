# Imports
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import html, callback, dcc, Output, Input, Dash, dash_table
from load_data import load_air_passengers, load_monthly_milk, load_air_pollution

# Load Data in Memory
air_passengers = load_air_passengers()
monthly_milk = load_monthly_milk()
air_pollution = load_air_pollution()

# Initialization
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Univariate Dataset Options
univariate_data_options = ['Air Passengers', 'Monthly Milk']

# Multivariate Dataset Options
multivariate_data_options = ['Air Pollution']

# Defining App Layout
app.layout = html.Div(children=[
    html.H1(children='Time Series Visualization', style={'textAlign' : 'center'}),

    dbc.Row(
        [dbc.Col(html.Div(children=[
            html.H3(children='Univariate Plot', style={'textAlign' : 'center'}),
            dcc.Dropdown(options=univariate_data_options,
                         value='Air Passengers',
                         id='dropdown-selection-univariate'),
            dcc.Graph(id='graph-content-univariate'),
            html.H3(children='Sample Data', style={'textAlign' : 'center'}), 
            html.Div(id='univariate_table')]), style={'border' : '2px black solid'}),

         dbc.Col(html.Div(children=[
            html.H3(children='Multivariate Plot', style={'textAlign' : 'center'}),
            dbc.Row([dbc.Col(dcc.Dropdown(options=multivariate_data_options,
                                          value='Air Pollution',
                                          id='dropdown-selection-multivariate')),
                     dbc.Col(dcc.Dropdown(id='x-variable-dropdown',
                                          placeholder='Select X-Variable')),
                     dbc.Col(dcc.Dropdown(id='y-variable-dropdown',
                                          placeholder='Select Y-Variable'))]),
            dcc.Graph(id='graph-content-multivariate'),
            html.H3(children='Sample Data', style={'textAlign' : 'center'}),
            html.Div(id='multivariate_table')]), style={'border' : '2px black solid'})]),
])


# Populate Univariate Table
@callback(
    Output('univariate_table', 'children'),
    Input('dropdown-selection-univariate', 'value')
)
def update_table_univariate(value):
    if value == 'Air Passengers':
        data = air_passengers
    elif value == 'Monthly Milk':
        data = monthly_milk
    
    sample_data = data.head(10)
    sample_data = sample_data.to_dict('records')
    columns = [{'name' : i, 'id' : i} for i in (data.columns)]

    return dash_table.DataTable(data=sample_data, columns=columns)
   

# Update Univariate Plot
@callback(
    Output('graph-content-univariate', 'figure'),
    Input('dropdown-selection-univariate', 'value')
)
def update_graph_univariate(value):
    if value == 'Air Passengers':
        data = air_passengers
        x = 'month_start'
        y = '#Passengers'
    elif value == 'Monthly Milk':
        data = monthly_milk
        x = 'month_start'
        y = 'pounds_per_cow'

    plot = px.scatter(data, x=x, y=y, trendline='ols')

    return plot


# Select Multivariate Dataset & Get Data Columns
@callback(
    Output('x-variable-dropdown', 'options'),
    Output('y-variable-dropdown', 'options'),
    Input('dropdown-selection-multivariate', 'value')
)
def set_variable_options(dataset):
    if dataset == 'Air Pollution':
        data = air_pollution
        options = [col for col in data.columns if col not in ['year', 'month', 'day', 'hour', 'cbwd']]

    return options, options


# Set Default Column from Selected Multivariate Dataset
@callback(
    Output('x-variable-dropdown', 'value'),
    Output('y-variable-dropdown', 'value'),
    Input('x-variable-dropdown', 'options')
)
def set_variable_value(available_columns):
     
    return available_columns[-1], available_columns[1]


# Populate Multivariate Table
@callback(
    Output('multivariate_table', 'children'),
    Input('dropdown-selection-multivariate', 'value')
)
def update_table_multivariate(value):
    if value == 'Air Pollution':
        data = air_pollution
    
    sample_data = data.head(10)
    sample_data = sample_data.to_dict('records')
    columns = [{'name' : i, 'id' : i,} for i in (data.columns)]

    return html.Div([dash_table.DataTable(data=sample_data, columns=columns)])
   

# Update  Multivariate Plot
@callback(
    Output('graph-content-multivariate', 'figure'),
    Input('dropdown-selection-multivariate', 'value'),
    Input('x-variable-dropdown', 'value'),
    Input('y-variable-dropdown', 'value')    
)
def update_graph_multivariate(dataset, x_var, y_var):
    if dataset == 'Air Pollution':
        data = air_pollution
        x = str(x_var)
        y = str(y_var)

        plot = px.scatter(data, x=x, y=y, trendline='ols')

    return plot


if __name__ == '__main__':
    app.run_server(debug=True)