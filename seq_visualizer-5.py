import base64
import requests
import pandas as pd
import difflib
from difflib import SequenceMatcher
import matplotlib.pyplot as plt
import numpy as np
from pandas import concat


_states = {'Alabama':{},'Alaska':{},'Arizona':{},'Arkansas':{},'California':{},'Colorado':{},
        'Connecticut':{},'Delaware':{},'Florida':{},'Georgia':{},'Hawaii':{},'Idaho':{},
        'Illinois':{},'Indiana':{},'Iowa':{},'Kansas':{},'Kentucky':{},'Louisiana':{},
        'Maine':{}, 'Maryland':{},'Massachusetts':{},'Michigan':{},'Minnesota':{},
        'Mississippi':{}, 'Missouri':{},'Montana':{},'Nebraska':{},'Nevada':{},
        'New Hampshire':{},'New Jersey':{},'New Mexico':{},'New York':{},
        'North Carolina':{},'North Dakota':{},'Ohio':{},
        'Oklahoma':{},'Oregon':{},'Pennsylvania':{},'Rhode Island':{},
        'South  Carolina':{},'South Dakota':{},'Tennessee':{},'Texas':{},'Utah':{},
        'Vermont':{},'Virginia':{},'Washington':{},'West Virginia':{},
        'Wisconsin':{},'Wyoming':{}}
stateslist = list(_states.keys())
#print(stateslist)


#url = 'https://api.github.com/repos/{user}/{repo_name}/contents/{path_to_file}
def returnYearStrains(year):
    """return predicted strins per year per state"""
    aaron_s = 'Aaron\'sBranch/Results/'
    url = 'https://raw.github.com/aaroncvega123/383Project1/' + aaron_s
    #aaron_s = 'aaroncvega123/383Project1/contents/tree/Aaron\'sBranch/Results/'
    #url = 'https://api.github.com/repos' + aaron_s
    strains = []

    for state in stateslist:
        fname = '_'.join([str(year), state, 'result.txt'])
        url2 = url + fname
        #print(url)

        r = requests.get(url2)
        strains.append(r.text)
    return strains


def getAbundantStrain(year):
    """return most abundant strain per year"""
    mohamed_s = 'MohamedBranch/Abundant%20Sequances/'
    url = 'https://raw.github.com/moabdi21/383Project1/' + mohamed_s
    url += 'Abundant_RAW_%d_H3N2_Strain.fasta' % (year)
    r = requests.get(url)
    data = r.text
    return data

#returns a list of ratio of the predicted strains being compared to the abundant strain for one specific year
def getRatio(year):
    """"ratio for predicted strain to most abundant in a given year
    per state"""
    ratioList = []
        #testing retrieval of abundant strain
    data_mohamed = getAbundantStrain(year)
    #printing the strain
    #print(data_mohamed)
    firstLine = str(data_mohamed).index('\n')
    data_mohamed = data_mohamed[firstLine:len(data_mohamed)]
    secondLine = data_mohamed.index('Human')
    data_mohamed = data_mohamed[secondLine+5:len(data_mohamed)]
    #print(data_mohamed)

    string_1 = data_mohamed
    list1 = []
    table = {'A':0, 'C':1, 'T':2, 'G':3} #Table keeps track if it's a nucluetide sequence.
    for i in string_1:
        if i in table: #makes sure it's a nucluetide/character A,C,T,& G
            list1.append(i)

    string_2 = returnYearStrains(year)
    #print(len(string_2))
    list2 = []
    for i in range(len(string_2)):    #runs the for loop by the number of predicted strain there are.
        currentPredictedStrain = string_2[i]
        for j in currentPredictedStrain:
            if j in table:  #makes sure it's a nucluetide/character A,C,T,& G
                list2.append(j)
        sm = difflib.SequenceMatcher(None, list1 ,list2)
        ratio = sm.ratio()
        ratioList.append(ratio) #adding the currect ration to the list.
        list2.clear() #want to clear to setup for the next strain.
    return ratioList



    fig = plt.figure()
    plt.title("Viral Realatedness Comparison between States")
    plt.xlabel('State Number')
    plt.ylabel('Relatedness')
    #plt.locatorparams(axis='y', nbins=10)
def plot(year, num):
    global fig

        x = []
        y = []


        f = open('ratio_' + str(year) + '.txt','r')
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

    for year in [2015, 2016, 2016]:
        plot(year, year)

    plt.show()



def main():
    ratioList1 = getRatio(2015)
    f = open('ratio_2015.txt','w')
    for i in range(len(ratioList1)):
        f.write(str(ratioList1[i]) + " : " + stateslist[i] + "\n")

    print('2015 ratios: ',ratioList1)

    f.close()
    print()

    ratioList1 = getRatio(2016)
    f = open('ratio_2016.txt','w')
    for i in range(len(ratioList1)):
        f.write(str(ratioList1[i]) + " : " + stateslist[i] + "\n")

    print('2016 ratios: ',ratioList1)

    f.close()
    print()

    ratioList1 = getRatio(2017)
    f = open('ratio_2017.txt','w')
    for i in range(len(ratioList1)):
        f.write(str(ratioList1[i]) + " : " + stateslist[i] + "\n")
    print('2017 ratios: ',ratioList1)

    f.close()


    #plot_2015 = plot(2015, int(round(x, -5)))
    #plt.show()
    #plot_2016 = plot(2016, int(round(x, -5)))
    #plt.show()
    #plot_2017 = plot(2017, int(round(x, -5)))
    #plt.show()

main()
