# Instructions
# ---------------------

# Section 1 Review

# 1. Variables and Constants
# Write a script where you:
# Define variables of different types: integer, float, string, boolean.
# Assign values to these variables and print their values.
# Experiment with constants by using all-uppercase variable names (e.g., PI = 3.14) and explain why constants are not enforced in Python but are a convention.
# 2. Data Types
# Write code snippets to check the data type of variables using type().
# Combine data types, such as concatenating strings with numbers using str().
# 3. Type Casting
# Experiment with casting values to int, float, str, and observe results for valid and invalid casts.

# ------------------------------------

# Section 2 Review 

# 1. Arithmetic Operators
# Write a calculator program that takes two inputs and performs operations: addition, subtraction, multiplication, division, modulus, floor division, and exponentiation.
# 2. Comparison Operators
# Write a program to compare two numbers and print whether they are equal, greater, or smaller.
# 3. Logical Operators
# Create a program that checks multiple conditions using and, or, and not.

name = input("\n Welcome to practice for sections 1 & 2 of python foundamentals! \n\n What is a good name for you? ")

programToRun = input(f"\n {name}, what lesson would you like to practice today from Section 1 (1.1, 1.2, 1.3)? ")

#class DifferentFunctions:

class DifferentReviews:
    @staticmethod
    def sectionOneOneReview():

        # -- Section 1.1 --

        a = 10
        b = 9.99
        c = "$9.99"
        d = True

        print(f"This is an integer: {a}")
        print(f"This is a float: {b}")
        print(f"This is a string: {c}")
        print(f"This is a boolean: {d}")

        userInput = input("Choose your poison: (a, b, c, d) ")

        if userInput.lower() == "a":
            print(a)
        elif userInput.lower() == "b":
            print(b)
        elif userInput.lower() == "c":
            print(c)
        elif userInput.lower() == "d":
            print(d)
        else:
            print(f"{name} choose one of the 4 options from the input question.")
    
    @staticmethod
    def sectionOneTwoReview():

        print(f"\n Ok {name}, \n It seems we are reviewing data types, and how concatination works with similar data types!")

        score = 0

        userInput0 = input(f"\n   -- Q1 -- \n\n (What is a string? \n\n Options: \n A) A value with quotations. \n B) A value with no quotations and that's a whole number. \n C) A value with decimals and no quations. \n D) True or False [with no quoations]. \n\n When you write the answer {name}, it's multiple choice; so make sure to write the letter option you think. ex: [a, b, c, d]) ")

        if userInput0.lower() == "a":
            print("\n Correct!")
            score += 1
        elif userInput0.lower() == "b":
            print(f"\n I'm sorry {name}, but this is incorrect. Try again next time.")
        elif userInput0.lower() == "c":
            print(f"\n I'm sorry {name}, but this is incorrect. Try again next time.")
        elif userInput0.lower() == "d":
            print(f"\n I'm sorry {name}, but this is incorrect. Try again next time.")
        else: 
            print(f"\n Make sure {name} you're writing your answer as a letter option (ex: a, b, c, d)")

        userInput1 = input(f"\n   -- Q2 -- \n\n (What is an integer? \n\n Options: \n A) A value with quotations. \n B) A value with no quotations and that's a whole number. \n C) A value with decimals and no quations. \n D) True or False [with no quoations]. \n\n When you write the answer {name}, it's multiple choice; so make sure to write the letter option you think. ex: [a, b, c, d]) ")

        if userInput1.lower() == "a":
            print(f"\n I'm sorry {name}, but this is incorrect. Try again next time.")
        elif userInput1.lower() == "b":
            print("\n Correct!")
            score += 1
        elif userInput1.lower() == "c":
            print(f"\n I'm sorry {name}, but this is incorrect. Try again next time.")
        elif userInput1.lower() == "d":
            print(f"\n I'm sorry {name}, but this is incorrect. Try again next time.")
        else: 
            print(f"\n Make sure {name} you're writing your answer as a letter option (ex: a, b, c, d)")

        userInput2 = input(f"\n   -- Q3 -- \n\n (What is a floating point number? \n\n Options: \n A) A value with quotations. \n B) A value with no quotations and that's a whole number. \n C) A value with decimals and no quations. \n D) True or False [with no quoations]. \n\n When you write the answer {name}, it's multiple choice so make sure to write the letter option you think. ex: [a, b, c, d]) ")

        if userInput2.lower() == "a":
            print(f"\n I'm sorry {name}, but this is incorrect. Try again next time.")
        elif userInput2.lower() == "b":
            print(f"\n I'm sorry {name}, but this is incorrect. Try again next time.")
        elif userInput2.lower() == "c":
            print("\n Correct!")
            score += 1
        elif userInput2.lower() == "d":
            print(f"\n I'm sorry {name}, but this is incorrect. Try again next time.")
        else: 
            print(f"\n Make sure {name} you're writing your answer as a letter option (ex: a, b, c, d)")
        
        userInput3 = input(f"\n   -- Q4 -- \n\n (What is a boolean? \n\n Options: \n A) A value with quotations. \n B) A value with no quotations and that's a whole number. \n C) A value with decimals and no quations. \n D) True or False [with no quoations]. \n\n When you write the answer {name}, it's multiple choice so make sure to write the letter option you think. ex: [a, b, c, d]) ")

        if userInput3.lower() == "a":
            print(f"\n I'm sorry {name}, but this is incorrect. Try again next time.")
        elif userInput3.lower() == "b":
            print(f"\n I'm sorry {name}, but this is incorrect. Try again next time.")
        elif userInput3.lower() == "c":
            print(f"\n I'm sorry {name}, but this is incorrect. Try again next time.")
        elif userInput3.lower() == "d":
            print("\n Correct!")
            score += 1
        else: 
            print(f"\n Make sure {name} you're writing your answer as a letter option (ex: a, b, c, d)")

        userInput4 = input(f"\n   -- Q5 -- \n\n ({name}, We're going to be doing some code! \n It will be plug and play, so follow along closely {name}. \n\n {name}, how would you concatinate this input value from an integer to a string? \n\n Here's the code: \n age = input('what is your age? ') \n \n print(______Your Answer_______) \n\n Options: \n\n A) | f'*curly brace* age variable *curly brace*'  \n B) | str(age)  \n C) | 'age'  \n D) | ' + age + '  \n\n Write your answer in multiple choice letter format.) ")

        if userInput4.lower() == "a":
            print(f"\n I'm sorry {name}, but this is incorrect. Try again next time.")
        elif userInput4.lower() == "b":
            print(f"\n Correct!")
            score += 1
        elif userInput4.lower() == "c":
            print(f"\n I'm sorry {name}, but this is incorrect. Try again next time.")
        elif userInput4.lower() == "d":
            print(f"\n I'm sorry {name}, but this is incorrect. Try again next time.")
        else: 
            print(f"\n Make sure {name} you're writing your answer as a letter option (ex: a, b, c, d)")
        
        print("\n\n Ok the quiz is finished [for now ;) ]")
        print(f"\n Here was your total score of correct answers: {score}")
        print(f" Thanks for playing {name}!")

        score = 0

    
    @staticmethod
    def sectionOneThreeReview():
        userInput = input(f"Choose your poison {name}: (a, b, c, d) ")

if programToRun == "1.1":
    DifferentReviews.sectionOneOneReview()
elif programToRun == "1.2":
    DifferentReviews.sectionOneTwoReview()
elif programToRun == "1.3":
    DifferentReviews.sectionOneThreeReview()
else:
    print(f" {name} choose section 1.1, 1.2, or 1.3. ")
