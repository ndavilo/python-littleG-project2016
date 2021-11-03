def errorcheck():
    try: import re;
    except:
        while 1: print 'error importing re'
    try: import urllib2;
    except:
        while 1: print 'error importing urllib2'
    try: from BeautifulSoup import BeautifulSoup;
    except:
        while 1: print 'error importing BeautifulSoup'
    try: from playsound import playsound;
    except:
        while 1: print 'error importing playsound'
    try:
        little_gods_file = open('LittleG file\problemstxt.txt', 'r')
        myStringProblem = little_gods_file.read()
    except:
        while 1: print 'error with LittleG file\problemstxt.txt'

    try:
        little_gods_file = open('LittleG file\problemstxt.txt', 'r')
        line = little_gods_file.readline()
    except:
        while 1: print 'error with LittleG file\solutionstxt.txt'

    try:
        myStringtime = ''
        littleGtime = open('LittleG file\littlegdate.txt', 'r')
        myStringtime = littleGtime.read()
        littleGtime.close()
    except:
        while 1: print 'error with LittleG file\littlegdate.txt'

    try:
        myStringtime = ''
        littleGtime = open('LittleG file\linking.txt', 'r')
        myStringtime = littleGtime.read()
        littleGtime.close()
    except:
        while 1: print 'error with LittleG file\linking.txt'




S2 = '!!!NO SOLUTION YET !!!'
check = 'hungry'
caps = "([A-Z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"

def split_into_sentences(check):
    text = checkOnline(check)
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + caps + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(caps + "[.]" + caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + caps + "[.]"," \\1<prd>",text)
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
        
    swrite = []
    for s in sentences:
        try:
            s = s.lower()
            sen = s
            if(len(sen.strip())) <= 40:
                del(s)
            if(len(sen.strip())) > 50:
                if(len(sen.strip())) < 150:
                    swrite.append(s + "\n")
        except:
            del(s)
   
    return swrite

def checkOnline(check):
    try:
        url = 'https://en.wikipedia.org/wiki/'+check
        
        playsound('LittleG sounds\wait-a-minute.wav')
        
        print '\n \n CHECKING ONLINE...\n\n'
        response = urllib2.urlopen(url)
        webContent = response.read()
        soup = BeautifulSoup(webContent)
        urlFile = soup.getText()
        return urlFile

    except:
        return 'NONE'

    


def printAllP(n): # function to print all problems
    little_gods_file = open('LittleG file\problemstxt.txt', 'r')
    listProblem = little_gods_file.readlines() # to read  the file line by line
    little_gods_file.close()
    little_gods_file = open('LittleG file\solutionstxt.txt', 'r')
    listSolution = little_gods_file.readlines() # to read  the file line by line
    little_gods_file.close()
    if n == 1: return str((len(listProblem)) - 1)
    print listProblem
    for Print in listProblem:
        number = listProblem.index(Print) 
        num = str(number)
        print "Problem ("+ num +") " + Print + " \nSolution ("+ num +") " + listSolution[number]
        num2 = str((len(listProblem)) - 1)
        print " "
    print " TOTAL OF " +num2+" PROBLEMS"
    print " "
    print " "

def deletePros(): # function to del or edit problems
    a = raw_input("TYPE PROBLEM/'S NUM YOU WISH TO DEL (OR) TYPE BACK TO SKIP:  ")
    alow =a.lower()
    if alow == 'back': return
    try:        #this is to make sure your program dont crash when you enter a non int value
        dl = int(a)
        dl = dl
    except:
        print 'ENTER NUMBER NEXT TIME'
        return
    editP = raw_input("TYPE THE NEW PROBLEM (OR) TYPE BACK TO STOP (OR) TYPE DEL TO DELETE:  ")
    editP = editP.lower()
    if editP == 'back': return
    
    little_gods_file = open("LittleG file\problemstxt.txt","r")
    listProblem = little_gods_file.readlines()
    little_gods_file.close()

    little_gods_file = open("LittleG file\solutionstxt.txt","r")
    listSolution = little_gods_file.readlines()
    little_gods_file.close()

    print 'YOU WANT TO EDIT?: ' + listProblem[dl]
                  
    if editP == "del":
        del listProblem[dl]
        del listSolution[dl]
        
    else:listProblem[dl] = editP+ "\n "
       
    little_gods_file = open("LittleG file\problemstxt.txt","w")
    little_gods_file.writelines(listProblem)
    little_gods_file.close()
    little_gods_file = open("LittleG file\solutionstxt.txt","w")
    little_gods_file.writelines(listSolution)
    little_gods_file.close()
    if editP != "del":
        print listProblem
        deleteSolut()
    return listProblem, listSolution

