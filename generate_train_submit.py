import csv

r = csv.reader(open('train.csv'))
r.next()
outf = open('train_submit.csv', 'w')
print >>outf, ''
for row in r:
    print >>outf, "%s,%s,%s,%s" % (row[0], row[5], row[6], row[7])
