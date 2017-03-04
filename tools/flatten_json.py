#!/usr/bin/env python
from __future__ import print_function
from itertools import chain

import simplejson
from pandas import DataFrame


def main(filename):
    with open(filename) as handle:
        data = simplejson.loads(handle.read())
    return [
        # Merge two dictionaries into one.
        # http://stackoverflow.com/questions/38987/how-to-merge-two-python-dictionaries-in-a-single-expression
        dict(chain(entry["data"].items(), entry["axes"].items()))
        for entry in data["entries"]
    ]

if __name__ == '__main__':
    x = main("../data/41010.json")
    pd = DataFrame(x)
    print(pd.head())
