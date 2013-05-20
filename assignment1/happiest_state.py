import sys
import json 
import re

def tweet_score(tweet, score_dict):
	final_score = 0.0;
	word_list = re.findall(r"[\w']+|[.,!?;]", tweet)
	for word in word_list:
		if word in score_dict.keys():
			final_score += float(score_dict[word])

	return final_score



sentiment_file = open('AFINN-111.txt')

sentiment_score = {}
count = 0

for line in sentiment_file:
	count += 1
	term, score = line.split("\t")
	sentiment_score[term] = int(score)

# print len(sentiment_score), count

tweet_file = open('output.txt')

for line in tweet_file:
	Tweet = json.loads(line)

	if('text' in Tweet.keys()):
		display_score = tweet_score(Tweet['text'], sentiment_score)

print "NY"