#format data from project data to svm: change label from name to 1/0, replace ':' between feature and value with space

import re
def preprocess_mega (trainFile, megaTrainFile, testFile, megaTestFile):
    train = open(trainFile, 'r')
    megaTrain = open(megaTrainFile, 'w')
    test = open(testFile, 'r')
    megaTest = open(megaTestFile, 'w')
    
    for line in train:
        newline = ''
        if line[0] == 'P':  #positive
            newline += '1'
            for i in range(8,len(line)):
                newline += line[i]
        if line[0] == 'N':  #negative
            newline += '0'
            for i in range(8,len(line)):
                newline += line[i]
        if line[0] == 'S':  #spam
            newline += '1'
            for i in range(4,len(line)):
                newline += line[i]
        if line[0] == 'H':  #ham
            newline += '0'
            for i in range(3,len(line)):
                newline += line[i]            
        newline = re.sub(r'(\d+):(\d+)', r'\1 \2', newline) 
        megaTrain.write(newline)
    
    for line in test:
        newline = re.sub(r'(\d+):(\d+)', r'\1 \2', line)
        megaTest.write('1 '+newline)
   
    train.close()
    megaTrain.close()
    test.close()
    megaTest.close()

if __name__ == "__main__":
    import sys
    preprocess_mega (sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
