x=0
y=0

import csv
ex= []
weatherdata = {}
with open('weather.csv','rt') as file:
    weather = csv.reader(file)
    for row in weather:
        weatherdata[str(row)] = row

for i in weatherdata:
    if weatherdata[i][1] > "30":
        if weatherdata[i][21] == "Yes":
            x +=1
        else:
            y +=1

print("(",x," + ",y,")/2")
pro = (x+y)/2
print("the probability of rain: ",pro)
