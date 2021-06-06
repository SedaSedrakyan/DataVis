import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import plotly.express as px

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]

data=pd.read_csv('hippoCorpusV2.csv')

# Histogram for working seconds
counts_1, bins_1 = np.histogram(data.WorkTimeInSeconds, bins=range(0, 12000, 2000))
counts_2, bins_2 = np.histogram(data.annotatorAge, bins=range(0, 100, 10))
counts_3, bins_3 = np.histogram(data.stressful, bins=range(0, 4, 4))
bins_1 = 0.5 * (bins_1[:-1] + bins_1[1:])
bins_2 = 0.5 * (bins_2[:-1] + bins_2[1:])
bins_3 = 0.5 * (bins_3[:-1] + bins_3[1:])
fig_1 = px.bar(x=bins_1, y=counts_1, labels={'x':'Total working seconds', 'y':'number of observations'}, title='Working seconds')
fig_5 = px.bar(x=bins_2, y=counts_2, labels={'x':'Annotator Age', 'y':'number of observations'}, title='Annotator age')
#fig_6 = px.bar(x=bins_3, y=counts_3, labels={'x':'Stress Level', 'y':'number of observations'}, title='Stress Level')
fig_2 = px.box(data, y='annotatorAge', title='Age distribution')
genders=data['annotatorGender']
fig_3 = go.Figure([go.Bar(x=genders, y=data.groupby(data['annotatorGender'])['annotatorGender'].count())])
app=dash.Dash()
fig_7 = px.scatter(data, x='draining', y='stressful', color="stressful")
fig_8 = px.scatter(data, x='frequency', y='stressful', color="stressful")
"""fig_9 = px.bar(data, x="memType", color="annotatorGender",
             y='annotatorGender',
             title="Gender differences in story telling",
             barmode='group'
            )"""
app.layout = html.Div([
				 html.H1('Dash App Human Cognition'),
				
	html.Div([
		html.Div([ dcc.Graph(figure=fig_1)], className='two columns')
		], className='row'),
	html.Div([html.P('Time in seconds that it took the worker to do the entire HIT (reading instructions, story writing, questions)')]),
	html.Div([
		html.Div([ dcc.Graph(figure=fig_2)], className='two columns')
		], className='row'),
	html.Div([html.P('Lower limit of the age bucket of the worker. Buckets are: 18-24, 25-29, 30-34, 35-39, 40-44, 45-49, 50-54, 55+')]),
	html.Div([
		html.Div([ dcc.Graph(figure=fig_3)], className='two columns')
		], className='row'),
	html.Div([html.P('Gender of the worker')]),
		html.Div([
		html.Div([ dcc.Graph(figure=fig_5)], className='two columns')
		], className='row'),
	html.Div([html.P('Races of the worker')]),
	html.Div([
		html.Div([ dcc.Graph(figure=fig_7)], className='two columns')
		], className='row'),
	html.Div([html.P('Stress VS draining')]),
		html.Div([
		html.Div([ dcc.Graph(figure=fig_8)], className='two columns')
		], className='row'),
	html.Div([html.P('How often do you think about or talk about this event?')])
	], className='container')

if __name__ == '__main__':
	app.run_server(debug=True, host = '127.0.0.1')