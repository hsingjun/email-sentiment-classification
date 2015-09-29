
def transf_label_imdb(numLabel, nameLabel, dataName):
    num = open(numLabel, 'r')
    name = open(nameLabel, 'w')
    
    for line in num:
        item = line.split()
        if float(item[0]) > 0:
            if dataName == 'imdb':
                name.write('POSITIVE\n')
            else:
                name.write('SPAM\n')
        else:
            if dataName == 'imdb':
                name.write('NEGATIVE\n')
            else:
                name.write('HAM\n')
    num.close()
    name.close()         

if __name__ == "__main__":
    import sys
    transf_label_imdb (sys.argv[1], sys.argv[2], sys.argv[3])
