import re
import math
import sys
def nbclassify (modelfile, testfile):

    modelf = open(modelfile, 'r')
    testf= open(testfile, 'r')

    model = modelf.readlines();
    dataname = model[0]
    pPos = float(model[1])
    pNeg = float(model[2])    
    condPosStr = re.findall('\d.\d+',model[3])
    condNegStr = re.findall('\d.\d+',model[4]) 
   
    #convert to float list   
    condPos = []
    condNeg = []
    for i in range(len(condPosStr)):
        condPos.append(float(condPosStr[i]))
        condNeg.append(float(condNegStr[i]))
 
    #find the smalles conditional probability in the model 
    minPos = min(condPos) 
    minNeg = min(condNeg)
    minProb = min(minPos, minNeg)
    
    for line in testf:
        features = re.findall(r'(\d+):',line)
        values = re.findall(r':(\d+)',line)
        pLabelPos = math.log(pPos)
        pLabelNeg = math.log(pNeg)
        for i in range(len(features)):
            if int(features[i]) > len(condPos): #if an unknown word, assign a small prob
                pLabelPos += int(values[i]) * math.log(minProb)  
                pLabelNeg += int(values[i]) * math.log(minProb)
            else: #otherwise, add the conditional probability   
                pLabelPos += int(values[i]) * math.log(float(condPos[int(features[i])-1]))
                pLabelNeg += int(values[i]) * math.log(float(condNeg[int(features[i])-1]))
        if pLabelPos >= pLabelNeg:
            if dataname == 'imdb\n':
                sys.stdout.write('POSITIVE\n')
            else:
                sys.stdout.write('SPAM\n')
        else:
            if dataname == 'imdb\n':
                sys.stdout.write('NEGATIVE\n')
            else:
                sys.stdout.write('HAM\n')
    
    modelf.close()
    testf.close()
    
if __name__ == "__main__":
    import sys
    nbclassify (sys.argv[1], sys.argv[2])
