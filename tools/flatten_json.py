#!/usr/bin/env python
from __future__ import print_function

import simplejson
from pandas import DataFrame


def main(filename):
    with open(filename) as handle:
        data = simplejson.loads(handle.read())
    return [
        # Merge two dicitonaries into one.
        # http://stackoverflow.com/questions/38987/how-to-merge-two-python-dictionaries-in-a-single-expression
        # A highly dubious approach
        dict(entry["data"], **entry["axes"])
        for entry in data["entries"]
    ]

if __name__ == '__main__':
    x = main("../data/41010.json")
    pd = DataFrame(x)
    print(pd.head())
