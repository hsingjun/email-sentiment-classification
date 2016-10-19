#process enron data into project data format

import os
def enron_preprocess (formattedFile, formattedTestFile):
    vocabf = open('enron.vocab', 'r', encoding='latin1')
    formatted = open(formattedFile, 'w')
    formattedTest = open(formattedTestFile, 'w')
    #construct a dictionary that stores the vocabulary and corresponding index
    vocabDict = {}
    count = 0
    for line in vocabf:
        count +=1
        vocabDict[line.rstrip('\n')] = count
    
    hamPaths = ['./enron1/ham', './enron2/ham', './enron4/ham', './enron5/ham']
    for path in hamPaths:
        for filename in os.listdir(path):
            email = open(path+'/'+filename, 'r', encoding='latin1')
            ftr_val = {}    #feature_value dictionary for this email
            for line in email:
                tokens = line.split()
                for token in tokens:
                    if token in vocabDict: #if this token exists in the vocab
                        if vocabDict[token] in ftr_val:   #if this token has already appeared in this email
                            ftr_val[vocabDict[token]] = ftr_val[vocabDict[token]] + 1
                        else:   #else:if this token has not appeared in the this email, then set a new key in the feature_value dictionary
                            ftr_val[vocabDict[token]] = 1
            formatted.write('HAM ')
            for key in sorted(ftr_val):
                 formatted.write(str(key)+':'+ str(ftr_val[key]) + ' ')
            formatted.write('\n')
            email.close()
            
    spamPaths = ['./enron1/spam', './enron2/spam', './enron4/spam', './enron5/spam']
    for path in spamPaths:
        for filename in os.listdir(path):
            email = open(path+'/'+filename, 'r', encoding='latin1')
            ftr_val = {}    #feature_value dictionary for this email
            for line in email:
                tokens = line.split()
                for token in tokens:
                    if token in vocabDict: #if this token exists in the vocab
                        if vocabDict[token] in ftr_val:   #if this token has already appeared in this email
                            ftr_val[vocabDict[token]] = ftr_val[vocabDict[token]] + 1
                        else:   #else:if this token has not appeared in the this email, then set a new key in the feature_value dictionary
                            ftr_val[vocabDict[token]] = 1
            formatted.write('SPAM ')
            for key in sorted(ftr_val):
                 formatted.write(str(key)+':'+ str(ftr_val[key]) + ' ')
            formatted.write('\n')
            email.close()
            
            
    testPath = './spam_or_ham_test'
    fileList = []
    for filename in os.listdir(testPath):
        if filename.endswith('.txt'):
            fileList.append(filename)
    fileList.sort()
    for filename in fileList:
        email = open(testPath+'/'+filename, 'r', encoding='latin1')
        ftr_val = {}    #feature_value dictionary for this email
        for line in email:
            tokens = line.split()
            for token in tokens:
                if token in vocabDict: #if this token exists in the vocab
                    if vocabDict[token] in ftr_val:   #if this token has already appeared in this email
                        ftr_val[vocabDict[token]] = ftr_val[vocabDict[token]] + 1
                    else:   #else:if this token has not appeared in the this email, then set a new key in the feature_value dictionary
                        ftr_val[vocabDict[token]] = 1
        for key in sorted(ftr_val):
             formattedTest.write(str(key)+':'+ str(ftr_val[key]) + ' ')
        formattedTest.write('\n')
        email.close()
        
    vocabf.close()
    formatted.close()
        

if __name__ == "__main__":
    import sys
    enron_preprocess (sys.argv[1], sys.argv[2])
