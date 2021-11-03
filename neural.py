
data = []
inFile = open('LittleG file\knownledgefiles.txt', 'r')
files = inFile.readlines()
inFile.close()

for filen in files:
    link = str(filen[13])
    filen = filen.replace('\n', '')
    inFile = open(filen, 'r')
    file = inFile.readlines()
    inFile.close()
    
    num = 0
    for filee in file:
        rel = link+str(num)
        num2 = 0
        
        inFile = open('LittleG file\knownledgefiles.txt', 'r')
        files = inFile.readlines()
        inFile.close()
        for filen in files:
            link2 = str(filen[13])
            filen = filen.replace('\n', '')
            inFile = open(filen, 'r')
            file2 = inFile.readlines()
            inFile.close()

            for fileee in file2:
                if fileee != filee:
                    import difflib
                    score = difflib.SequenceMatcher(None,fileee.lower(),filee.lower()).ratio()
                    score = score*100
                    if score > 60:
                        rel2 = ':'+ link2 +str(num2)+'['+str(score)+']'
                        rel= rel+rel2
                    num2 = num2 + 1
            data.append(rel+'\n')
                        
        num = num + 1

inFile = open('LittleG file\Neuralnetwork.txt','w')
inFile.writelines(data)
inFile.close()
        

        
