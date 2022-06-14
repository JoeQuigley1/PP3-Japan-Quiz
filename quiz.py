"""
Import selection
"""
import time
from termcolor import colored

score = 0
total_questions = 10


def quest_1():
    """
    Contains the data for question 10
    """
    while True:
        print("\nQ1. What is the capital of Japan?\n")
        print("A: Beijing, B: Tokyo, C: Seoul")

        answer1 = input("\nPlease answer here:\n")

        if answer1.upper() == "B" or answer1.capitalize() == "Tokyo":
            print("\nCorrect answer!")
            global score
            score += 1
            break
        elif answer1.upper() == "A" or answer1.upper() == "C":
            print("\nIncorrect answer!")
            break
        elif answer1.capitalize() == "Beijing":
            print("\nIncorrect answer!")
            break
        elif answer1.capitalize() == "Seoul":
            print("\nIncorrect answer!")
            break
        else:
            print(f"Invalid data: {answer1}. Please try again! \n")
    print(colored(f"Answer: Tokyo \nYour score: {score}/10 \n"), 'blue')
    print("\nTokyo Metropolis is a large metropolitan area,")
    print("made up of 23 cities (called 'ku' in Japanese) in central Tokyo")
    print("and a futher 26 cities, (referred to a 'shi' in Japanese)\n")
    print("Loading next question...")


def quest_2():
    """
    Contains the data for question 2
    """
    while True:
        print("\nQ2. What is the population of Japan?")
        print("A: 126 million, B: 94 million, C: 77 million ")

        answer2 = input("\nPlease answer here:\n")

        if answer2.upper() == "A" or answer2 == "126 million":
            print("\nCorrect answer!")
            global score
            score += 1
            break
        elif answer2.upper() == "B" or answer2.upper() == "C":
            print("\nIncorrect answer!")
            break
        elif answer2.capitalize() == "94 million":
            print("\nIncorrect answer!")
            break
        elif answer2.capitalize() == "77 million":
            print("\nIncorrect answer!")
            break
        else:
            print(f"Invalid data: {answer2}. Please try again! \n")
    print(f"Answer: 126 million \nYour score: {score}/10 \n")
    print("\n\nJapan has one of the largest populations in the world.")
    print("However it is also one of the fastest declining populations.")
    print("There are many factors that contribute to this..")
    print("most prominently being the high demograohic of elderly people.\n\n")
    print("Loading next question...")


def quest_3():
    """
    Contains the data for question 3
    """
    while True:
        print("\nQ3.")
        print("Almost half of all Japanese households have a fax machine")
        print("\nPlease answer T for True or F for False")

        answer3 = input("Please answer here:\n")

        if answer3.upper() == "T" or answer3 == "True":
            print("\nCorrect answer!")
            global score
            score += 1
            break
        elif answer3.upper() == "F" or answer3 == "False":
            print("\nIncorrect answer!")

            break
        else:
            print(f"Invalid data: {answer3}. Please try again! \n")
    print(f"Answer: True \nYour score: {score}/10 \n")
    print("According to the Times, almost 100% of businesses and 45%")
    print("of households in Japan still have fax machines!")
    print("")
    print("Loading next question...")
    time.sleep(3)


def quest_4():
    """
    Contains the data for question 4
    """
    while True:
        print("\nQ4.")
        print("In Japan which of these numbers are considered to be unlucky")
        print("\nA: 100, B: 13, C: 4")

        answer4 = input("\nPlease answer here:\n")

        if answer4.upper() == "C" or answer4 == "4":
            print("\nCorrect answer!")
            global score
            score += 1
            break
        elif answer4.upper() == "A" or answer4 == "100":
            print("\nIncorrect answer!")
            break
        elif answer4.upper() == "B" or answer4 == "13":
            print("\nIncorrect answer!")
            break
        else:
            print(f"Invalid data: {answer4}. Please try again! \n")
    print(f"Answer: (C) 4 \nYour score: {score}/10 \n")
    print("\n\nUnlucky numbers in Japanese often derive from their readings")
    print("The number 4 is sometimes called 'shi' which...")
    print("also unfortunatley sounds like the word for death.\n")
    print("Many East Asian countries share similar")
    print("superstitions around numbers.\n\n")
    print("Loading next question...")
    time.sleep(3)


def quest_5():
    """
    Contains the data for question 5
    """
    while True:
        print("\nQ5. What do Japanese people eat for Christmas?\n")
        print("\nA: Stinky Tofu, B: California Roll, C: KFC Chicken")

        answer5 = input("\nPlease answer here:\n")

        if answer5.upper() == "C" or answer5 == "KFC Chicken":
            print("\nCorrect answer!")
            global score
            score += 1
            break
        elif answer5.upper() == "A" or answer5 == "Stinky Tofu":
            print("\nIncorrect answer!")
            break
        elif answer5.upper() == "B" or answer5 == "Tuna Sushi":
            print("\nIncorrect answer!")
            break
        else:
            print(f"Invalid data: {answer5}. Please try again! \n")
    print(f"Answer: (C) KFC Chicken \nYour score: {score}/10 \n")
    print("\n\nChristmas is not widely celebrated in Japan like in the West.")
    print("People go shopping and couples go out for a Christmas meal. Turkey")
    print("which is usually eaten at Christmas, is difficult to source")
    print("in Japan. For this reason KFC is an extremely popular alternative.")
    print("KFC restaurants will ONLY serve those who have booked in advance.")
    print("Loading next question...")
    time.sleep(3)


