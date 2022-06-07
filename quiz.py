
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
            print( "\nCorrect! Well done!\n\n")
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
            print( "\nCorrect! Well done!\n\n")
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
        print("In Japan it is rude to slurp ramen when eating. \n")
        print("Please answer T for True or F for False \n")

        answer3 = input("Please answer here: ")

        if answer3.upper() == "F" or answer3 == "False":
            print("\nCorrect! Well done!\n\n")
            score += 1
            break
        elif answer3.upper() == "T" or answer3 == "True":
            print("\nIncorrect answer!\n\n")

            break
        else:
            print(f"Invalid data: {answer3}. Please try again! \n")
    print(f"Answer: False \nYour score: {score}/10 \n")
    print("\n loremupsumloremupsumloremupsumloremupsum")
    print("oremupsumloremupsumloremupsum \n")


    # Question 4f
    while True:
        print("In Japan which of these numbers are considered to be unlucky \n")
        print("A: 100, B: 13, C: 4 \n")

        answer4 = input("Please answer here: ")

        if answer4.upper() == "C" or answer4 == "4":
            print("\nCorrect! Well done!\n\n")
            score += 1
            break
        elif answer4.upper() == "A" or answer4 == "100" or answer4.upper() == "B" or answer4 == "13" :
            print("\nIncorrect answer!\n\n")

            break
        else:
            print(f"Invalid data: {answer4}. Please try again! \n")
    print(f"Answer: (C) 4 \nYour score: {score}/10 \n")
    print("loremupsumloremupsumloremupsumloremupsum")
    print("oremupsumloremupsumloremupsum")


    # Question 5
    while True:
        print("Which of the following meals do people eat for Christmas in Japan")
        print("A: Stinky Tofu, B: Tuna Sushi, C: KFC Chicken")

        answer5 = input("Please answer here: ")

        if answer5.upper() == "C" or answer5 == "KFC Chicken":
            print("\nCorrect! Well done!\n\n")
            score += 1
            break
        elif answer5.upper() == "A" or answer5 == "Stinky Tofu" or answer5.upper() == "B" or answer5 == "Tuna Sushi" :
            print("\nIncorrect answer!\n\n")

            break
        else:
            print(f"Invalid data: {answer5}. Please try again! \n")
    print(f"Answer: (C) KFC Chicken \nYour score: {score}/10 \n")
    print("loremupsumloremupsumloremupsumloremupsum")
    print("oremupsumloremupsumloremupsum")


    # Question 6
    while True:
        print("Japan sells more adult diapers than children's diapers.")
        print("Please enter T for True and F for False")

        answer5 = input("Please answer here: ")

        if answer5.upper() == "T" or answer5 == "True":
            print("\nCorrect! Well done!\n\n")
            score += 1
            break
        elif answer5.upper() == "F" or answer5 == "False":
            print("\nIncorrect answer!\n\n")

            break
        else:
            print(f"Invalid data: {answer5}. Please try again! \n")
    print(f"Answer: (T) True \nYour score: {score}/10 \n")
    print("loremupsumloremupsumloremupsumloremupsum")
    print("oremupsumloremupsumloremupsum")
        #return score


start_quiz()