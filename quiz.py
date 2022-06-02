
# This file will hold the play the quiz function and the questions


# questions = {
   # "What is the capital of Japan?: ": "B"
   # "What is the population of Japan?: ":  "A"
    #"In Japan it is rude to make noise when eating.:": "F"
    #"How many prefecture are there in Japan?:": "C"
    #"Which of these are NOT Japanese?:":  "C"
    #"Japan has the most vending machines in the world.:": "T"}


# Using a similar structure to the check_username the start_quiz function,
# gives the question and checks to see if the answer is true
def start_quiz():

    score = 0



    #Question 1
    while True:
        print("What is the capital of Japan? \n")
        print("A: Beijing, B: Tokyo, C: Seoul")

        answer1 = input("Please answer here: ")

        if answer1.upper() ==  "B" or answer1 == "Tokyo":
            print( "\nYou got the right answer! Well done!\n\n")
            score += 1
            break
        elif answer1.upper() == "A" or answer1.upper() == "C":
            print("\nIncorrect answer!\n\n")
            break
        else:
            print(f"Invalid data {answer1}. Please try again! \n" )
    print("Answer: Tokyo \n \n")
    print("Tokyo Metropolis is a large metropolitan area that is made up of 23 cities (called ku in Japanese) in central Tokyo")
    print("and a futher 26 cities (referred to a shi in Japanese) outside of central Tokyo")



