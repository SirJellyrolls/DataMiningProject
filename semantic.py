import csv
import re
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#A:\Dowloads\finalArticles(1).txt
#P:\Fall2023Code\NotesFall2023\finalTitles.txt
def freq():
    #used to generated a text document of frequency of all words in a goven text document 
    finalFile=open("titleFreq.csv","x",encoding="utf8")
    print("Please input file name:")
    masterlist={}
    regex = re.compile('[^a-zA-Z]')  #used for normalization of words
    with open(input(),'r',encoding="utf8") as csv_file:
        articles=csv.reader(csv_file)
        for lines in articles:
            for word in lines:
                j=word.split(" ")
                for wordy in j:
                    newword=str.lower(regex.sub('', wordy)) # remove spaces from words to normalize
                    if newword in masterlist:
                        masterlist[newword]=masterlist.get(newword)+1
                    else:
                        masterlist[newword]=1
    
    for s in masterlist.items(): #write out the collection of word freq
        finalFile.write(s[0]+","+str(s[1])+"\n")
    finalFile.close()

def labelFiles():
    #used to label number each body of text in a document
    ff=open("labeldTitles.txt","x",encoding="utf8")
    ff.write("1\n")
    i=1
    blank=re.compile('^\s+')
    with open(input(),'r',encoding="utf8") as csv_file:
        for line in csv_file:
            if blank.match(line):
                i=i+1
                ff.write(str(i)+"\n")
            else:
                ff.write((line))

def semGen():
    semFile=open("semBod.csv","x",encoding="utf8")
    #generate a csv file with each body of text's semantic distance 
    f=open("bodyFreq.csv","r") #file with word freqeunecies 
    fdict=dict(csv.reader(f))
    xbar=0 
    for k,v in fdict.items():
        xsquare=int(v)*int(v)
        xbar=xbar+xsquare
    xbar=xbar**(.5) #square root of sum of all values squared 

    testBod=open("testBod.txt","x",encoding="utf8")
    i=2
    testBod.write("1\n")
    
    with open(input(),'r',encoding="utf8") as csv_file: ##
     blank=re.compile('^\s+')
     #articles=csv.reader(csv_file)
     blankcount=0 #0 write to array
     curP={}
     semDistances=set()
     regex = re.compile('[^a-zA-Z]')
     jh=1 
     for line in csv_file:
       # print(line)
       # print("ss")
        #if len(line)>0:
            #blankcount=0
            
        if blank.match(line): #if we have a new line AKA different article calculate semDist for y
            testBod.write(str(jh)+"\n")
            i+=1
            blankcount=1
            #print("\n")
            ybar=0
            for k,v in curP.items():
                v2=v*v
                ybar+=(v2)
            ybar=ybar**(.5)
            #print(ybar)

            xdoty=0
            for k,v in fdict.items():
                if curP.__contains__(k):
                    xdoty=xdoty+(int(v)*int(curP.get(k)))
            
            xybar=xbar*ybar
            if ybar != 0:
                finalNumber=xdoty/xybar
            else:
                finalNumber=0
            semDistances.add(finalNumber)
            
            semFile.write(str(jh)+","+str(finalNumber)+"\n")
            jh+=1
            curP.clear()

        else:
            testBod.write(line)
            
            j=line.split(" ")
            print(j)
            for wordy in j:
                newword=str.lower(regex.sub('', wordy))
                if newword in curP:
                    curP[newword]=curP.get(newword)+1
                else:
                    curP[newword]=1
        #if blankcount==0:
        """
        for word in line: 
            #print(word)
            j=word.split(" ")
            for wordy in j:
                newword=str.lower(regex.sub('', wordy))
                if newword in curP:
                    curP[newword]=curP.get(newword)+1
                else:
                    curP[newword]=1
                    """

    #print(curP)
    #print(paras)
    
    semFile.close
    testBod.close
    """
    for k in semDistances:
        semFile.write(str(i)+","+str(k)+"\n")
        i=i+1
    print(semDistances)
    semFile.close
    testBod.close
    """
#now that word list is generated you can find semantic of all compared to sample

