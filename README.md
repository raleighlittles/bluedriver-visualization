![img](https://images-na.ssl-images-amazon.com/images/I/71RQ96Zb9eL._SL1500_.jpg)

# About

This repository contains a very simple script you can use to visualize the data from your BlueDriver OBD2 dongle.
Once you've exported your logs from the app, save them to a directory.

Your log files should be in CSV format, with 2 lines (a name and a date) before the column heading, ie.

```
BlueDriver Data Log
Jul 23, 2018 8:18:31 AM
Time (s),Barometric Pressure (kPa),Vehicle Speed (MPH),Absolute Load Value (%),Ambient Air Temperature (°C),Intake Air Temperature (°C),Engine Coolant Temperature (°C),Catalyst Temperature Bank 1 - Sensor 1 (°C),Engine RPM (rpm),Fuel Level Input (%)
```

This script will go through and create a simple scatterplot for every possible data field seen, and optionally, rename your log file using the timestamp.

Here's an example of one scatterplot.

![output](output/FuelLevelInput.svg)

# Pre-requisites

Install [Matplotlib](https://matplotlib.org/) and [Pandas](https://pandas.pydata.org/) via setup.py.

# Usage

Run:

```
usage: bluedriver_visualizer.py [-h] -i INPUT_FOLDER -o OUTPUT_FOLDER -r

options:
  -h, --help            show this help message and exit
  -i INPUT_FOLDER, --input-folder INPUT_FOLDER
                        Input directory: where Bluedriver data files are stored
  -o OUTPUT_FOLDER, --output-folder OUTPUT_FOLDER
                        Output directory: where output graphs will be stored
  -r, --rename          Whether or not you'd like the files to be renamed
```