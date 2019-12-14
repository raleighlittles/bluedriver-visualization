![img](https://images-na.ssl-images-amazon.com/images/I/71RQ96Zb9eL._SL1500_.jpg)

# About

This repository contains a very simple script you can use to visualize the data from your BlueDriver OBD2 dongle.
Once you've exported your logs from the app, save them to a directory. 

This script will go through and create a simple scatterplot for every possible data field seen.

Here's an example of one.

![output](output/FuelLevelInput.svg)

# Pre-requisites

Install [Matplotlib](https://matplotlib.org/) and [Pandas](https://pandas.pydata.org/) via setup.py.

# Usage

Run:

```bash 
$ python3 main.py "<input-directory>" "<output-directory>"
```