# We start by importing the JSON library to use for this project.
# Twitter data is stored in this format - this is the same format
# students learned for their Survey Project!
import json

# Next we want to open the JSON file. We tag this file as
# "r" read only because we are only going to look at the data.
tweetFile = open("tweets_small.json", "r")

# We use the JSON library to get data from the file as JSON data.
tweetData = json.load(tweetFile)

# We can close the file now that we have locally stored the data.
tweetFile.close()

# We then print the data of ONE tweet:
# the [0] denotes the *first* tweet object.
# We access parts of the tweet using ["NameOfPart"].
#print("Tweet: ", tweetData[0])
#print("Tweet id: ", tweetData[0]["id"])

# How might we print the text object?
#print("Tweet text: ", tweetData[0]["text"])


# How might we use loops to print the ["text"] of all the tweets?
for i in range(len(tweetData)):
	print(tweetData[i]["user"]["screen_name"])

for tweet in tweetData:
	print(tweet["text"])