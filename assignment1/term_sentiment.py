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
sentscore = []
newterms = {}
scorepair = {}

for item in tweettext:
	tweetscore = 0.0
	nonzeroscores = []
	scorepair[item] = []
	tweetwords = item.split()
	for word in tweetwords:
		word = word.strip().lower().encode('utf-8')
		if word in scores: # if a word in the tweet is in our sentiment corpus, we add up the corresponding score
			tweetscore = tweetscore + scores[word]
			nonzeroscores.append(scores[word])
		else:
			tweetscore = tweetscore + 0
	scorepair[item].append(tweetscore)
	scorepair[item].append(nonzeroscores)
	sentscore.append(scorepair)
# print "%d sentiment scores" % len(sentscore)

for tweet in scorepair:
	nonzeroscores = scorepair[tweet][1]
	tweetwords = tweet.split()
	for word in tweetwords:
		wordLower = word.strip().lower().encode('utf-8')
		word = word.strip().encode('utf-8')
		if wordLower not in scores and word not in newterms:
			newterms[word] = float(sum(nonzeroscores)) / len(nonzeroscores) if len(nonzeroscores) > 0 else 0.0
		if wordLower not in scores and word in newterms:
			newterms[word] = newterms[word] + (float(sum(nonzeroscores)) / len(nonzeroscores) if len(nonzeroscores) > 0 else 0.0)

for key in newterms:
	print key, newterms[key]
