import pandas as pd
import numpy as np

#loading Data

fuel_econ = pd.read_csv('fuel_econ.csv')
pokemon = pd.read_csv('pokemon.csv')

# Day 1/100
fuel = fuel_econ['fuelType']
print(fuel)

#fuel shape
fuel = fuel_econ['fuelType']
fuel= fuel.shape
print(fuel)

#frequency

fuel = fuel_econ['fuelType']
fuel= fuel.value_counts()
print(fuel)

# relative Frequency

fuel = fuel_econ['fuelType']
fuel= fuel.value_counts(normalize=True)
print(fuel)

fuel = fuel_econ['fuelType']
fuel= fuel.value_counts() / fuel.shape[0]
print(fuel)
