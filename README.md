# Python Package Exercise

## Package Description

This package allows for users to easily convert values to different units, for data, distance, mass, and temperature.

[![Python package CI](https://github.com/swe-students-spring2026/3-package-silverback_gorilla/actions/workflows/python-package-ci.yml/badge.svg)](https://github.com/swe-students-spring2026/3-package-silverback_gorilla/actions/workflows/python-package-ci.yml)

## PyPI Page
 
[Link](https://github.com/swe-students-spring2026/3-package-silverback_gorilla/tree/main)
Needs to be updated

## How to Use

### Setup

```bash 
pip install unit-convert-swe-nyu
```

The package is now built!

### Function Overview

```convert_data(x: float, unit_from: UnitData, unit_to: UnitData)```

Converts data units (KB, MB, GB, etc.)

```convert_distance(x: float, unit_from: UnitDistance, unit_to: UnitDistance)```

Converts distance units (meters, kilometers, miles, etc.)

```convert_mass(x: float, unit_from: UnitMass, unit_to: UnitMass)```

Converts mass units (grams, kilograms, pounds)

```convert_temperature(x: float, unit_from: UnitTemperature, unit_to: UnitTemperature)```

Converts temperature units (Celsius, Fahrenheit, Kelvin)

### Example Usage

```python
# Option 1:
# from unit_convert import *

# Option 2: explicit import
from unit_convert import (
    convert_data,
    convert_distance,
    convert_mass,
    convert_temperature,
    UnitData,
    UnitDistance,
    UnitMass,
    UnitTemperature,
)

print(convert_data(1024, "KB", "MB"))
print(convert_distance(1, "mile", "km"))
print(convert_mass(10, "kg", "lb"))
print(convert_temperature(32, "F", "C"))
```

### Example File

[Example](example.py)

### Run Example Locally

From the project root:

```bash
# using pipenv
pipenv run pip install -e .
pipenv run python example.py
```

### Run Example in Another Project

Install from PyPI:

```bash
pip install unit-convert-swe-nyu
```

Create an `example.py` file in any folder, then run:

```bash
python example.py
```

## How to Contribute

To contribute to this project you must fork the repository, then submit your changes via pull request and wait for it to be accepted.

Test the project using
```pytest```
before creating a pull request.

## Team members

Aleks Nuzhnyi - [GitHub Profile](https://github.com/nuzhny25)  
Calvin Pun - [GitHub Profile](https://github.com/CalvinPun)  
Sunil Parab - [GitHub Profile](https://github.com/SunilParab)  
Yash Pazhianur - [GitHub Profile](https://github.com/yashpaz123)  