def quest_6():
    """
    Contains the data for question 6
    """
    while True:
        print("\nQ6. Japan sells more adult diapers than children's diapers.")
        print("\nPlease enter T for True and F for False")

        answer6 = input("\nPlease answer here:\n")

        if answer6.upper() == "T" or answer6 == "True":
            print("\nCorrect answer!")
            global score
            score += 1
            break
        elif answer6.upper() == "F" or answer6 == "False":
            print("\nIncorrect answer!")
            break
        else:
            print(f"Invalid data: {answer6}. Please try again! \n")
    print(f"Answer: (T) True \nYour score: {score}/10 \n")
    print("Japan has a very large ageing population.")
    print("One third of the Japanese population is aged over 65.")
    print("This is attributed to many things such as the high standard")
    print("of living, low emigration and a declining birth rate.")
    time.sleep(3)


def quest_7():
    """
    Contains the data for question 7
    """
    while True:
        print("\nQ7. How many islands are there in Japan?")
        print("A: 500 B: 2500, C: 6800")
        answer7 = input("\nPlease answer here:\n")

        if answer7.upper() == "C" or answer7 == "6800":
            print("\nCorrect answer!")
            global score
            score += 1
            break
        elif answer7.upper() == "A" or answer7 == "500":
            print("\nIncorrect answer!")
            break
        elif answer7.upper() == "B" or answer7 == "2500":
            print("\nIncorrect answer!")
            break
        else:
            print(f"Invalid data: {answer7}. Please try again! \n")
    print(f"Answer: (C) \nYour score: {score}/10 \n")
    print("\n While it is widely known that Japan it a large country,")
    print("with different climates, ")
    print("not many know that Japan is the 4th largest island nation ")
    print("in the world. It has 4 main islands but also contains upwards of")
    print("6000 smaller islands.")
    time.sleep(3)


def quest_8():
    """
    Contains the data for question 8
    """
    while True:
        print("\nQ8. How many earthquakes are there in Japan every year?")
        print("A: 675 B: 350, C: 1500")

        answer8 = input("\nPlease answer here:\n")

        if answer8.upper() == "C" or answer8 == "1500":
            print("\nCorrect answer!")
            global score
            score += 1
            break
        elif answer8.upper() == "A" or answer8 == "675":
            print("\nIncorrect answer!")
            break
        elif answer8.upper() == "B" or answer8 == "350":
            print("\nIncorrect answer!")
            break
        else:
            print(f"Invalid data: {answer8}. Please try again! \n")
    print(f"Answer: (C) \nYour score: {score}/10 \n")
    print("Japan is located along the 'Pacific Ring of Fire' and is ")
    print("one of the most Earthquake prone nations in the world. ")
    print("However most of the 1500 earthquakes go unnoticed as they are")
    print("too weak to be felt by the average person.")
    time.sleep(3)


def quest_9():
    """
    Contains the data for question 9
    """
    while True:
        print("\nQ9. What happens when a train is delayed in Japan?")
        print("\nA:They give you a sugary snack on arrival")
        print("\nB:They issue a certificate to notify your employer")
        print("\nC:They delivery complimentary tissues to your home")

        answer9 = input("\nPlease answer here:\n")

        if answer9.upper() == "B":
            print("\nCorrect answer!")
            global score
            score += 1
            break
        elif answer9.upper() == "A" or answer9.upper() == "C":
            print("\nIncorrect answer!")

            break
        else:
            print(f"Invalid data: {answer9}. Please try again! \n")
    print(f"Answer: (B) \nYour score: {score}/10 \n")
    print("Punctuality is exceptionally important in all spheres of society.")
    print("This is evident in the amazing public transport system.")
    print("Trains are almost always on time to the minute. So much so that")
    print("When a train is delayed, you can get a train delay certificate")
    time.sleep(3)


def quest_10():
    """
    Contains the data for question 10
    """
    while True:
        print("\nQ10. Which of the following is the ruler of Japan have?")
        print("A:President")
        print("B:Emporer")
        print("C:King")

        answer10 = input("\nPlease answer here:\n")

        if answer10.upper() == "B" or answer10.capitalize() == "Emporer":
            print("\nCorrect answer!")
            global score
            score += 1
            break
        elif answer10.upper() == "A" or answer10.capitalize() == "President":
            print("\nIncorrect answer!")
            break
        elif answer10.upper() == "C" or answer10.capitalize() == "King":
            print("\nIncorrect answer!")
            break
        else:
            print(f"Invalid data: {answer10}. Please try again! \n")
    print(f"Answer: (B) \nYour score: {score}/10 \n")
    print("The Emporer of Japan is the head of the Japanese nation.")
    print("He is a ceremonial figurehead.")
    print("It is commonly accepted that there has been an Emporer in Japan")
    print("for more the 1500 years. All descended from one family. ")
    time.sleep(3)


def get_percentage(score, total_questions):
    """
    Gets a percentage to show the user at the end of the quiz.
    """
    end_percent = 100 * round(score)/round(total_questions)
    return print(f"\nYou got {end_percent}% ")


def start_quiz():
    """
    This intiates the quiz and calls  all of the
    questions in order.
    Calls the get_percentage function and returns the score.
    """
    quest_1()
    quest_2()
    quest_3()
    quest_4()
    quest_5()
    quest_6()
    quest_7()
    quest_8()
    quest_9()
    quest_10()

    get_percentage(score, total_questions)
    return score
