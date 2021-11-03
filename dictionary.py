#dictionary
print ''
word = raw_input('ENTER WORD or TYPE Main.py AND PRESS ENTER TO GO BACK ').lower()
if word == 'main.py': execfile('Main.py') 

def openDictionary(word):
    
    filedict = open('knowledge data\kdictionary.txt', 'r')
    data = filedict.readlines()
    filedict.close()
      
    for ch in range(len(data)):
        data[ch] = data[ch].rstrip().strip()
        word = word.strip().rstrip()

        import difflib
        score = difflib.SequenceMatcher(None,data[ch].lower(),word.lower()).ratio()
        score = score*100
        if score >= 100:
            num = ch+ 50
            num2 = ch
            while num > (len(data)):
                num = num - 1
            while num2 < num:
                print data[num2]
                num2= num2+1
            return

openDictionary(word)
