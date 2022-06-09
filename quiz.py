

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
    print("and a futher 26 cities, (referred to a shi in Japanese) outside of central Tokyo \n")

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




    #Question 3
    while True:
        print("In Japan it is polite to slurp when eating ramen. \n")
        print("Please answer T for True or F for False \n")

        answer3 = input("Please answer here: ")

        if answer3.upper() == "T" or answer3 == "True":
            print("\nCorrect! Well done!\n\n")
            score += 1
            break
        elif answer3.upper() == "F" or answer3 == "False":
            print("\nIncorrect answer!\n\n")

            break
        else:
            print(f"Invalid data: {answer3}. Please try again! \n")
    print(f"Answer: True \nYour score: {score}/10 \n")


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


    # Question 6
    while True:
        print("Japan sells more adult diapers than children's diapers.")
        print("Please enter T for True and F for False")

        answer6 = input("Please answer here: ")

        if answer6.upper() == "T" or answer6 == "True":
            print("\nCorrect! Well done!\n\n")
            score += 1
            break
        elif answer6.upper() == "F" or answer6 == "False":
            print("\nIncorrect answer!\n\n")

            break
        else:
            print(f"Invalid data: {answer6}. Please try again! \n")
    print(f"Answer: (T) True \nYour score: {score}/10 \n")
   

    # Question 7 
    while True:
        print("How many islands are there in Japan?")
        print("A: 500 B: 2500, C: 6800")
        
        answer7 = input("Please answer here: ")

        if answer7.upper() == "C" or answer7 == "6800":
            print("\nCorrect! Well done!\n\n")
            score += 1
            break
        elif answer7.upper() == "A" or answer7 == "500" or answer7.upper() == "B" or answer7 == "2500":
            print("\nIncorrect answer!\n\n")

            break
        else:
            print(f"Invalid data: {answer7}. Please try again! \n")
    print(f"Answer: (T) True \nYour score: {score}/10 \n")
    print("\n While it is widely known that Japan has many different prefectures with different climates, ")
    print("not many know that Japan is actually an island nation. It is, in fact, the largest East Asian island country, and the 4th largest island nation in the world. \n \n")
    

    #Question 8 
    while True:
        print("How many earthquakes are there in Japan every year?")
        print("A: 675 B: 350, C: 1500")

        answer8 = input("Please answer here: ")

        if answer8.upper() == "C" or answer8 == "1500":
            print("\nCorrect! Well done!\n\n")
            score += 1
            break
        elif answer8.upper() == "A" or answer8 == "675" or answer7.upper() == "B" or answer7 == "350":
            print("\nIncorrect answer!\n\n")

            break
        else:
            print(f"Invalid data: {answer7}. Please try again! \n")
    print(f"Answer: (T) True \nYour score: {score}/10 \n")
    
    #Qestion 9  
    while True:
        print("What happens when a train is delayed in Japan?")
        print("A:They give you a sugary snack on arrival")
        print("B:They issue a paper slip to notify your employer")
        print("C:They delivery complimentary tissues to your home")

        answer9 = input("Please answer here: ")

        if answer9.upper() == "B":
            print("\nCorrect! Well done!\n\n")
            score += 1
            break
        elif answer9.upper() == "A" or answer9.upper() == "C":
            print("\nIncorrect answer!\n\n")

            break
        else:
            print(f"Invalid data: {answer9}. Please try again! \n")
    print(f"Answer: (T) True \nYour score: {score}/10 \n")

    # question 10
    while True:
        print("Which of the following is the ruler of Japan have?")
        print("A:President")
        print("B:Emporer")
        print("C:King")

        answer10 = input("Please answer here: ")

        if answer10.upper() == "B" or answer10.capitalize() == "Emporer":
            print("\nCorrect! Well done!\n\n")
            score += 1
            break
        elif answer10.upper() == "A" or answer10.capitalize() == "President" or answer10.upper() == "C" or answer10.capitalize() == "King":
            print("\nIncorrect answer!\n\n")

            break
        else:
            print(f"Invalid data: {answer10}. Please try again! \n")
    print(f"Answer: (T) True \nYour score: {score}/10 \n")
    return score

    


