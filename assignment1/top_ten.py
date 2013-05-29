from sys import argv
import json
from collections import Counter

tweetfile = open(argv[1])
tags = []
for line in tweetfile:
	tweet = json.loads(line)
	if tweet.get('entities') is None or tweet.get('entities')['hashtags'] is None:
		pass
	else:
		hashtags = tweet.get('entities')['hashtags']
		for item in hashtags:
			tags.append(item['text'])

tagcounts = Counter(tags)
tagcounts = dict(tagcounts)

# for item in tagcounts:
# 	print "%s %r" % (item, float(tagcounts[item]))

highest = sorted(tagcounts, key=tagcounts.get)[-10:]
highest.reverse()

for item in highest:
	print "%s %r" % (item, float(tagcounts[item]))
