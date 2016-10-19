import sys
def evaluation (trueFile, predFile):
    truef = open(trueFile, 'r')
    predf = open(predFile, 'r')
    
    trueLabel = truef.readlines()
    predLabel = predf.readlines()

    if len(trueLabel) != len(predLabel):
        print('Number of true labels and number of predict labels are not consistent!')
        print('No. of lables in true file:' + str(len(trueLabel)))
        print('No. of lables in predict file:' + str(len(predLabel)))
    else:
        numPosCorr = 0
        numNegCorr = 0
        numClassifiedPos = 0
        numClassifiedNeg = 0
        numTruePos = 0
        numTrueNeg = 0
        for i in range(len(trueLabel)):
            if trueLabel[i][0] == 'P' or trueLabel[i][0] == 'S' :
                numTruePos +=1
            if trueLabel[i][0] == 'N' or trueLabel[i][0] == 'H':
                numTrueNeg +=1
            if predLabel[i][0] == 'P' or predLabel[i][0] == 'S':
                numClassifiedPos +=1
                if trueLabel[i][0] == 'P' or trueLabel[i][0] == 'S':
                    numPosCorr +=1
            if predLabel[i][0] == 'N' or predLabel[i][0] == 'H':
                numClassifiedNeg +=1
                if trueLabel[i][0] == 'N' or trueLabel[i][0] == 'H':
                    numNegCorr +=1
        precPos = numPosCorr / numClassifiedPos
        precNeg = numNegCorr / numClassifiedNeg 
        recallPos = numPosCorr / numTruePos
        recallNeg = numNegCorr / numTrueNeg
        f1Pos = (2*precPos*recallPos) / (precPos+recallPos)
        f1Neg = (2*precNeg*recallNeg) / (precNeg+recallNeg)   
        accuracy = (numPosCorr+numNegCorr) / (numTruePos+numTrueNeg)    
        sys.stdout.write('precision(Pos) = '+str(precPos)+'\n')  
        sys.stdout.write('precision(Neg) = '+str(precNeg)+'\n') 
        sys.stdout.write('recal(Pos) = '+str(recallPos)+'\n')  
        sys.stdout.write('recal(Neg) = '+str(recallNeg)+'\n') 
        sys.stdout.write('f1(Pos) = '+str(f1Pos)+'\n')
        sys.stdout.write('f1(Neg) = '+str(f1Neg)+'\n')
        sys.stdout.write('Accuracy = '+str(accuracy))

if __name__ == "__main__":
    import sys
    evaluation (sys.argv[1], sys.argv[2])
