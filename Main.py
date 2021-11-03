import sys
import os
import neural
import LITTLEGOD

def paths():
    paths =''
    cur_dir =os.getcwd()
    print ''
    print 'AVALIABLE FILES: '
    num = 1
    for file in os.listdir(cur_dir):
        if file.endswith(".py"):
            print str(num) +' '+ str(os.path.join(cur_dir,file))
            paths = paths + (os.path.join(cur_dir,file))+'\n'
            num = num+1
    
    print ''
    filew = open('LittleG file\Lfilepath.txt', 'w')
    filew.writelines(paths)
    filew.close()


def runPy():
    paths()        
    name = raw_input(' enter file name or just press only ENTER to go LITTLEGOD: ')
    if name == '':
        mainName= 'LITTLEGOD.py'
        
    if name != '':
        filew = open('LittleG file\Lfilepath.txt', 'r')
        filer = filew.read()
        filew.close()
        filer = filer.split('\n')
        try:
            num = int(name)-1
            print filer[num]
            mainName = filer[num]

        except:
            print 'ENTERED WRONG NUMBER'
            return
    try:
        execfile(mainName)
    except:
        print 'SORRY WRONG FILE NAME TRY AGAIN\n'
        return
    


runPy()          
