import json

#TO DO: fill in a list of questions, and a list of associated keys for the survey results
questions = [" ", " ", " "]
keys = [" ", " ", " "]

#create a list that stores each person's response as a separate dictionary
list_of_answers = []

while True:
    answerDict = {}
    #loop through questions
    for i in range(len(questions)):
        #TO DO: get user input to your question at index i and store in a variable response

        #TO DO: store response to the corresponding key in the answerDict

        #print statement for testing purposes! don't edit the following 2 lines
        print("dictionary with your answer: ")
        print(answerDict)

    #TO DO: append answer for this particular response to master list of list_of_answers


    #TO DO: check if done and break or continue accordingly
    done = input("are you done collecting responses? ")
    if done == "yes":

    else:

#UN-COMMENT THIS SECTION TO WORK ON PART 3
#TO DO: open a file, and write each entry into the file in json format
#file = open("allanswers.json", "w")
#TO DO: fill out range parameter to loop through list_of_answers
#for i in range():
    #TO DO: while looping, dump answer at each index in list_of_answers into json file
    #json.dump( , )
    #file.write('\n')
#TO DO: use close() fumction to close your file