import copy

from dash.dependencies import Input
from dash.dependencies import Output

layout = dict(
    autosize=True,
    automargin=True,
    height=150,
    margin=dict(l=30, r=30, b=00, t=00),
    hovermode="closest",
    plot_bgcolor="#F9F9F9",
    paper_bgcolor="#fff",
    font=dict(color="#777777"),
    legend=dict(
        font=dict(color="#333", size="10"),
        orientation="v",
        bgcolor="rgba(0,0,0,0)",
        y=0.8),
    title=""
)

graph_data = dict(
    type="pie",
    hoverinfo="label+value+percent",
    textinfo="percent",
    textfont=dict(size=9, color="#fff"),
    hole=0.5,
    direction="clockwise",
    sort=False,
    marker=dict(
        colors=["#0077C8", "#32a3df", "#673ab7", "#9c27b0"],
        line=dict(color='#fff', width=1)
    ),
)

def register_callbacks(dashapp):
    @dashapp.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
    def update_graph(selected_dropdown_value):
        device_types = ['Client A', 'Client B', 'Client C', 'Client D']
        yy = [27.5, 26.4, 32.3, 13.8]

        data = copy.deepcopy(graph_data)
        data['labels'] = device_types
        data['values'] = yy

        figure = dict(data=[data], layout=layout)
        return figure
