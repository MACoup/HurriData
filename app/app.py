import os

from flask import Flask
from flask import render_template

from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import (
  GMapPlot, GMapOptions, ColumnDataSource, Circle, DataRange1d, PanTool, WheelZoomTool, BoxSelectTool
)
from bokeh.embed import components


API_KEY = os.environ['GOOGLEMAPS_API_KEY']

buoy_file = os.path.join(os.pardir, 'data', '41010.json')
df_buoy = pd.DataFrame(fj.main(buoy_file))

filename = os.path.join(os.pardir, 'data', 'hurricane_kate.csv')
df = pd.read_csv(filename)
df = process_df(df)

app = Flask(__name__)


def hurricane_map_plot():
    map_options = GMapOptions(lat=30.29, lng=-97.73, map_type="roadmap", zoom=11)

    plot = GMapPlot(
        x_range=DataRange1d(), y_range=DataRange1d(), map_options=map_options
    )
    plot.title.text = "Austin"

    # For GMaps to function, Google requires you obtain and enable an API key:

    plot.api_key = API_KEY
 
#    colors = ['b'] * len()
#    lat = 
#    lon = 
#    buoy_lat = df_buoy.iloc[0]['latitude']
#    buoy_lon = df_buoy.iloc[0]['longitude']
#   
    source = ColumnDataSource(
        data=dict(
            lat=[30.29, 30.20, 30.29],
            lon=[-97.70, -97.74, -97.78],
            colors=colors,
        )
    )

    circle = Circle(x="lon", y="lat", size=15, fill_color="blue", fill_alpha=0.8, line_color=None)
    plot.add_glyph(source, circle)

    plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())

    script, div = components(plot)

    return div, script

@app.route('/')
def main():
    div, script = hurricane_map_plot()
    return render_template('layout.html', div=div, script=script)


if __name__ == '__main__':
    app.run(debug=True)
