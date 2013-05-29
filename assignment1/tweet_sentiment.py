import sys
import json

# Get sentiment scores for each term from corpus
afinnfile = open(sys.argv[1])
scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.

# Get list of valid tweets from tweet file, discarding the non-tweet actions
tweetfile = open(sys.argv[2])
tweettext = []
for line in tweetfile:
    tweet = json.loads(line)
    if tweet.get('text') is None:
    	pass
    else:
    	tweettext.append(tweet.get('text'))
# print "%d valid tweets" % len(tweettext)

# Split tweet into constituent words and compute sentiment score
sentscore = [] # Let's store the scores in a list
for item in tweettext:
	tweetscore = 0.0
	tweetwords = item.split()
	for word in tweetwords:
		if word.strip().lower() in scores: # if a word in the tweet is in our sentiment corpus, we add up the corresponding score
			tweetscore = tweetscore + scores[word.strip().lower()]
		else:
			tweetscore = tweetscore + 0
	sentscore.append(tweetscore)
# print "%d sentiment scores" % len(sentscore)

for item in sentscore:
	print item