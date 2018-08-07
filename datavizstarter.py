'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#TO DO: Get the JSON data



#Create list for polarity
polarityList = []

#Loop through your tweets 
for tweet in tweetData:
	#TO DO: Create a TextBlob from the text of each tweet 
	#Look at the TextBlob documentation under the reference section of the project prompt

	#TO DO: Append the polarity from the TextBlob to the polarityList



#Calculate the average polarity 
polaritySum = 0
#TO DO: Loop through the polarity list and add all of the values together 

#TO DO: Divide the sum of all the polarity values by the number of elements in the list



#Print statement for testing purposes! Don't edit this line
print("average polarity: ", avgPolarity)






#PART 2: CREATE YOUR GRAPH!
#Look at the pyplot documentation under the reference section of the project prompt
#TO DO: Create the PLT graph for polarity

#TO DO: Set the x label

#TO DO: Set the y label

#TO DO: Set the title 

#TO DO: Set the axis 

#Show the plot




#Now make find the average subjectivity and make a graph! 


