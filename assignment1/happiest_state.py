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
tweets = []
for line in tweetfile:
	tweetstate = []
	tweet = json.loads(line)
	if tweet.get('place') is None or tweet.get('place')['country_code'] != "US":
		pass
	else:
		tweetstate.append(tweet.get('text'))
		tweetstate.append(tweet.get('place')['full_name'][-2:])
		tweets.append(tweetstate)

# Split tweet into constituent words and compute sentiment score
states = []
for item in tweets:
	tweetscore = 0
	tweetwords = item[0].split()
	for word in tweetwords:
		word = word.strip().lower().encode('utf-8')
		if word in scores: # if a word in the tweet is in our sentiment corpus, we add up the corresponding score
			tweetscore = tweetscore + scores[word]
		else:
			tweetscore = tweetscore + 0
	item.append(tweetscore)
	states.append(item[1])

states = set(states)

statescores = {}

for state in states:
	statescore = 0
	for item in tweets:
		if item[1] == state:
			statescore = statescore + item[2]
		else:
			statescore = statescore + 0
	statescores[state] = statescore

print sorted(statescores, key=statescores.get)[-1]
