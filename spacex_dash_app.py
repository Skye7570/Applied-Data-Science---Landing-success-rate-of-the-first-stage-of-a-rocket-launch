# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()
spacex_df['result'] = 56 * ["fail"]
spacex_df['count'] = 56 * [1]

for Class, index in zip(spacex_df['class'], spacex_df.index):
    if Class == 1:
        spacex_df.iloc[index,7] = 'success'
    elif Class == 0:
        spacex_df.iloc[index,7] = 'fail'

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(id = 'site-dropdown',
                                             options = [{'label': 'All Sites', 'value': 'ALL'},
                                                        {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                                                        {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                                                        {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                                                        {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}],
                                             value = 'ALL',
                                             placeholder = 'Select a Launch Site here',
                                             searchable = True),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(id = 'payload-slider', min = 0, max = 10000, step = 1000,
                                                marks = {0: '0', 2500: '2500', 5000: '5000', 7500: '7500', 10000: '10000'},
                                                value = [min_payload, max_payload]),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(Output(component_id = 'success-pie-chart', component_property = 'figure'),
              Input(component_id = 'site-dropdown', component_property = 'value'))

def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        pie_fig_all = px.pie(spacex_df, values = 'class', names = 'Launch Site', title = 'Total Success Launches By Site')
        return pie_fig_all
    elif entered_site == 'CCAFS LC-40':
        pie_fig_1 = px.pie(spacex_df[spacex_df['Launch Site'] == 'CCAFS LC-40'], values = 'count', names = 'result', title = 'Total Success Launches for site CCAFS LC-40')
        return pie_fig_1
    elif entered_site == 'VAFB SLC-4E':
        pie_fig_2 = px.pie(spacex_df[spacex_df['Launch Site'] == 'VAFB SLC-4E'], values = 'count', names = 'result', title = 'Total Success Launches for site VAFB SLC-4E')
        return pie_fig_2
    elif entered_site == 'KSC LC-39A':
        pie_fig_3 = px.pie(spacex_df[spacex_df['Launch Site'] == 'KSC LC-39A'], values = 'count', names = 'result', title = 'Total Success Launches for site KSC LC-39A')
        return pie_fig_3
    else:
        pie_fig_4 = px.pie(spacex_df[spacex_df['Launch Site'] == 'CCAFS LC-40'], values = 'count', names = 'result', title = 'Total Success Launches for site CCAFS SLC-40')
        return pie_fig_4



# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id = 'success-payload-scatter-chart', component_property = 'figure'),
              [Input(component_id = 'site-dropdown', component_property = 'value'),
               Input(component_id = 'payload-slider', component_property = 'value')])

def get_scatter_chart(entered_site, payload):
    if entered_site == 'ALL':
        scatter_fig = px.scatter(spacex_df, x = 'Payload Mass (kg)', y = 'class', color = 'Booster Version Category')
        return scatter_fig
    elif entered_site == 'CCAFS LC-40':
        scatter_fig1 = px.scatter(spacex_df[spacex_df['Launch Site'] == 'CCAFS LC-40'], x = 'Payload Mass (kg)', y = 'class', color = 'Booster Version Category')
        return scatter_fig1
    elif entered_site == 'VAFB SLC-4E':
        scatter_fig2 = px.scatter(spacex_df[spacex_df['Launch Site'] == 'VAFB SLC-4E'], x = 'Payload Mass (kg)', y = 'class', color = 'Booster Version Category')
        return scatter_fig2
    elif entered_site == 'KSC LC-39A':
        scatter_fig3 = px.scatter(spacex_df[spacex_df['Launch Site'] == 'KSC LC-39A'], x = 'Payload Mass (kg)', y = 'class', color = 'Booster Version Category')
        return scatter_fig3
    else:
        scatter_fig4 = px.scatter(spacex_df[spacex_df['Launch Site'] == 'CCAFS LC-40'], x = 'Payload Mass (kg)', y = 'class', color = 'Booster Version Category')
        return scatter_fig4


# Run the app
if __name__ == '__main__':
    app.run_server()
