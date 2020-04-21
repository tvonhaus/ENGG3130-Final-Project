import csv
import matplotlib.pyplot as plt
import numpy as np

years = []
hares = []
lynx = []

with open('HudsonBayData.txt') as HusonBayDataFile:
    csv_reader = csv.reader(HusonBayDataFile, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            years.append(row[0])
            hares.append(int(row[1]))
            lynx.append(int(row[2]))
            line_count += 1


# print(hares)
# print(lynx)

plt.plot(years,hares,label='Hares')
plt.plot(years,lynx,label='Lynx')
plt.ylim(0,150)
plt.title('Predator Prey Relations')
plt.ylabel('Population (thousands)')
plt.xlabel('Year')
plt.xticks(rotation=30)
plt.legend(loc='best')
plt.show()


