#!/usr/bin/env python
from setuptools import setup

def dependencies():
    with open("requirements.txt") as handle:
        return [line.strip() for line in handle if not line.startswith("#")]


setup(
    name='HurriData',
    version='0.1',
    description='Application for Galvanize hackathon',
    author='Dylan Albrecht, Dan Beerman, Mark Coup, Hugh Brown',
    author_email='djalbrecht@email.wm.edu, coupmark@gmail.com, daniel.beerman@galvanize.com, hughdbrown@yahoo.com',
    license="MIT",
    install_requires=dependencies(),
)
