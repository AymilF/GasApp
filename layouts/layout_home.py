import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash import dash_table

navbar = html.Div(
    children=[
        dbc.Nav(
            [
                dbc.NavItem(dbc.NavLink("Home",
                                        href="/home", active="exact")),
                dbc.NavItem(dbc.NavLink("Ajout de stations",
                                        href="/explore", active="exact")),
                dbc.NavItem(dbc.NavLink("Gestion des stations",
                                        href="/gaslist", active="exact"))
            ],
            className="navbar",
            pills=True,
            justified=True,
            fill=True
        ),
        html.Br()
    ]
)


layout_homepage = html.Div(
    [
        html.Div(
            [
                dcc.Markdown(
                    "# **Liste des Stations**",
                    className="maintitle"
                )
            ]
        ),
        navbar,
        html.Div(
            [
                dcc.Interval(
                    id="interval_updatedays",
                    interval=2000
                    ),
                dcc.Markdown(" ## Vous êtes :"),
                dcc.Dropdown(
                    id="configuration_id",
                    value=None,
                    multi=False,
                    clearable=False
                                ),
            ]
        )
    ]
)
