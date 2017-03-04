import os

import cPickle as pickle
import pandas as pd
from flask import Flask
from flask import render_template

from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import (
  GMapPlot, GMapOptions, ColumnDataSource, Circle, DataRange1d, PanTool, WheelZoomTool, BoxSelectTool
)
from bokeh.embed import components

import flatten_json as fj


API_KEY = os.environ['GOOGLEMAPS_API_KEY']

buoy_file = os.path.join(os.pardir, 'data', '41010.json')
df_buoy = pd.DataFrame(fj.main(buoy_file))

filename = os.path.join(os.pardir, 'data', 'hurricane_kate.csv')
with open('../data/hurricane_df.pkl', 'rb') as f:
    df = pickle.load(f)

app = Flask(__name__)


def hurricane_map_plot():
    map_options = GMapOptions(lat=28.906000137329102, lng=-78.471000671386719, map_type="roadmap", zoom=5)

    plot = GMapPlot(
        x_range=DataRange1d(), y_range=DataRange1d(), map_options=map_options
    )
    plot.title.text = "Hurricane Kate"

    # For GMaps to function, Google requires you obtain and enable an API key:

    plot.api_key = API_KEY
 
    lat = list(df['latitude'].values)
    lon = list(-df['longitude'].values)
    colors = ['b'] * len(lat)
    buoy_lat = df_buoy.iloc[0]['latitude']
    buoy_lon = df_buoy.iloc[0]['longitude']

    source = ColumnDataSource(
        data=dict(
            lat=lat,
            lon=lon,
        )
    )
    source2 = ColumnDataSource(
        data=dict(
            lat=[buoy_lat],
            lon=[buoy_lon],
        )
    )

    circle = Circle(x="lon", y="lat", size=15, fill_color="blue", fill_alpha=0.8, line_color=None)
    plot.add_glyph(source, circle)
    circle2 = Circle(x="lon", y="lat", size=15, fill_color="red", fill_alpha=0.8, line_color=None)
    plot.add_glyph(source2, circle2)

    plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())

    script, div = components(plot)

    return div, script

@app.route('/')
def main():
    div, script = hurricane_map_plot()
    return render_template('layout.html', div=div, script=script)


if __name__ == '__main__':
    app.run(debug=True)
