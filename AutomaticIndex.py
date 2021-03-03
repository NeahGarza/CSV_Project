import csv
from datetime import datetime

def readCSV(fileName, min, max, date, highVals, lowVals, dateVals):
    for row in fileName:
        try:
            high = int(row[max])
            low = int(row[min])
            converted_date = datetime.strptime(row[date], "%Y-%m-%d")
        except ValueError:
            print(f"Missing data for {converted_date}")
        else:
            highVals.append(int(row[max]))
            lowVals.append(int(row[min]))
            dateVals.append(converted_date)

def retMin(dictionary):
    return dictionary['TMIN']

def retMax(dictionary):
    return dictionary["TMAX"]

def retDate(dictionary):
    return dictionary["DATE"]

def retStation(dictionary):
    return dictionary["STATION"]

#Death Valley input
DV_Input = open("death_valley_2018_simple.csv", "r")
csv_file1 = csv.reader(DV_Input, delimiter=",")
header_row1 = next(csv_file1)

#Sitka input
Sitka_Input = open("sitka_weather_2018_simple.csv", "r")
csv_file2 = csv.reader(Sitka_Input, delimiter=",")
header_row2 = next(csv_file2)

#Creating empty dictionaries to store header/index values
DV_Index = {}
Sitka_Index = {}

#Storing header/index values in dictionaries
for index, column_header in enumerate(header_row1):
    DV_Index[column_header] = index

for index, column_header in enumerate(header_row2):
    Sitka_Index[column_header] = index

print(DV_Index, Sitka_Index)

DV_highs = []
DV_lows = []
DV_dates = []

Sitka_highs = []
Sitka_lows = []
Sitka_dates = []

DV_Min = retMin(DV_Index)
Sitka_Min = retMin(Sitka_Index)

DV_Max = retMax(DV_Index)
Sitka_Max = retMax(Sitka_Index)

DV_Date = retDate(DV_Index)
Sitka_Date = retDate(Sitka_Index)

DV_Station = retStation(DV_Index)
Sitka_Station = retStation(Sitka_Index)

#Need to call function to find/store values
#Format: fileName, min, max, date, highVals, lowVals, dateVals
readCSV(csv_file1, DV_Min, DV_Max, DV_Date, DV_highs, DV_lows, DV_dates)
readCSV(csv_file2, Sitka_Min, Sitka_Max, Sitka_Date, Sitka_highs, Sitka_lows, Sitka_dates)

print(DV_dates, Sitka_dates)

#plot data on chart

import matplotlib.pyplot as plt

fig, ax = plt.subplots(2,1, sharex=True)

#Sitka
ax[0].plot(Sitka_highs, c="red")
ax[0].plot(Sitka_lows, c="blue")
ax[0].fill_between(Sitka_Date, Sitka_highs, Sitka_lows, facecolor="blue", alpha=.1)
#ax[0].title(Sitka_Station, fontsize = 16)
#ax[0].xlabel("", fontsize = 12)
#ax[0].ylabel("Temperature (F)", fontsize = 12)
#ax[0].tick_params(axis="both", labelsize = 12)

#Death Valley
ax[1].plot(DV_dates, DV_highs, c="red")
ax[1].plot(DV_dates, DV_lows, c="blue")
ax[1].fill_between(DV_dates, DV_highs, DV_lows, facecolor="blue", alpha=.1)
#ax[1].title(DV_Station, fontsize = 16)
#ax[1].xlabel("", fontsize = 12)
#ax[1].ylabel("Temperature (F)", fontsize = 12)
#ax[1].tick_params(axis="both", labelsize = 12)

fig.autofmt_xdate()

plt.show()