
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

        if answer1.upper() ==  "B" or answer1.capitalize() == "Tokyo":
            print( "\nYou got the right answer! Well done!\n\n")
            score += 1 
            break
        elif answer1.upper() == "A" or answer1.upper() == "C" or answer1.capitalize() == "Beijing" or answer1.capitalize() == "Seoul":
            print("\nIncorrect answer!\n\n")
            break
        else:
            print(f"Invalid data: {answer1}. Please try again! \n" )
    print(f"Answer: Tokyo \nYour score: {score}/10 \n")
    print("Tokyo Metropolis is a large metropolitan area that is made up of 23 cities, (called ku in Japanese) in central Tokyo")
    print("and a futher 26 cities, (referred to a shi in Japanese) outside of central Tokyo")

    #Question 2
    while True:
        print("What is the population of Japan? \n")
        print("A: 126 million, B: 94 million, C: 77 million ")

        answer2 = input("Please answer here: ")

        if answer2.upper() ==  "A" or answer2 == "126 million":
            print( "\nYou got the right answer! Well done!\n\n")
            score += 1
            break
        elif answer2.upper() == "B" or answer2.upper() == "C" or answer2 == "94 million" or answer2 == "77 million":
            print("\nIncorrect answer!\n\n")
            break
        #Need to find a way to get this to work
        #elif answer1.upper() == "94 million" or answer1.upper() == "77 million":
            print("\nIncorrect answer!\n\n")
            break
        else:
            print(f"Invalid data: {answer2}. Please try again! \n" )
    print(f"Answer: 126 million \nYour score: {score}/10 \n")
    print("loremupsumloremupsumloremupsumloremupsum")
    print("oremupsumloremupsumloremupsum")



    #Question 3
    while True:
        print("In Japan it is rude to make noise when eating.")
        print("Please answer T for True or F for False")

        answer3 = input("Please answer here: ")

        if answer3.upper() == "F":
            print("\nYou got the right answer! Well done!\n\n")
            score += 1
            break
        elif answer3.upper() == "T":
            print("\nIncorrect answer!\n\n")

            break
        else:
            print(f"Invalid data: {answer3}. Please try again! \n")
    print(f"Answer: False \nYour score: {score}/10 \n")
    print("loremupsumloremupsumloremupsumloremupsum")
    print("oremupsumloremupsumloremupsum")


    # Question 4f



        #return score


start_quiz()