#format data from project train data to svm format: change label from name to +1/-1
#add an arbitrary label (1) to test data)

def preprocess_svm (trainFile, svmTrainFile, testFile, svmTestFile):
    train = open(trainFile, 'r')
    svmTrain = open(svmTrainFile, 'w')
    test = open(testFile, 'r')
    svmTest = open(svmTestFile, 'w')
    
    for line in train:
        if line[0] == 'P':  #positive
            svmTrain.write('+1')
            for i in range(8,len(line)):
                svmTrain.write(line[i])
        if line[0] == 'N':  #negative
            svmTrain.write('-1')
            for i in range(8,len(line)):
                svmTrain.write(line[i])
        if line[0] == 'S':  #spam
            svmTrain.write('+1')
            for i in range(4,len(line)):
                svmTrain.write(line[i])
        if line[0] == 'H':  #ham
            svmTrain.write('-1')
            for i in range(3,len(line)):
                svmTrain.write(line[i])
                
    for line in test:
        svmTest.write('+1 '+line)
        
if __name__ == "__main__":
    import sys
    preprocess_svm (sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
