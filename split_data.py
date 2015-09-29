#Split data into two groups: 75%training and 25%testing OR 25%training 75% testing

import random
import re
def split_data (formattedFile, train, test, test_label, train_ratio):
    wholeSet = open(formattedFile, 'r') 
    tr = open(train, 'w')
    te = open(test, 'w')
    lb = open(test_label, 'w')
    ratio = train_ratio
    
    lines = wholeSet.readlines()

    order = list(range(len(lines)))
    shuffled = random.sample(order, len(order))   

    for i in range(0, int(float(ratio)*len(shuffled))):
        tr.writelines(lines[shuffled[i]])
    for i in range(int(float(ratio)*len(shuffled)), len(shuffled)):
        fv = re.findall(r'\d+:\d+', lines[shuffled[i]])
        te.writelines(' '.join(fv))
        te.write('\n')
        label = re.findall(r'([A-Z]+)', lines[shuffled[i]])
        lb.write(label[0] + '\n')    
        
    wholeSet.close()
    tr.close()
    te.close()
    lb.close()

if __name__ == "__main__":
    import sys
    split_data(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
