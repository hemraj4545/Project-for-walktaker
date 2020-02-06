import csv
import pylab as pb
import pandas as pd

def average_time_heel(name):
    heel_time = 0
    df1 = pd.read_csv(name)
    for i in range(len(df1)):
        heel_time = heel_time + df1['Time'][i]    
    
    heel_avg = heel_time/len(df1)
    return heel_avg

    if(len(df1)>50):
        lines = []
        with open("dataTimeHeel.csv",'r') as file:
            r = csv.reader(file)
            for i in r:
                lines.append(i)
                for j in i:
                    lines.remove(i)
            
        with open('dataTimeHeel.csv', 'w') as w:
            writer = csv.writer(w)
            writer.writerows(lines)

def average_time_toe(name):
    toe_time = 0
    df2 = pd.read_csv(name)
    for i in range(len(df2)):
        toe_time = toe_time + df2['Time'][i]    
    
    toe_avg = toe_time/len(df2)
    return toe_avg


    if(len(df2)>50):
        lines = []
        with open("dataTimeToe.csv",'r') as file:
            r = csv.reader(file)
            for i in r:
                lines.append(i)
                for j in i:
                    lines.remove(i)
            
        with open('dataTimeToe.csv', 'w') as w:
            writer = csv.writer(w)
            writer.writerows(lines)
            
x = average_time_heel("dataTimeHeel.csv")            
y = average_time_toe("dataTimeToe.csv")

with open("averageTime.csv",'w',newline='') as file:
    w = csv.writer(file)
    w.writerow(["Heel","Toe"])
    w.writerow([x,y])
