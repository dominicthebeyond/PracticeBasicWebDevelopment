greet = input("Hello! Would you like to play some quizzing today? ")

if greet.lower() == "yes":
    print("Ok bet bro. Let's get it! ")

    def directions():
        # This is a function that will print if this "if statement" executes.
        return print("For this quiz, you will need: 1) a brain, 2) commitment and determination, 3) to finish the quiz.")
    
    print(directions())

    class Program():
        # This will run the program after the directions.
        typeOfQuiz = input("What would you like to quiz about today (Computers, Code, Or Graphic Design)?: ")
        
        if typeOfQuiz.lower() == "computers":
            print("You have selected the computers section of this interactive quiz. Let's begin!")

            q1 = input ("What is the CPU?")
            
            if q1.lower() == "central processing unit":
                print("Correct!")
            else: 
                print("I'm sorry, but this was incorrect. Try again next time!")
            
            q2 = input ("What is the GPU?")
            
            if q2.lower() == "graphics processing unit":
                print("Correct!")
            else: 
                print("I'm sorry, but this was incorrect. Try again next time!")
            
            q3 = input ("What is the PSU?")
            
            if q3.lower() == "power supply unit":
                print("Correct!")
            else: 
                print("I'm sorry, but this was incorrect. Try again next time!")
            
            q4 = input ("What is RAM?")
            
            if q4.lower() == "random access memory":
                print("Correct!")

                print("RAM is ")
            else: 
                print("I'm sorry, but this was incorrect. Try again next time!")
            
            
            
else:
    print("Alright. Come back whenever you want to do some quizzing! ")

print("quiz ended")