def deleteSolut():
    a = raw_input("TYPE SOLUTION/'S NUM YOU WISH TO DEL (OR) TYPE BACK TO SKIP:  \n \n ")
    alow =a.lower()
    if alow == 'back': return
    try:        #this is to make sure your program dont crash when you enter a non int value
        dl = int(a)
        dl = dl
    except:
        print 'ENTER NUMBER NEXT TIME'
        return
    
    editS = raw_input("TYPE THE NEW SOLUTION (OR)TYPE BACK TO STOP (OR) TYPE DEL TO DELETE:  \n \n ")
    editS = editS.lower()
    if editS == 'back': return

    little_gods_file = open("LittleG file\solutionstxt.txt","r")
    listSolution = little_gods_file.readlines()
    little_gods_file.close()
    print 'YOU WANT TO EDIT?: ' + listSolution[dl]
              
    if editS == "del":
        editS = '!!!NO SOLUTION YET !!!'
   
    listSolution[dl] = editS+ "\n "
       
    little_gods_file = open("LittleG file\solutionstxt.txt","w")
    little_gods_file.writelines(listSolution)
    little_gods_file.close()
    print listSolution
    return listSolution

def saving(myStringProblem, myStringSolution):
    little_gods_file = open("LittleG file\problemstxt.txt","w")
    little_gods_file.write(myStringProblem)
    little_gods_file.close()
    little_gods_file = open("LittleG file\solutionstxt.txt","w")
    little_gods_file.write(myStringSolution)
    little_gods_file.close()
    return myStringProblem , myStringSolution



def addKeyWords(add):
    if add == 'checking':
        return keywords
    if add != 'checking':
        keywords.append(add)
        return keywords
        

#class for checking words
    
class Checking:
    def __init__(self, words , F):
        self.words = words
        self.F = F
        
    def checkwordsPercentage(self, check):
        # checking the percentage match of sentence
        maxscore = []
        if self.F == 1:
            inFile = open('LittleG file\problemstxt.txt', 'r')
            oldP = inFile.readlines()
            inFile.close()
            inFile = open('LittleG file\solutionstxt.txt', 'r')
            oldP2 = inFile.readlines()
            inFile.close()
        if self.F == 2:
            inFile = open('LittleG file\solutionstxt.txt', 'r')
            oldP = inFile.readlines()
            inFile.close()
            inFile = open('LittleG file\problemstxt.txt', 'r')
            oldP2 = inFile.readlines()
            inFile.close()
        if self.F == 3:
            oldP = split_into_sentences(check)
        if self.F == 4:
            inFile = open('LittleG file\problemstxt.txt', 'r')
            oldP = inFile.readlines()
            inFile.close()
            inFile = open('LittleG file\solutionstxt.txt', 'r')
            oldP2 = inFile.readlines()
            inFile.close()
           
        score_old = 0    
        for ch in range(len(oldP)):
            
                oldP[ch] = oldP[ch].rstrip()
                oldP[ch] = oldP[ch].strip()
                checkP = self.words.strip().rstrip()

                import difflib
                score = difflib.SequenceMatcher(None,oldP[ch].lower(),checkP.lower()).ratio()
                score = score*100
                maxscore.append(score)

               
                if score >= 50:
                    if self.F == 1:
                        print str(score)+'%'
                        print "Related to:  "
                        print 'NO ('+ str(ch) +'): ' + oldP[ch]
                        if score >= 60:
                            num1 = int(printAllP(1))+1
                            print linking(num1, ch)
                        print ""
                        print "Solution:  "
                        print 'NO ('+ str(ch) +'): ' + oldP2[ch]
                       
                        print ""
                    if self.F == 2:
                        print str(score)+'%'
                        print "Related to:  "
                        print 'NO ('+ str(ch) +'): ' + oldP[ch]
                        print ""
                        print "Problem:  "
                        print 'NO ('+ str(ch) +'): ' + oldP2[ch]
                        print ""
                    if self.F == 3:
                        print str(score)+'%'
                        print "ONLINE SOLUTIONS:  "
                        print 'NO ('+ str(ch) +'): ' + oldP[ch]
                        print ""
                        print " DO YOU WANT TO SAVE ANY?  "
                    if self.F == 4:
                        if (score >= score_old):
                            S2 = oldP2[ch]
                            score_old = score
                            print "Solution:  "
                            print S2
                            print ""
                       
                 
                
       

        try:
            if self.F == 4:
                num2 = ch
                num1 = int(printAllP(1))+1
                print linking(num1, ch)
                
                return S2
            return max(maxscore)
        except:
            return 0
    
    def checkingWords(self):
        keywords = addKeyWords('checking')
        checkP = self.words.split(' ')
        for checkP in checkP:
            for keyword in keywords:
                if keyword == checkP:
                    k = raw_input("ARE YOU SURE YOU WANT "+ str(keyword).upper()+ "? IF NO: JUST PRESS ONLY ENTER, IF YES: TYPE IT AGAIN AND ENTER \n: ")
                    k=k.lower()
                    if k == 'no':
                        return self.P
                    if k == keyword:
                        return keyword
        checkP = self.words.split(' ')
        ppp = ''
        ch_next = 0
        for checkP in checkP:
            
            if checkP == 'date':
                checkP = 'date ['+dateD()+']'
            if checkP == 'time':
                checkP = 'time ['+timeT()+']'
            if checkP == 'today':
                checkP = 'today ['+dateD()+' '+ timeT()+']'
            if checkP == 'day':
                checkP = 'day ['+dateD()+']'
            if checkP == 'i':
                ch_next = 1
                checkP = 'davilo'
            if checkP == 'am':
                if ch_next == 1:
                    checkP = "is"
                    ch_next = 0
            if checkP == 'my':
                checkP = "davilo's"   

            ppp = ppp+' '+ checkP
        print ppp
                
        return ppp

