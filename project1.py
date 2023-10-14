import re as re
def cleanTitles():
    #FIX OFF BY ONE ERROR

    #/Users/darwyn/Downloads/pubmed_abstract.txt
    #/Users/darwyn/Downloads/iphone.txt
     fo=open(input())
     lineStart=re.compile('^\d+\.\s\w+\s+') #match start of line to number._ to find new entries
     year=re.compile('\d{4}') #regex to check for for digits in a row use to check for publication data
     newLineTest=re.compile('^\s+')  #regex to see if line is blank or not
     nextFlag=False
     lf=False
     for line in fo:
        #these flags are used to find determine new article entry
        startflag=lineStart.search(line)
        yearFlag=year.search(line)
        if startflag and yearFlag: #if this is a title line we want the info after it  
            nextFlag=True
            
        elif nextFlag and lf==False and newLineTest.search(line):#find line break after title mark it
            lf=True 
            
        elif nextFlag and lf : #if this is the data after title and line break
            print(line)
            if newLineTest.search(line): #if the line is white space reset
                lf=False
                nextFlag=False
     print("done")

def cleanArticles():
     #IMPORTANT to note spacecount is bc there are 2 spaces between the end of each article and start of a new one

    #/Users/darwyn/Downloads/pubmed_abstract.txt
    #/Users/darwyn/Downloads/iphone.txt
     fo=open(input())
     lineStart=re.compile('^\d+\.\s\w+\s+')
     year=re.compile('\d{4}')
     titleFlag=False
     authorFlag=False
     lineFlag=False
     spacecount=0
     for line in fo:
         if line.__contains__("Author information"): #find we went over line with author info techincally 2nd step in process move this later
            authorFlag=True
            
         elif lineStart.search(line): #find if we went over the line that shows a new entry
             titleFlag=True
             
         elif line.isspace() and authorFlag: #if the line is a blank line update the blank line count
             lineFlag=True
             spacecount=spacecount+1

         elif titleFlag and authorFlag and lineFlag and(line.isspace()==False): #if we went over the title,author info, and new space
            if line.isspace():          #if the newline is also a blank space update
             spacecount=spacecount+1
            print(line)

            if spacecount>1: #if there is more than one space article is done print line break to organize 
                print()     #reset all values back to default
                spacecount=0
                titleFlag=False
                lineFlag=False
                authorFlag=False

if __name__=="__main__":
    cleanArticles()
