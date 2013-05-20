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

def new_words_calculation(sample_tweet_score_dict, sample_sentiment_score_dict):
	final_word_score_dict = {}
	for item in sample_tweet_score_dict:			
		each_tweet_word_list_dict = {}
		tweet_word_list = re.findall(r"[\w']+|[.,!?;]", item)
		for word in tweet_word_list:
			if(word not in sample_sentiment_score_dict.keys()):
				each_tweet_word_list_dict[word] = sample_tweet_score_dict[item]

		#update the final_word_score_dict with the each_tweet_word_list_dict
		for new_word in each_tweet_word_list_dict:
			if(new_word not in final_word_score_dict.keys()):
				final_word_score_dict[new_word] = each_tweet_word_list_dict[new_word]
			else:
				final_word_score_dict[new_word] += each_tweet_word_list_dict[new_word]

	return final_word_score_dict





sentiment_file = open(sys.argv[1])

sentiment_score = {}
tweet_score_dict = {}
final_list = {}
count = 0

for line in sentiment_file:
	count += 1
	term, score = line.split("\t")
	sentiment_score[term] = int(score)

# print len(sentiment_score), count

tweet_file = open(sys.argv[2])

for line in tweet_file:
	Tweet = json.loads(line)

	if('text' in Tweet.keys()):
		display_score = tweet_score(Tweet['text'], sentiment_score)
		tweet_score_dict[Tweet['text']] = display_score

final_list = new_words_calculation(tweet_score_dict, sentiment_score)


for item in final_list:
	print item, final_list[item]