def linking(num1, num2):
        inFile = open('LittleG file\linking.txt', 'r')
        oldcheck = inFile.readlines()
        inFile.close()
        oldcheckP=''
        score_old = 0    
        for ch in range(len(oldcheck)):
               oldcheckP = oldcheckP+oldcheck[ch]
               
        oldcheck = oldcheckP.split('\n')
        check_num1 = 0
        check_num2 = 0
        num1 = str(num1)
        num2 = str(num2)
        for ch in range(len(oldcheck)):
            
            oldcheck[ch] = oldcheck[ch].replace(':', ' ')
            oldcheck[ch] = oldcheck[ch].split(' ')
            for chh in oldcheck[ch]:
               
                if num1 == chh:
                    check_num1 = 1
                    len_num1 = ch
                if num2 == chh:
                    check_num2 = 1
                    len_num2 = ch
                    
        if(check_num1 == 1 and check_num2 == 1):
            if(len_num1 == len_num2):
                return oldcheck[len_num1]
            if(len_num1 != len_num2):
                inFile = open('LittleG file\linking.txt', 'r')
                oldcheck = inFile.readlines()
                inFile.close()
                oldcheck[len_num1] = oldcheck[len_num1].replace('\n', ':')+ oldcheck[len_num2].replace('\n', '')+'\n'
                del oldcheck[len_num2]
                inFile = open('LittleG file\linking.txt', 'w')
                inFile.writelines(oldcheck)
                inFile.close()
                return oldcheck[len_num1]
        if(check_num1 == 1 and check_num2 != 1):
            inFile = open('LittleG file\linking.txt', 'r')
            oldcheck = inFile.readlines()
            inFile.close()
            oldcheck[len_num1] = oldcheck[len_num1].replace('\n', ':')+ num2+'\n'
            inFile = open('LittleG file\linking.txt', 'w')
            inFile.writelines(oldcheck)
            inFile.close()
            return oldcheck[len_num1]
        if(check_num1 != 1 and check_num2 == 1):
            inFile = open('LittleG file\linking.txt', 'r')
            oldcheck = inFile.readlines()
            inFile.close()
            oldcheck[len_num2] = oldcheck[len_num2].replace('\n', ':')+ num1+'\n'
            inFile = open('LittleG file\linking.txt', 'w')
            inFile.writelines(oldcheck)
            inFile.close()
            return oldcheck[len_num2]
        if(check_num1 != 1 and check_num2 != 1):
            inFile = open('LittleG file\linking.txt', 'r')
            oldcheck = inFile.readlines()
            inFile.close()
            oldcheck.append('\n'+num1 +':'+ num2+'\n')
            inFile = open('LittleG file\linking.txt', 'w')
            inFile.writelines(oldcheck)
            inFile.close()
            return 'ok'
        
def timeT():
    import time
    return (time.strftime("%I:%M:%S"))
