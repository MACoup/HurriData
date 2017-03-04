import os

import pandas as pd
import matplotlib.pyplot as plt

import flatten_json as fj

def time_convert(military_time):
    military_time = str(military_time)
    if len(military_time) == 1:
	military_time += '0' * (4 - len(military_time))
    elif len(military_time) == 3:
	military_time = '0' + military_time

    military_time = military_time[:2] + ':' + military_time[2:]
    military_time += ':00'
    return military_time


def process_df(df_in):
    df = df_in.copy()
    # Create proper timestamp:
    df['Time (UTC)'] = df['Time (UTC)'].apply(time_convert)
    dt_str = df['Date'] + ' ' + df['Time (UTC)']
    df['datetime'] = dt_str.apply(pd.Timestamp)
    del df['Date']
    del df['Time (UTC)']

    # Set timestamp as index and 'pad':
    df.index = df['datetime']
    del df['datetime']
    df = df.fillna(method='pad')

    # Fix column names
    columns = df.columns.tolist()
    cs = [c.split('(')[0].lower() for c in columns]

    cs_ = ['_'.join(c.split()) for c in cs]

    df.columns = cs_

    return df


if __name__ == '__main__':
    buoy_file = os.path.join(os.pardir, 'data', '41010.json')
    df_buoy = pd.DataFrame(fj.main(buoy_file))

    filename = os.path.join(os.pardir, 'data', 'hurricane_kate.csv')
    df = pd.read_csv(filename)
    df = process_df(df)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(-df['longitude'].values, df['latitude'])
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_title('Hurricane Kate')

    buoy_lon = df_buoy.iloc[0]['longitude']
    buoy_lat = df_buoy.iloc[0]['latitude']
    ax.scatter(buoy_lon, buoy_lat, color='r')

    ax.annotate('41010', (buoy_lon-0.6, buoy_lat+0.6))

    savefile = os.path.join(os.pardir, 'images', 'hurricane_kate.png')
    plt.savefig(savefile)
    plt.show()

