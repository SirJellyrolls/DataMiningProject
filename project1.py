import re as re
def cleanTitles():
    #/Users/darwyn/Downloads/pubmed_abstract.txt
    #/Users/darwyn/Downloads/iphone.txt
     finalFile=open("finalTitles.txt","x")
     fo=open(input())
     lineStart=re.compile('^\d+\.\s\w+') #match start of line to number._ to find new entries
     year=re.compile('\d{4}') #regex to check for for digits in a row use to check for publication data
     newLineTest=re.compile('^\s+')  #regex to see if line is blank or not
     nextFlag=False
     lf=False
     for line in fo:
        #these flags are used to check for start of new line
        startflag=lineStart.match(line)
        yearFlag=year.search(line)
        if startflag and yearFlag: #if this is a title line we want the info after it  
            nextFlag=True
            print(line)
            
        elif nextFlag and lf==False and newLineTest.search(line):#find line break after title mark it
            lf=True 
            
        elif nextFlag and lf : #if this is the data after title and line break
            
            print(line)
            finalFile.write(line)
            if newLineTest.search(line): #if the line is white space reset
                lf=False
                nextFlag=False
            
     print("done")
     finalFile.close()

def cleanArticles():
     #IMPORTANT to note spacecount is bc there are 2 spaces between the end of each article and start of a new one
    #/Users/darwyn/Downloads/pubmed_abstract.txt
    #/Users/darwyn/Downloads/iphone.txt
     finalFile=open("finalArticles.txt","w")
     fo=open(input())
     lineStart=re.compile('^\d+\.\s\w+')
     
     pmid=re.compile('^PMID:')
     
     titleFlag=False
     authorFlag=False
     lineFlag=False
     spacecount=0
     prev=""
     for line in fo:
         #not special checks for certain charcters
         notSpecial=line.__contains__("https:")==False and line.__contains__("©")==False and line.__contains__("DOI: ")==False and line.__contains__("PCID")==False and line.__contains__("PMCID: ")==False
         if line.__contains__("Author information"): #find we went over line with author info techincally 2nd step in process move this later
            authorFlag=True
            
         elif lineStart.search(line): #find if we went over the line that shows a new entry
             titleFlag=True
             
         elif line.isspace() and authorFlag: #if the line is a blank line update the blank line count
             lineFlag=True
             spacecount=spacecount+1 
         elif titleFlag and authorFlag and lineFlag and(line.isspace()==False) and notSpecial: #if we went over the title,author info, and new space
            if line.isspace():          #if the newline is also a blank space update
             spacecount=spacecount+1
            if pmid.search(line) or prev.__contains__("Copyright") or line.__contains__("Fang EF et al."): #make sure not a copyright line
                pass
            elif line.__contains__("Comment in") or prev.__contains__("Comment in") or line.__contains__("Originally published in the Journal of Medical Internet Research") : #make sure its not a comment in line
                pass
            else:
             #write line if valid line
             finalFile.write(line)
            if line.__contains__("Comment in"):# for comment in lines spacecount-1 becuase it is read like regular info
                spacecount=spacecount-1
            elif spacecount>1: #if there is more than one space article is done print line break to organize 
                    #reset all values back to default
                finalFile.write("\n") #print blank line 
                spacecount=0
                titleFlag=False
                lineFlag=False
                authorFlag=False
         prev=line #update prev line
     finalFile.close()#close file when done looping
if __name__=="__main__":
    print("enter file name:")
    cleanArticles()
    print("again")
    cleanTitles()
    print("done")
