#Naive Bayes
#Output modelfile: line[0]:indicate if it's email data or imdb data, line[1]:P(positive), line[2]:P(negative), line[3]:P(word|positive), line[4]:P(word|negative). Conditional probabilities for each word are separated by space

import re
def nblearn (trainingfile, modelfile):

    train = open(trainingfile, 'r')
    model = open(modelfile, 'w')    

    numPos = 0       #number of positive cases
    numNeg = 0       #number of negative cases
    posWdCnt = []    #count number of each token in positive reviews
    negWdCnt = []     #count number of each token in positive reviews
    totalPos = 0      #total number of word occurence in positive cases
    totalNeg = 0      #total number of word occurence in negative cases
    
    for line in train:
        features = re.findall(r'(\d+):',line)
        values = re.findall(r':(\d+)',line)
        if line[0] == 'P' or line[0] == 'S':
            numPos +=1
            for i in range(len(features)):
                if int(features[i]) > len(posWdCnt):
                    posWdCnt.extend([0]*(int(features[i]) - len(posWdCnt)))
                posWdCnt[int(features[i])-1] += int(values[i])
                totalPos += int(values[i])
        else:
            numNeg +=1
            for i in range(len(features)):
                if int(features[i]) > len(negWdCnt):
                    negWdCnt.extend([0]*(int(features[i]) - len(negWdCnt)))
                negWdCnt[int(features[i])-1] += int(values[i])
                totalNeg += int(values[i])
    
    #extend posWdCnt and negWdCnt to same length
    if len(posWdCnt) < len(negWdCnt):
        posWdCnt.extend([0]*(len(negWdCnt)-len(posWdCnt)))
    else:
        negWdCnt.extend([0]*(len(posWdCnt)-len(negWdCnt)))
        
    V = 0 #count vocabulary size
    for i in range(len(posWdCnt)):
        if posWdCnt[i] != 0 or negWdCnt[i] != 0:
            V += 1
        
    N = numPos + numNeg
    pPos = numPos / N
    pNeg = numNeg / N
    
    probGivenPos = []
    probGivenNeg = []
    
    for i in range(len(posWdCnt)):
        probGivenPos.append((int(posWdCnt[i])+1)/(totalPos+V))
    for i in range(len(negWdCnt)):
        probGivenNeg.append((int(negWdCnt[i])+1)/(totalNeg+V))
    
    train.close()
    train = open(trainingfile, 'r')
    line = train.readline()
    if line[0] == 'P' or line[0] == 'N':
        model.write('imdb' + '\n')
    else:
        model.write('email'+ '\n')
    model.write(str(pPos)+'\n')
    model.write(str(pNeg)+'\n') 
    posStr = ''   
    for i in range(len(probGivenPos)):
        posStr += str('%.10f' %probGivenPos[i]) + ' '  
    negStr = '' 
    for i in range(len(probGivenNeg)):
        negStr += str('%.10f' %probGivenNeg[i]) + ' '
    model.write(posStr+'\n'+negStr)

    train.close()
    model.close()
    
if __name__ == "__main__":
    import sys
    nblearn (sys.argv[1], sys.argv[2])
