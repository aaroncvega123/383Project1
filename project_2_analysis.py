from __future__ import division

import difflib
import math
import pandas as pd
import os

from collections import Counter
from difflib import SequenceMatcher

states = {'Alabama':{},'Alaska':{},'Arizona':{},'Arkansas':{},'California':{},'Colorado':{},
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

#importing the datasets from each year to put in DataFrame
#need help only adding for each year to its seperate data DataFrame
#and annotating each seq with its state and year
#ex: all 2016 states in one 2016 data frame
def readfile(fileName):
    dataset = pd.read_txt('383Project1/Results/')
    data = []
    path = '.'
    f = [f for f in os.listdir(path) if os.path.isfile(f)]
    for f in files:
        with open (f, "r") as myfile:
            data.append(myfile.read())
    df = pd.DataFrame(data)
    #f = open(fileName,'w')
        #f.write(df)
    #f.close()

def seq_matching(fileName, data):
    data =[]
    #want to use this to compare most abundanrt  seq from year to each
    #seq in data frame
    #this is the example I found
    
    #s1=[1,8,3,9,4,9,3,8,1,2,3]
    #s2=[1,8,1,3,9,4,9,3,8,1,2,3]
    #sm = difflib.SequenceMatcher(None,s1,s2)
    #sm.ratio()
