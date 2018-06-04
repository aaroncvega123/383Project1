import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
plt.title("Viral Realatedness Comparison between States")
plt.xlabel('State Number')
plt.ylabel('Relatedness')
#plt.locatorparams(axis='y', nbins=10)

def plot(year, num):
    global fig

    x = []
    y = []


    #f = open('ratio_' + str(year) + '.txt','r')
    f = open('ratio_2017.txt','r')
    stateNumber = 1
    for line in f:
        current_line = line.split(":")
        x.append(stateNumber)
        y.append(current_line[0])
        stateNumber = stateNumber + 1

    #x = [row.split(' ')[1] for row in data]
    #y = [row.split(' ')[0] for row  in data]

    ax1 = fig.add_subplot(111)

    ax1.plot(x,y, c='g', label=(year))


    leg = ax1.legend()

for year in [2017]:
    plot(year, year)

plt.show()