def dateD():
    import time
    return (time.strftime("%d:%m:%Y"))
def timediff():
    import time
    get_old_time = open('LittleG file\littlegdate.txt', 'r')
    Data = get_old_time.read()
    get_old_time.close

    oldTimeDate = Data.split(' ')
    counttime =0
    for oldTimeD in oldTimeDate:
        if counttime == 0:
            oldyear = int(oldTimeD)
        if counttime == 1:
            oldmonth = int(oldTimeD)
        if counttime == 2:
            oldday = int(oldTimeD)
        if counttime == 3:
            oldhour = int(oldTimeD)
        if counttime == 4:
            oldmin = int(oldTimeD)
        if counttime == 5:
            oldsec = int(oldTimeD)
        counttime = counttime+1
    minsec=0
    hourmin=0
    dayhour=0
    monthday=0
    yearmonth=0
    
    secdiff = int(time.strftime("%S"))-oldsec
    if secdiff < 0: secdiff = 60 + secdiff; minsec=-1
    mindiff = int(time.strftime("%M"))-oldmin + minsec
    if mindiff < 0: mindiff = 60 + mindiff; hourmin=-1
    hourdiff = int(time.strftime("%H"))-oldhour + hourmin
    if hourdiff < 0: hourdiff = 24 + hourdiff; dayhour=-1
    daydiff = int(time.strftime("%d"))-oldday + dayhour
    
    datediff = str(int(time.strftime("%Y"))-oldyear) + ' years. ' + str(int(time.strftime("%m"))-oldmonth)+' months. '+str(daydiff)+' days.'
    timediff = str(hourdiff)+ ' hours. '+str(mindiff)+' minutes. '+str(secdiff)+ ' seconds. '

    timedate = time.strftime("%Y %m %d")+' '+time.strftime("%H %M %S")
    get_old_time = open('LittleG file\littlegdate.txt', 'w')
    Data = get_old_time.write(timedate)
    get_old_time.close

    return datediff, timediff

def action():
    while 1:
        time.sleep(5)
        playsound('LittleG sounds\go-head.wav')

class knowledge_data:
    
    def __init__(self, check , F):
        self.F = F
        self.check = check

    def filenames(self):
        dataout =[]
        data =''
        openfile = open('knowledge data\kfiles.txt', 'r')
        data = openfile.read()
        while data:
            dataout.append(data)
            data = openfile.read()

        openfile.close()
        return dataout
    
    def selectfile(self, fileopen, inout, data2):
        string_filename = 'knowledge data\k'+ str(fileopen)+'.txt'
        dataout =[]
        data =''
        openfile = open(string_filename, 'r')
        data = openfile.read()
        while data:
            dataout.append(data)
            data = openfile.read()
        
        openfile.close()
        if inout == 1:
            for s in dataout:
                s = s.split('\n')
                for s in s:
                    if data2 == s.lower():
                        return 'exist'
                if data2 != s.lower():
                    dataout.append(str(data2)+'\n')
                    openfile = open(string_filename, 'w')
                    data = openfile.writelines(dataout)
                    openfile.close()
                    return
        return dataout

    def check_knowledge(self):
        check = knowledge_data(self.check, self.F)
        filename2 = check.filenames()
        for f in filename2:
            f=f.split('\n')
            for f in f:
                dataname = f
                check = knowledge_data(self.check, self.F)
                selectedfiles = check.selectfile(f, 0, '')
                                
                for s in selectedfiles:
                    s = s.split('\n')
                    for s in s:
                        if self.check == s.lower():
                            return str(dataname)+' '+ str(self.check) 
            
                        
    def add_knowledge(self, inputfile, inputword):
        check = knowledge_data(self.check, self.F)
        filename2 = check.filenames()
        for f in filename2:
            f=f.split('\n')
            for f in f:
                if inputfile == f:
                    check = knowledge_data(self.check, self.F)
                    selectedfiles = check.selectfile(inputfile, 1, inputword)
                    return
            else:
                print 'NOT A VALID FILE NAME '
                print check.filenames()
                return

def knowledge(words):
    words = words.split(' ')
    for word in words:
        check = knowledge_data(word, 1)
        print check.check_knowledge()

def history(P):
    callP = Checking(P, 1)
    checkP = callP.checkwordsPercentage(checkK)
    print str(checkP) +'%'


