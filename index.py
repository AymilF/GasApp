# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

from app import app
from layouts.layouts_home import layout_homepage

app.layout = html.Div([
    dcc.Location(
        id="url_id",
        refresh=False
    ),
    html.Div(
        id="page-content"
    )
])


@app.callback(
    Output("page-content", "children"),
    Input("url_id", "pathname"))
def display_page(pathname):

    if pathname == "/home":
        return layout_homepage

    return layout_homepage


if __name__ == '__main__':
    app.run_server(
        port="8084",
        debug=True,
        host="0.0.0.0"
    )
