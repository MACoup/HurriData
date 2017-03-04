#!/usr/bin/env python
from __future__ import print_function

import simplejson
from pandas import DataFrame


def main(filename):
    axis_keys = ["time", "latitude", "longitude"]
    with open(filename) as handle:
        data = simplejson.loads(handle.read())
    return [
        {
            k: v
            for k, v in entry["data"].items() + [(key, entry["axes"][key]) for key in axis_keys]
        }
        for entry in data["entries"]
    ]

if __name__ == '__main__':
    x = main("32012.json")
    pd = DataFrame(x)
    print(pd.head())
