# -*- coding: utf-8 -*-
# (c) Copyright 2022 Sensirion AG, Switzerland

import os
import re
from setuptools import setup, find_packages


# Read version number from version.py
version_line = open("circuitpython_sensirion_i2c_sen5x/version.py", "rt").read()
result = re.search(r"^version = ['\"]([^'\"]*)['\"]", version_line, re.M)
if result:
    version_string = result.group(1)
else:
    raise RuntimeError("Unable to find version string")


# Use README.rst and CHANGELOG.rst as package description
root_path = os.path.dirname(__file__)
readme = open(os.path.join(root_path, 'README.rst'), encoding='utf-8').read()
changelog = open(os.path.join(root_path, 'CHANGELOG.rst'), encoding='utf-8').read()
long_description = readme.strip() + "\n\n" + changelog.strip() + "\n"


setup(
    name='circuitpython-sensirion-i2c-sen5x',
    version=version_string,
    author='Sensirion',
    author_email='info@sensirion.com',
    description='I2C Driver for Sensirion SEN5x Sensors. Fork of official python driver.',
    license='BSD',
    keywords='sensirion i2c sen5x sen50 sen54 sen55 driver',
    url='https://github.com/good-enough-technology/CircuitPython_sensirion_i2c_sen5x',
    packages=find_packages(exclude=['tests', 'tests.*']),
    long_description=long_description,
    python_requires='>=3.5',
    install_requires=[
        'circuitPython-sensirion-i2c-sen5x',
    ],
    extras_require={
        'test': [
            'flake8~=3.9.2',
            'pytest~=5.4.3',
            'pytest-cov~=2.12.1',
            'sensirion-shdlc-sensorbridge~=0.1.1',
        ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: System :: Hardware :: Hardware Drivers'
    ]
)
