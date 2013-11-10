import math
import csv
import sys
r = csv.reader(open(sys.argv[1]))
r.next()
d = {}
for row in r:
    d[row[0]] = row
    
r = csv.reader(open("train.csv"))
r.next()
votes = comments = views = 0
total_sum = 0
count = 0
for row in r:
#    print row
    test = d[row[0]]
    votes, comments, views = map(int, row[5:8])
    test_views, test_votes, test_comments = map(int, test[1:])
    row_sum = sum([(math.log(test_views+1) - math.log(views+1))**2, (math.log(test_votes+1) - math.log(votes+1))**2, (math.log(test_comments+1)-math.log(comments+1))**2])
    total_sum += row_sum
    count += 1
print float(1)/(count*3) * total_sum    
