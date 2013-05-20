import sys

sentiment_file = open("AFINN-111.txt")

sentiment_score = {}
count = 0

for line in sentiment_file:
	count += 1
	term, score = line.split("\t")
	sentiment_score[term] = int(score)

print len(sentiment_score), count