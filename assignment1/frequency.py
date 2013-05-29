from sys import argv
import json
from collections import Counter

tweetfile = open(argv[1])
tweettext = []
for line in tweetfile:
    tweet = json.loads(line)
    if tweet.get('text') is None:
    	pass
    else:
    	tweettext.append(tweet.get('text'))

wordlist = []
for item in tweettext:
	tweetwords = item.split()
	for word in tweetwords:
		word = word.strip().lower().encode('utf-8')
		wordlist.append(word)

no_of_words = len(wordlist)
wordcounts = Counter(wordlist)
wordcounts = dict(wordcounts)

for item in wordcounts:
	print "%s %r" % (item, float(wordcounts[item])/float(no_of_words))
