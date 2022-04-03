"""
Websocket client for getting and visualization tickers prices in realtime.
"""
import json

import pandas as pd
import plotly.graph_objects as go
from dash import html, dcc, Dash, Input, Output, State
from dash_extensions import WebSocket

WS_HOST = "localhost"
WS_PORT = 8765

# DataFrame with tickers prices history
df = pd.DataFrame()
tickets = [f'ticker_{i:02}' for i in range(100)]

# Create app layout
app = Dash(prevent_initial_callbacks=True)
app.layout = html.Div(
    [
        html.Div(
            [
                dcc.Dropdown(
                    options=tickets,
                    value=tickets[0],
                    id='trade-instrument-filter',
                    clearable=False
                )
            ]
        ),
        html.Div(
            [
                dcc.Graph(
                    id="graph", 
                    figure=go.Figure(
                        go.Scatter(
                            x=[], 
                            y=[]
                        )
                    )
                )
            ]
        ),
        WebSocket(
            url=f"ws://{WS_HOST}:{WS_PORT}", 
            id="ws"
        )
    ]
)

@app.callback(
    Output("graph", "figure"), 
    [
        Input("ws", "message"),
        Input("trade-instrument-filter", "value")
    ]
)
def update_graph(msg: str, filter: str) -> go.Figure:
    """Update visualization.

    Keyword arguments:
    msg -- message from websocket server
    filter -- filter for ticker

    Return new figure.
    """
    global df

    # getting new data if possible
    if df.empty or not msg['timeStamp'] == max(df['ts']):
        new_tickers = json.loads(msg["data"])
        added_df = pd.DataFrame(
            {
                'ticker': new_tickers.keys(),
                'price': new_tickers.values()
            }
        )
        added_df['ts'] = msg['timeStamp']
        df = pd.concat([df, added_df], ignore_index=True)

    # updating figure with new data or other filter
    current_df = df[df.ticker == filter]
    return go.Figure(
        data=go.Scatter(
            x=current_df.ts, 
            y=current_df.price
        )
    )

if __name__ == "__main__":
    app.run_server(debug=True, port=5000)
