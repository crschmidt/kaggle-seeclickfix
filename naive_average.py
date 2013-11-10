import random
import csv

r = csv.reader(open("train.csv"))
r.next()
votes = comments = views = 0
count = 0 
for row in r:
    if '2013' not in row[9]:
        continue
    votes += int(row[5])
    comments += int(row[6])
    views += int(row[7])
    count += 1
avg_votes = float(votes)/count
avg_comments = float(comments)/count
avg_views = float(views)/count
outf = open('out.csv', 'w')
outf.write("id,num_views,num_votes,num_comments\n")
avg_views_ipart = int(avg_views)
avg_comments_ipart = int(avg_comments)
avg_votes_ipart = int(avg_votes)
r = csv.reader(open("test.csv"))
r.next()
for row in r:
    id = row[0]
    num_views = avg_views_ipart + 1 * (random.random() > (avg_views - avg_views_ipart))
    num_votes = avg_votes_ipart + 1 * (random.random() > (avg_votes - avg_votes_ipart))
    num_comments = 0 # avg_comments_ipart + 1 * (random.random() > (avg_comments - avg_comments_ipart))
    print >>outf, "%i,%i,%i,%i" % (int(id), num_views, num_votes, num_comments)

