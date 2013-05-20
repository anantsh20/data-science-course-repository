import sys
import json 
import re
from operator import itemgetter

def hashtag_dict(sample_hashtags_list):
	final_hashtags_freq_dict = {}
	for item in sample_hashtags_list:			
		each_tweet_hashtags_list = {}
		separated_hashtags_list = re.findall(r"[\w']+|[.,!?;]", item)
		for item in separated_hashtags_list:
			print item
		for sample_hashtag in separated_hashtags_list:
			if(sample_hashtag not in each_tweet_hashtags_list.keys()):
				each_tweet_hashtags_list[sample_hashtag] = 1.0
			else:
				each_tweet_hashtags_list[sample_hashtag] = each_tweet_hashtags_list[sample_hashtag] + 1.0


		#update the final_word_score_dict with the each_tweet_word_list_dict
		for each_hashtag in each_tweet_hashtags_list:
			if(each_hashtag not in final_hashtags_freq_dict.keys()):
				final_hashtags_freq_dict[each_hashtag] = each_tweet_hashtags_list[each_hashtag]
			else:
				final_hashtags_freq_dict[each_hashtag] = final_hashtags_freq_dict[each_hashtag] + 1.0

	return final_hashtags_freq_dict

	
final_list = {}
hashtags_list = []
sum_of_total_words = 0

tweet_file = open(sys.argv[1])

for line in tweet_file:
	Tweet = json.loads(line)

	if('entities' in Tweet.keys()):
		pyresponse = Tweet['entities']
		pyresponse1 =  pyresponse['hashtags']
		pyresponse2 =  pyresponse1[0]
		pyresponse3 = pyresponse2['text']
		hashtags_list.append(pyresponse3)


final_list = hashtag_dict(hashtags_list)


sample_final_list = sorted(final_list.items(), key=lambda kv: kv[1], reverse=True)

for k, v in sample_final_list[:10]:
    print k, v