def informations():
    print 'TYPE /" ALL/" AND PRESS ENTER TO SHOW ALL PROBLEMS AND SOLUTIONS  '
    
    print " "
        
    print 'TYPE /" DELP/" AND PRESS ENTER TO DEL PROBLEMS '
   
    print " "

    print 'TYPE /" DELS/" AND PRESS ENTER TO DEL SOLUTIONS '
   
    print " "
    print 'TYPE /" BACK/" AND PRESS ENTER TO GO BACK '

    print " "
    print 'TYPE /" QUIT /" AND PRESS ENTER TO QUIT '

    print " "
    print 'TYPE /" PRINT /" AND PRESS ENTER TO PRINT ONE PROBLEM STORED IN THE SYSTEM'
    
    print " "
    print "TYPE MAIN.py AND ENTER TO RUN OTHER PROGRAMS"

    print " "
    print " "
    return

        
def inputP(): return raw_input("Enter The Problem and press 'ENTER':  ").lower().strip().rstrip()

def inputK(): return raw_input("Enter The /keyword AND PRESS ENTER / FOR ONLINE CHECK /OR/ PRESS ONLY ENTER:  ").lower().strip().rstrip()
    
def inputS(): return raw_input("HELP WITH A SOLUTION! Enter The Solution /OR/ PRESS ONLY ENTER IF NO SOLUTION YET:  \n \n ").lower().strip().rstrip()

def instCheck(): return raw_input("TYPE /BACK/ TO GO BACK /OR/ / QUIT / TO QUIT /OR/ JUST ENTER TO CONTINUE:  ").lower().strip().rstrip()
  

    
# MAIN BODY STARTS HERE

errorcheck()
import re
import urllib2
from BeautifulSoup import BeautifulSoup
from playsound import playsound
import threading
from threading import Thread

i = 1
j = 2
Problems = ['  ']
Solutions = ['  ']
myStringProblem = " "
myStringSolution = " "
space = " "
check = 1

keywords = ['delp', 'info', 'dels', 'Print', 'back', 'all', 'quit']


little_gods_file = open('LittleG file\problemstxt.txt', 'r')
myStringProblem = little_gods_file.read()

little_gods_file = open('LittleG file\problemstxt.txt', 'r')
line = little_gods_file.readline()


while line:
    Problems.append(line)
    line = little_gods_file.readline()
little_gods_file.close()

little_gods_file = open('LittleG file\solutionstxt.txt', 'r')
myStringSolution = little_gods_file.read()

little_gods_file = open('LittleG file\solutionstxt.txt', 'r')
line = little_gods_file.readline()
while line:
    Solutions.append(line)
    line = little_gods_file.readline()
little_gods_file.close()

