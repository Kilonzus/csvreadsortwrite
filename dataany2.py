import csv
import operator
from collections import Counter
from collections import defaultdict

fin_name = raw_input('Enter the name of the input file, include the extenstion if needed \n')
fout_name = raw_input('Enter the name of the output file, include the extenstion if necessary \n')

with open(fin_name, 'rb') as fin:
    with open(fout_name, 'wb') as fout:
        reader = csv.reader(fin)
        next(reader)
        writer = csv.writer(fout)
        sortedlist = sorted(reader, key=operator.itemgetter(1), reverse=False)
        writer.writerows(sortedlist)
        d = defaultdict(list)
        #sortedlist.next()
        city_counter = {}
        for row in sortedlist:
            print(row[0], row[1], row[2], row[3], row[4])
            city_list = row[1]
            for city in city_list:
                if city in city_counter:
                    city_counter[city] +=1
                else:
                    city_counter[city] = 1
            if row[1]  != 'City':
                d[row[1]].append(float(row[3]))
        for k,v in d.iteritems():
            Counter(value for values in d.itervalues() for value in values)
            c = Counter(k)
            print c
            print "There are {} points of data for {}, ".format([len(v)], k), "{}'s Average is {}".format(k,sum(v)/len(v))
