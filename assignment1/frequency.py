import sys
import json 
import re

def freq_calculation(sample_tweet_score_list):
	final_word_freq_dict = {}
	for item in sample_tweet_score_list:			
		each_tweet_word_list_dict = {}
		tweet_word_list = re.findall(r"[\w']+|[.,!?;]", item)
		for word in tweet_word_list:
			if(word not in each_tweet_word_list_dict.keys()):
				each_tweet_word_list_dict[word] = 1.0
			else:
				each_tweet_word_list_dict[word] =+ 1.0

		#update the final_word_score_dict with the each_tweet_word_list_dict
		for each_word in each_tweet_word_list_dict:
			if(each_word not in final_word_freq_dict.keys()):
				final_word_freq_dict[each_word] = 1.0
			else:
				final_word_freq_dict[each_word] += 1.0

	return final_word_freq_dict


final_list = {}
tweet_list = []
sum_of_total_words = 0

tweet_file = open(sys.argv[1])

for line in tweet_file:
	Tweet = json.loads(line)

	if('text' in Tweet.keys()):
		tweet_list.append(Tweet['text'])

final_list = freq_calculation(tweet_list)


for item in final_list:
	sum_of_total_words += final_list[item]

for individual_word in final_list:
	individual_word_freq = final_list[individual_word]/sum_of_total_words
	print individual_word, individual_word_freq
