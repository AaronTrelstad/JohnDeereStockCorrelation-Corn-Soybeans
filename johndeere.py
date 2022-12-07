import pandas as pd
from sklearn.metrics import r2_score
import math
import csv

jdstock = []
corn = []
soybean = []

with open('johndeere.csv') as f:
    reader = csv.reader(f)
    jdstock = list(reader)
with open('corn.csv') as f:
    reader = csv.reader(f)
    corn = list(reader)
with open('soybean.csv') as f:
    reader = csv.reader(f)
    soybeans = list(reader)
tjd = 0
t = 0
jd2 = 0
soy2 = 0
corn2 = 0
combine = 0
while True:
    input = input("Do you want to find John Deeres stock correlation with corn or soybeans? ")
    if input == 'corn':
        for i in range(0, len(jdstock)):
            tjd += float(jdstock[i][1])
            t += float(corn[i][1])
        meanjd = tjd / len(jdstock)
        mean = t / len(corn)
        for x in range(0, len(jdstock)):
            jd1 = float(jdstock[x][1]) - meanjd
            jd2 += (float(jdstock[x][1]) - meanjd)**2
            corn1 = float(corn[x][1]) - mean
            corn2 += (float(corn[x][1]) - mean)**2
            combine += jd1 * corn1
        r = (combine) / math.sqrt(jd2 * corn2)
        print(f"The correlation between John Deere stock price and corn is {round(r, 2)} and the r^2 value is {round(r**2, 2)}")
        break
    if input == 'soybeans':
        for i in range(0, len(jdstock)):
            tjd += float(jdstock[i][1])
            t += float(soybeans[i][1])
        meanjd = tjd / len(jdstock)
        mean = t / len(soybeans)
        for x in range(0, len(jdstock)):
            jd1 = float(jdstock[x][1]) - meanjd
            jd2 += (float(jdstock[x][1]) - meanjd)**2
            soy1 = float(soybeans[x][1]) - mean
            soy2 += (float(soybeans[x][1]) - mean)**2
            combine += jd1 * soy1
        r = (combine) / math.sqrt(jd2 * soy2)
        print(f"The correlation between John Deere stock price and soybeans is {round(r, 2)} and the r^2 value is {round(r**2, 2)}")
        break
