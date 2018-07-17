#text to start
start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''

#text for left option
left = '''
You come across a street with a cafe and a library. Type 'cafe' to go to the cafe or 'library' to go to the library.
'''

#text for right option 
right = '''
You get to the airport with two free seats on planes to Melbourne and Hawaii. Type 'Melbourne' to go down under or 'Hawaii' to go to paradise.
'''

print(start)

print("Type 'left' to go left or 'right' to go right.") 

user_input = input()

#deals with left options 
if user_input == "left":
    print("You decide to go left and %s" %(left)) 
    left_input = input()
    if left_input == "cafe":
    	print("You went to the cafe and got a nice latte! Yay!")
    elif left_input == "library":
    	print("You went to the library and got a great book! Woohoo!")
 
#deals with right options 
elif user_input == "right":
    print("You choose to go right and ... %s" %(right)) 
    right_input = input()
    if right_input == "Melbourne":
    	print("You went to Melbourne! Have fun with the koalas!")
    elif right_input == "Hawaii":
    	print("You went to Hawaii! Have fun with the dolphins!")

#end message
print("Hope you had a great trip!")