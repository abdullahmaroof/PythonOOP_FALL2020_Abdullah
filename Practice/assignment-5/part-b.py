#find maximum temperature in MaxTemp column in weather.csv dataset and determined, did it rain that day when MaxTemp was maximum.

# Reading an excel file using Python
import csv
ex= []
weatherdata = {}
with open('weather.csv','rt') as file:
    weather = csv.reader(file)
    for row in weather:
        weatherdata[str(row)] = row
maxtemp = []
for column in weatherdata:
    x = weatherdata[str(column)][1]
    maxtemp.append(x)
maxtemp.pop(0)
for i in range(0,len(maxtemp)):
    maxtemp[i] = float(maxtemp[i])
print(maxtemp)
max = max(maxtemp)
index = maxtemp.index(max)
index +=1
print("The maxtemp = ",max)
for i in weatherdata:
    if weatherdata[i][1] == "35.8":
        print("there is a ran = ",weatherdata[i][21])