#/Users/darwyn/git/NotesFall2023/DataMining/finalArticles.txt
#/Users/darwyn/git/NotesFall2023/finalArticles.txt
def plotData():
    df=pd.read_csv('semBod.csv')
    df.columns =['article number','sematnic distance']
    plt.xlabel("Article Number")
    plt.ylabel("semantic distance")
    fig, ax=plt.subplots()
    ax.axhspan(0,(0.4677666160510401+0.700903015954268)/2,facecolor='red',alpha=.5)
    plt.axhline(y=0.4677666160510401,color='black')
    ax.axhspan((0.4677666160510401+.700903015954268)/2,(0.700903015954268+0.9016866481827526)/2,facecolor='blue',alpha=.5)
    plt.axhline(y=0.700903015954268,color='black')
    ax.axhspan((0.700903015954268+0.9016866481827526)/2,1,facecolor='green',alpha=.5)
    plt.axhline(y=0.9016866481827526,color='black')
    plt.title("Semantic distance of body paragraphs")
    df.plot(kind="scatter",x="article number",y="sematnic distance",ax=ax)
    plt.tight_layout()
    plt.xticks(np.arange(0, 400, 10),rotation=90)
    plt.show()
    max=.957
    mid=.824
    min=.6
    getRanges(df,max,mid,min)


def plotDataTitles():
    df=pd.read_csv('semanticTitles.csv')
    df.columns =['Title number','sematnic distance']
    fig, ax=plt.subplots()
    ax.axhspan(0,(0.1645418916974338+0.3922124769491012)/2,facecolor='red',alpha=.5)
    plt.axhline(y=0.1645418916974338,color='black')
    ax.axhspan((0.1645418916974338+0.3922124769491012)/2,(0.6007903242452202+0.3922124769491012)/2,facecolor='blue',alpha=.5)
    plt.axhline(y=0.3922124769491012,color='black')
    ax.axhspan((0.6007903242452202+0.3922124769491012)/2,1,facecolor='green',alpha=.5)
    plt.axhline(y=0.6007903242452202,color='black')
    df.plot(kind="scatter",x="Title number",y="sematnic distance",ax=ax)
    plt.title("Semantic Distance of Titles")
    plt.tight_layout()
    plt.xticks(np.arange(0, 400, 10),rotation=90)
    plt.show()
    semDist=df['sematnic distance'].tolist()
    #print(df.describe(include='all'))
    max=.8
    mid=.4
    min=.074
    getRanges(df,max,mid,min)
   
def plotDataFunctional():
    df=pd.read_csv(input("Insert file name: "))
    df.columns =['Title number','sematnic distance']
    semDist=df['sematnic distance'].tolist()
    
    mid=np.average(semDist)
    max=mid*1.25
    min=mid*.65
    toplist={}
    midlist={}
    botlist={}
    #first pass to set inital values
    initCount=1
    for value in semDist:
        topDist=abs(value-max)
        midDist=abs(value-mid)
        minDist=abs(value-min)
    #case 1 highest value is closest
        if topDist<midDist and topDist<minDist:
            toplist[initCount]=value
            initCount+=1
        elif minDist<topDist and minDist<midDist:
            botlist[initCount]=value
            initCount+=1
        else:
            midlist[initCount]=value
            initCount+=1
   # print(len(toplist))
    #print(len(midlist))
    #print(len(botlist))
    newMax=avgOf(toplist)
    newMid=avgOf(midlist)
    newMin=avgOf(botlist)
    newTL={}
    newML={}
    newBL={}
    while((newMax!=max)or(newMid!=mid)or(newMin!=min)):
        #update cluster
        max=newMax
        mid=newMid
        min=newMin
        for key , value in toplist.items():
         topDist=abs(value-max)
         midDist=abs(value-mid)
         minDist=abs(value-min)
    #case 1 highest value is closest
         if topDist<midDist and topDist<minDist:
            newTL[key]=value
         elif minDist<topDist and minDist<midDist:
            newBL[initCount]=value
         else:
            newML[initCount]=value
        for key , value in midlist.items():
         topDist=abs(value-max)
         midDist=abs(value-mid)
         minDist=abs(value-min)
    #case 1 highest value is closest
         if topDist<midDist and topDist<minDist:
            newTL[key]=value
         elif minDist<topDist and minDist<midDist:
            newBL[initCount]=value
         else:
            newML[initCount]=value
        for key , value in botlist.items():
         topDist=abs(value-max)
         midDist=abs(value-mid)
         minDist=abs(value-min)
    #case 1 highest value is closest
         if topDist<midDist and topDist<minDist:
            newTL[key]=value
         elif minDist<topDist and minDist<midDist:
            newBL[initCount]=value
         else:
            newML[initCount]=value
        newMax=avgOf(toplist)
        newMid=avgOf(midlist)
        newMin=avgOf(botlist)
        toplist=newTL
        midlist=newML
        botlist=newBL
        newMax=avgOf(toplist)
        newMid=avgOf(midlist)
        newMin=avgOf(botlist)
    print("\n")
    print(newMax)
    print(newMid)
    print(newMin)
    fig, ax=plt.subplots()
    ax.axhspan(0,newMin,facecolor='red',alpha=.5)
    ax.axhspan(newMin,newMid,facecolor='blue',alpha=.5)
    ax.axhspan(newMid,1,facecolor='green',alpha=.5)
    df.plot(kind="scatter",x="Title number",y="sematnic distance",ax=ax)
    plt.show()
    pass
    
