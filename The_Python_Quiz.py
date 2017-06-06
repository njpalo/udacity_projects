# just laying out all of my text and answers here.
# answers take the form of a list so I can call them by position later.
easy_text = '''
The Python programming language was created by ____1____ and first released
in the year ____2____. Python was designed to be more easily readable than 
other languages, for example using ____3____ indentation to define code blocks 
instead of curly braces or keywords. Python is intended to be ____4____ to use,
which is reflected in the name, a reference to ____5____ Python.
''' 

easy_answers = ['guido van rossum', '1991', 'whitespace', 'fun', 'monty']

medium_text = '''
Python uses the arithmetic operators: +, -, *, and / as usual, but introduces
____1____ for exponents. The = sign is used for assignment statements in Python,
so ____2____ is used for equality comparison. Other symbol combinations include:
____3____ for not equal to, ____4____ for greater than or equal to and ____5____
for less than or equal to. However, += is something different, called an ____6____
assignment statement, which allows: n = n + 1 to be written as n += 1.
'''

meduim_answers = ['**', '==', '!=', '>=', '<=', 'augmented']

hard_text = '''
If you enter the Statement: "____1____" into your Python interpreter, 
A set of 20 software principles, written by Tim ____2____, will be revealed.
The title of this list is: "The ____3____ of Python". Here are the first four
principles: ____4____ is better than ugly. Explicit is better than ____5____.
Simple is better than ____6____. ____6____ is better than complicated.
'''

hard_answers = ['import this', 'peters', 'zen', 'beautiful', 'implicit', 'complex']

# Now I put the texts and answers into these meta-lists so I can call them by position
# according to user input on level of difficulty. This will make it nice if I decide
# to add more levels of difficulty later.

text_list = [easy_text, medium_text, hard_text]

answer_list = [easy_answers, meduim_answers, hard_answers]

level_word = ['easy', 'medium', 'hard']

blanks = ['____0____', '____1____', '____2____', '____3____', '____4____', '____5____', '____6____']

welcome_menu = '''--------------------------------------------

Hello! Welcome to the Monty Quiz of Python!
Please choose a level of difficulty:

0 - easy

1 - medium

2 - hard

3 - exit game
'''

options = ['0', '1', '2', '3']
guesses = ['1', '2', '3', '4', '5']
max_attempts = 3

# now I'm going to make a little sub-function called "validate" to make sure 
# user input is in the list of available options.

def validate(data, dataset):
	attempts = 0
	while data not in dataset:
		if attempts == max_attempts:
			exit()
		print "invalid answer, tries remaining: ", 3 - attempts
		data = raw_input("answer: ")
		attempts += 1
	return data

# Let's define the game: I'll have two counters, "question" is the current question
# as we can progress through the game. "wrong" will track incorrect guesses so the 
# game can end when they hit the limit. "g" is the user entered number of guesses
# allowed per question. The rest of the game funtion is basically a more elaborate 
# version of the validate sub-function. 

def play_game(text, answers, difficulty, max_guesses):
	question = 1
	wrong = 0
	print "This is the", level_word[difficulty], "quiz:"
	print text
	while question <= len(answers):
		print "please fill in blank #", question
		answer = raw_input("answer: ")
		if answer.lower() in answers[question - 1]:
			print "correct !"
			text = text.replace(blanks[question], answer)
			print text
			question += 1
		else:
			wrong += 1
			print "incorrect! tries remaining: ", max_guesses - wrong
			if wrong == max_guesses:
				print "all your base are belong to us!"
				exit()
	if question == len(answers) + 1:
		print "you win the game!!!"

# OK, before we start the game, I need the user to enter a level of difficulty. 
# first I prompt them with the welcome menu, then the validate sub-funtion gives 
# them four chances to provide a valid response before it exits the program. 
# Then I need the user to enter "max_attempts" the number of guesses allowed per question 
# before the game begins. Same protocol for data entry as level of difficulty.
# finally, we play the game!

def set_game():
	print welcome_menu
	level = raw_input("answer: ")
	validate(level, options)
	level = int(level)
	if level == 3:
		exit()
	max_attempts = raw_input("please enter the number of guesses (between 1 and 5) you'd like to have for each question: ")
	validate(max_attempts, guesses)
	max_attempts = int(max_attempts)
	play_game(text_list[level], answer_list[level], level, max_attempts)

set_game()

# The number '3' on line 117 is not magic. It is a hard set option from the options 
# menu that allows the user to exit the game. 


	
	
	


