"""
Script to determine total CPU time used on ISCA in a given time period, and associated
energy and CO2 usage.
Author: Tom Joshi-Cale (tj294@exeter.ac.uk)
"""

import numpy as np
from os import system

username = str(input("ISCA username?\n"))

system(f"sacct -T -S2020-01-01-12:00 -u {username} -ojobid,start,end,cputime,cputimeraw > isca_history.txt")

data = np.genfromtxt('isca_history.txt', dtype=None, skip_header=2, usecols=(4))
total_secs = np.sum(data)
total_hours = total_secs / 3600
total_days = total_hours / 24
print('Total time: %d days, %d hours, %d minutes, %d seconds' % (total_days, total_hours % 24, total_secs % 3600 / 60, total_secs % 60))

ISCA_WATTS_PER_CPU = 90/16 # 90 Watts per 16 CPU node
total_joules = ISCA_WATTS_PER_CPU * total_secs
print(f"Total energy usage {total_joules:2.3e} J")
total_kwh = total_joules * 2.778e-7
total_co2 = total_kwh * 0.19338 #based on UK grid June 2022
print(f"Total CO2 usage: {total_co2:.3f} kg")