def avgOf(someList)->float:
    avgFloat=float(0.0)
    size=len(someList)
    for key, value in someList.items():
        avgFloat+=value
        
    avgFloat=avgFloat/size
    #print(avgFloat)
    
    return float(avgFloat)

def plotFreqWords(): 
   plt.rcParams['font.size']=7
   df=pd.read_csv("bodyFreq.csv")
   df.columns=['Word','Freq']
   df=df.sort_values(by='Freq',ascending=False)
   df=df.drop(df[df['Freq']==16610].index)
   top=df.head(30)
   df.describe()
   print('s')
   x=top['Word']
   y=top['Freq']
   plt.xlabel("Words")
   plt.ylabel("# of occuerences")
   plt.title("Freq of words within all Body paragraphs")
   plt.bar(x,y)
   plt.xticks(x,x,rotation=90)
   plt.tight_layout()
   #ax=plt.gca()
   print(x)
   #plt.bar(top['Word'],top['Freq'])
   plt.show()

def plotFreqTitle(): 
   plt.rcParams['font.size']=7
   df=pd.read_csv("titleFreq.csv")
   df.columns=['Word','Freq']
   df=df.sort_values(by='Freq',ascending=False)
   df=df.drop(df[df['Freq']==490].index)
   top=df.head(30)
   df.describe()
   print('s')
   x=top['Word']
   y=top['Freq']
   plt.title("Freq of words within all titles")
   plt.ylabel("# of occuerences")
   plt.xlabel("Words")
   plt.bar(x,y)
   plt.xticks(x,x,rotation=90)
   plt.tight_layout()
   #ax=plt.gca()
   print(x)
   #plt.bar(top['Word'],top['Freq'])
   print("hh")
   plt.show()

def getRanges(df,mt,mm,ml):
    #takes input as a dataframe
    semDist=df['sematnic distance'].tolist()
    #print(df.describe(include='all'))
    max=mt
    mid=mm
    min=ml
    toplist={}
    midlist={}
    botlist={}
    #first pass to set inital values
    initCount=1
    for value in semDist:
        topDist=abs(value-max)
        midDist=abs(value-mid)
        minDist=abs(value-min)
    #case 1 highest value is closest
        if topDist<midDist and topDist<minDist:
            toplist[initCount]=value
            initCount+=1
        elif minDist<topDist and minDist<midDist:
            botlist[initCount]=value
            initCount+=1
        else:
            midlist[initCount]=value
            initCount+=1
   # print(len(toplist))
    #print(len(midlist))
    #print(len(botlist))
    newMax=avgOf(toplist)
    newMid=avgOf(midlist)
    newMin=avgOf(botlist)
    newTL={}
    newML={}
    newBL={}
    while((newMax!=max)or(newMid!=mid)or(newMin!=min)):
        #update cluster
        max=newMax
        mid=newMid
        min=newMin
        for key , value in toplist.items():
         topDist=abs(value-max)
         midDist=abs(value-mid)
         minDist=abs(value-min)
    #case 1 highest value is closest
         if topDist<midDist and topDist<minDist:
            newTL[key]=value
         elif minDist<topDist and minDist<midDist:
            newBL[initCount]=value
         else:
            newML[initCount]=value
        for key , value in midlist.items():
         topDist=abs(value-max)
         midDist=abs(value-mid)
         minDist=abs(value-min)
    #case 1 highest value is closest
         if topDist<midDist and topDist<minDist:
            newTL[key]=value
         elif minDist<topDist and minDist<midDist:
            newBL[initCount]=value
         else:
            newML[initCount]=value
        for key , value in botlist.items():
         topDist=abs(value-max)
         midDist=abs(value-mid)
         minDist=abs(value-min)
    #case 1 highest value is closest
         if topDist<midDist and topDist<minDist:
            newTL[key]=value
         elif minDist<topDist and minDist<midDist:
            newBL[initCount]=value
         else:
            newML[initCount]=value
        newMax=avgOf(toplist)
        newMid=avgOf(midlist)
        newMin=avgOf(botlist)
        toplist=newTL
        midlist=newML
        botlist=newBL
        newMax=avgOf(toplist)
        newMid=avgOf(midlist)
        newMin=avgOf(botlist)
    print("\n")
    print(newMax)
    print(newMid)
    print(newMin)


if __name__=="__main__":
    print()
    #freq()
    #labelFiles()
    #semGen()
   # plotDataFunctional()
   # plotFreqWords()
    plotDataTitles()
    #plotFreqTitle()
    plotData()
    