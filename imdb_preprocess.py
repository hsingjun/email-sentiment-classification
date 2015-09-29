#Convert the data into required format and store in the file 'imdb_formatted'

import re
def imdb_preprocess (rawfile, formattedfile):
    raw = open(rawfile, 'r') 
    formatted = open(formattedfile, 'w')

    for line in raw:
        output = ''
        point = re.search(r'^(\d+)\s', line)
        if point:
            if int(point.group(1)) >= 7:
                output += 'POSITIVE '
            else:
                output += 'NEGATIVE '
        features = re.findall(r'(\d+):',line)
        values = re.findall(r':(\d+)',line)
        for i in range(len(features)):
            output += str(int(features[i])+1) + ':' + values[i] + ' '
        output += '\n'
        formatted.write(output)

    raw.close()
    formatted.close()

if __name__ == "__main__":
    import sys
    imdb_preprocess (sys.argv[1], sys.argv[2])

