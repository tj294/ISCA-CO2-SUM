"""
Script to determine total CPU time used on ISCA in a given time period, and associated
energy and CO2 usage.
Author: Tom Joshi-Cale (tj294@exeter.ac.uk)
"""

import numpy as np
from os import system

username = str(input("ISCA username?\n"))

system("sacct -T -S2020-01-01-12:00 -u {} -ojobid,start,end,cputime,cputimeraw > isca_history.txt".format(username))

data = np.genfromtxt('isca_history.txt', dtype=None, skip_header=2, usecols=(4))
total_secs = np.sum(data)
total_hours = total_secs / 3600
total_days = total_hours / 24
print('Total time: %d days, %d hours, %d minutes, %d seconds' % (total_days, total_hours % 24, total_secs % 3600 / 60, total_secs % 60))

ISCA_WATTS_PER_CPU = 90/16 # 90 Watts per 16 CPU node
total_joules = ISCA_WATTS_PER_CPU * total_secs
print("Total energy usage {2.3e} J".format(total_joules))
total_kwh = total_joules * 2.778e-7
total_co2 = total_kwh * 0.19338 #based on UK grid June 2022
print("Total CO2 usage: {.3f} kg".format(total_co2))
