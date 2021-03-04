import csv
from datetime import datetime


def readCSV(fileName, min, max, date, highVals, lowVals, dateVals, NameIndex, titles):
    getName = True

    for row in fileName:
        try:
            high = int(row[max])
            low = int(row[min])
            converted_date = datetime.strptime(row[date], "%Y-%m-%d")
            if(getName):
                Name = row[NameIndex]
                titles.append(Name)
                getName = False
        except ValueError:
            print(f"Missing data for {converted_date}")
        else:
            highVals.append(high)
            lowVals.append(low)
            dateVals.append(converted_date)


def retMin(dictionary):
    return dictionary['TMIN']

def retMax(dictionary):
    return dictionary["TMAX"]

def retDate(dictionary):
    return dictionary["DATE"]

def retName(dictionary):
    return dictionary["NAME"]


#Death Valley input
dv_Input = open("death_valley_2018_simple.csv", "r")
csv_file1 = csv.reader(dv_Input, delimiter=",")
header_row1 = next(csv_file1)

#Sitka input
Sitka_Input = open("sitka_weather_2018_simple.csv", "r")
csv_file2 = csv.reader(Sitka_Input, delimiter=",")
header_row2 = next(csv_file2)

#Creating empty dictionaries to store header/index values
dv_Index = {}
Sitka_Index = {}

#Storing header/index values in dictionaries
for index, column_header in enumerate(header_row1):
    dv_Index[column_header] = index

for index, column_header in enumerate(header_row2):
    Sitka_Index[column_header] = index

print(dv_Index, Sitka_Index)

dv_highs = []
dv_lows = []
dv_dates = []

Sitka_highs = []
Sitka_lows = []
Sitka_dates = []

dv_Min = retMin(dv_Index)
Sitka_Min = retMin(Sitka_Index)

dv_Max = retMax(dv_Index)
Sitka_Max = retMax(Sitka_Index)

dv_Date = retDate(dv_Index)
Sitka_Date = retDate(Sitka_Index)

dv_nameIndex = retName(dv_Index)
Sitka_nameIndex = retName(Sitka_Index)

names = []

#Need to call function to find/store values
#Format: fileName, min, max, date, highVals, lowVals, dateVals
readCSV(csv_file1, dv_Min, dv_Max, dv_Date, dv_highs, dv_lows, dv_dates, dv_nameIndex, names)
readCSV(csv_file2, Sitka_Min, Sitka_Max, Sitka_Date, Sitka_highs, Sitka_lows, Sitka_dates, Sitka_nameIndex, names)

dv_Name = names[0]
Sitka_Name = names[1]

#plot data on chart
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 1)

#Sitka
ax[0].plot(Sitka_dates, Sitka_highs, c="red")
ax[0].plot(Sitka_dates, Sitka_lows, c="blue")
ax[0].fill_between(Sitka_dates, Sitka_highs, Sitka_lows, facecolor="blue", alpha=.1)
ax[0].set_title(Sitka_Name, fontsize = 14)
ax[0].set_xlabel("", fontsize = 12)
ax[0].set_ylabel("Temperature (F)", fontsize = 12)
ax[0].tick_params(axis="both", labelsize = 12)

#Death Valley
ax[1].plot(dv_dates, dv_highs, c="red")
ax[1].plot(dv_dates, dv_lows, c="blue")
ax[1].fill_between(dv_dates, dv_highs, dv_lows, facecolor="blue", alpha=.1)
ax[1].set_title(dv_Name, fontsize = 14)
ax[1].set_xlabel("", fontsize = 12)
ax[1].set_ylabel("Temperature (F)", fontsize = 12)
ax[1].tick_params(axis="both", labelsize = 12)

fig.autofmt_xdate()

plt.show()