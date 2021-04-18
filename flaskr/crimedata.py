import numpy as np
import pandas as pd
import os
from scipy import stats
df = pd.read_csv("crime.csv")
crimes = []
class Crime:
    type = ""
    posn = (0, 0) 
    def __init__(self, type, posn, time):
        self.type = type
        self.posn = posn
        self.time = time
posns = df['Location']
offenses = df['OFFENSE_CODE_GROUP']
times = df['HOUR']
for i in range(len(df)):
    crimes.append(Crime(offenses[i], eval(posns[i]), times[i]))
    
# radius in degrees
def get_num_crimes_in_radius(posn, radius, time):
    num_crimes_in_radius = 0
    bad_crime_weight = 0
    for crime in crimes:
        dist = get_distance(crime.posn, posn)
        time_range = (crime.time-3, crime.time+3)
        if dist < radius and int(time) >= time_range[0] and int(time) <= time_range[1]:
            num_crimes_in_radius = num_crimes_in_radius + 1
    return num_crimes_in_radius
def get_distance(posn1, posn2):
    return np.sqrt((posn1[0] - posn2[0])**2 + (posn1[1] - posn2[1])**2)
    
def get_weight(posn, radius, time):
    return get_num_crimes_in_radius(posn, radius, time)