while i <= j:
    import neural
    print ' TYPE /" INFO + ENTER /" TO SEE INSTRUCTIONS OR /" Q + ENTER/" TO QUIT \n  keywords = ["delp", "info", "delP", "Print", "back", "all", "quit"]'
    print'\n Date: '+dateD()+ ' Time: '+timeT()+'\n'
    print 'it been: '
    print  timediff()
    print '\n'
    
    oldtime = timeT()
    olddate = dateD()
    playsound('LittleG sounds\welcome.wav')
    import time
    import thread
    thread.start_new_thread(action, ())
    P = inputP(); playsound('LittleG sounds\wall-right.wav')
    if P == 'back': continue
    if P == 'alll': print printAllP(1); continue

    
    checkK = P
    OnlineCheckK =P
    if P == 'main.py': execfile('Main.py')
    if P == 'quit':playsound('LittleG sounds\goodbye.wav'); break # to stop
    if P == 'q': playsound('LittleG sounds\goodbye.wav'); break  # to stop
    if((P.split(' '))[0]) == '+':informations(); continue
    if((P.split(' '))[0]) == '+add': addKeyWords((P.split(' '))[1]); continue
    if((P.split(' '))[0]) == '+keywords': print (addKeyWords('checking')); continue
    callP = Checking(P, 1)
    P = callP.checkingWords()
    if P == 'info': informations(); continue
    if P == 'quit':playsound('LittleG sounds\goodbye.wav'); break # to stop
    if P == 'q': playsound('LittleG sounds\goodbye.wav'); break  # to stop
    if P == '': continue
    
    if P == ' ': continue
    if len(P) < 2: inputP()
    if P == 'print':
        P =raw_input("Enter The Problem NUM IF YOU DONT REMEMBER THE PROBLEM NUM TYPE BACK +ENTER \n AND TYPE ALL +ENTER :  ")
        if P == 'back': continue
        try:
            int(P)
            print '\n Problem : (' +str(P)+ ') '+ Problems[int(P)]
            continue
        except: continue
        
    if P == 'all': printAllP(0);playsound('LittleG sounds\what-do-you-think.wav'); continue
    
    if P == 'delp': deletePros(); continue
    if P == 'dels': deleteSolut(); continue
    if P == 'back': continue
    P = P + ' ?'

    if __name__ == '__main__':
        Thread(target = knowledge(P)).start()
        Thread(target = history(P)).start()
    

    
    callP = Checking(P, 1)
    checkP = callP.checkwordsPercentage(checkK)
    if checkP >99: continue
    callP = Checking(P, 2)
    checkP = callP.checkwordsPercentage(checkK)
    print str(checkP) +'%'

    playsound('LittleG sounds\what-do-you-think.wav')
    if checkP >94: continue
    inst = instCheck()
    if inst == 'back': continue
    if inst == 'quit': playsound('LittleG sounds\goodbye.wav'); break # to stop
    callK = Checking(P, 3)
    checkK = callK.checkwordsPercentage(checkK.upper())
    print str(checkK) +'%'
    if checkK == 0: print '!!! CHECK INTERNET CONNECTIONS !!! \n \n';print '!!! TYPE /check again/ +ENTER TO CHECK INTERNET AGAIN !!! \n OR JUST PRESS ENTER SKIP \n'
    if checkK != 0:
        onlinePrint = raw_input(' DO YOU WANT TO PRINT IT TYPE "YES" OR "NO" ?:  ')
        if (onlinePrint.lower()) == 'yes':
            print split_into_sentences(OnlineCheckK.upper())
    
    
    S = inputS(); playsound('LittleG sounds\wall-right.wav')
    while S == 'check again':
        callK = Checking(P, 3)
        print OnlineCheckK.upper()
        checkK = callK.checkwordsPercentage(OnlineCheckK.upper())
        print str(checkK) +'%'
        if checkK == 0: print '!!! CHECK INTERNET CONNECTIONS !!! \n \n';print '!!! TYPE /check again/ +ENTER TO CHECK INTERNET AGAIN !!! \n OR JUST PRESS ENTER SKIP \n'

        if checkK != 0:
            onlinePrint = raw_input(' DO YOU WANT TO PRINT IT TYPE "YES" OR "NO" ?:  ')
            if (onlinePrint.lower()) == 'yes': print split_into_sentences(OnlineCheckK.upper())
        S = inputS(); playsound('LittleG sounds\wall-right.wav')
    remove_next_line = 0    
    if S == '':
        callK = Checking(P, 4)
        S2 = callK.checkwordsPercentage(OnlineCheckK)
        try: S2 = S2.replace('\n', ' ')
        except: S2 = '!!!NO SOLUTION YET !!!'
        S2 = S2.strip().rstrip()
        print S2
        S = S2  #this is to asign the problem that closely related
        remove_next_line = 1
        
    callS = Checking(S, 2)
    S = callS.checkingWords()
    if S == 'info': informations(); continue
    if S == 'quit': playsound('LittleG sounds\goodbye.wav');break # to stop
    if S == 'all': printAllP(0);playsound('LittleG sounds\what-do-you-think.wav'); continue
    if S == 'delp': deletePros(); continue
    if S == 'print':
        S =raw_input("Enter The Problem NUM:  ")
        print '\n Problem : (' +str(S)+ ') '+ Problems[int(S)]
        playsound('what-do-you-think.wav')
        continue
    if S == 'dels': deleteSolut(); continue
    if S == 'back': continue
    callS = Checking(S, 2)
    checkS = callS.checkwordsPercentage(OnlineCheckK)
    print str(checkS) +'%'
    playsound('LittleG sounds\what-do-you-think.wav')
    
    
    Problems.append(P)
    Solutions.append(S)
    print " "
    num = str(i)
    print "Problem: (" + num +") " + P+ " Solution: (" + num +") " + S
    print " "
    i+=1
    myStringProblem = myStringProblem + "\n " + P
    if remove_next_line == 1:
        myStringSolution = myStringSolution+ "\n " + S
    if remove_next_line == 0:
        myStringSolution = myStringSolution + "\n " + S
        
    saving(myStringProblem, myStringSolution)
        
    lenNum = str((len(Problems)) - 1)
    print "Number of Problems: " + lenNum
    print " "        
        
        
    
    Problems.sort()
   
        
    j+=1
  
#Dictionary can be used the link the problem to the solution
