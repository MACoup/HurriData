#!/usr/bin/env python
"""
Script to pull buoy data into json files
"""
from __future__ import print_function

from sys import stderr
import os
import os.path

import requests

FMT = (
    "https://api.planetos.com/v1/datasets/noaa_ndbc_stdmet_stations/stations/" +
    "{0}?apikey={1}&count=200000"
)

BUOY_IDS = [
    '41001',
    '41002',
    '41003',
    '41004',
    '41005',
    '41006',
    '41007',
    '41008',
    '41009',
    '41010',
    '41011',
    '41012',
    '41015',
    '41016',
    '41017',
    '41018',
    '41021',
    '41022',
    '41023',
    '41025',
    '42001',
    '42002',
    '42003',
    '42004',
    '42005',
    '42006',
    '42007',
    '42008',
    '42009',
    '42010',
    '42011',
    '42012',
    '42015',
    '42016',
    '42017',
    '42018',
    '42019',
    '42020',
    '42025',
    '42035',
    '42036',
    '42037',
    '42039',
    '42040',
    '42041',
    '42042',
    '42054',
    '44001',
    '44003',
    '44004',
    '44005',
    '44006',
    '44007',
    '44008',
    '44009',
    '44010',
    '44011',
    '44012',
    '44013',
    '44014',
    '44015',
    '44017',
    '44018',
    '44019',
    '44023',
    '44025',
    '44026',
    '44028',
    'EB01',
    'EB10',
    'EB31',
    'EB32',
    'EB36',
    'EB52',
    'EB53',
    'EB61',
    'EB62',
    'EB91',
    'EB92',
]



def get_buoy(buoy_id, apikey="9e4d0dff12f7436fbd72cdeff2cab51b"):
    """ Get a single buoy """
    print(buoy_id, file=stderr)
    filename = "{0}.json".format(buoy_id)
    if not os.path.exists(filename):
        url = FMT.format(buoy_id, apikey)
        print(url, file=stderr)
        req = requests.get(url)
        with open(filename, "w") as handle:
            handle.write(req.text)


def get_all_buoys():
    """ Get data for all buoys """
    for buoy_id in BUOY_IDS:
        get_buoy(buoy_id)


if __name__ == '__main__':
    get_all_buoys()
