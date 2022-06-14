score = 0

def quest_1():
    
    while True:
        print("\n\nWhat is the capital of Japan? \n")
        print("A: Beijing, B: Tokyo, C: Seoul")

        answer1 = input("\nPlease answer here: ")

        if answer1.upper() == "B" or answer1.capitalize() == "Tokyo":
            print("\nCorrect! Well done!\n\n")
            global score
            score += 1
            break
        elif answer1.upper() == "A" or answer1.upper() == "C":
            print("\nIncorrect answer!\n\n")
            break
        elif answer1.capitalize() == "Beijing":
            print("\nIncorrect answer!\n\n")
            break
        elif answer1.capitalize() == "Seoul":
            print("\nIncorrect answer!\n\n")
            break
        else:
            print(f"Invalid data: {answer1}. Please try again! \n")
    print(f"Answer: Tokyo \nYour score: {score}/10 \n")
    print("\n\nTokyo Metropolis is a large metropolitan area,")
    print("made up of 23 cities (called 'ku' in Japanese) in central Tokyo")
    print("and a futher 26 cities, (referred to a 'shi' in Japanese)\n")
    print("Loading next question...")
    

def quest_2():
    while True:
        print("\nWhat is the population of Japan? \n")
        print("A: 126 million, B: 94 million, C: 77 million ")

        answer2 = input("\nPlease answer here: ")

        if answer2.upper() == "A" or answer2 == "126 million":
            print("\nCorrect! Well done!\n\n")
            global score
            score += 1
            break
        elif answer2.upper() == "B" or answer2.upper() == "C":
            print("\nIncorrect answer!\n\n")
            break
        elif answer2.capitalize() == "94 million":
            print("\nIncorrect answer!\n\n")
            break
        elif answer2.capitalize() == "77 million":
            print("\nIncorrect answer!\n\n")
            break
        else:
            print(f"Invalid data: {answer2}. Please try again! \n")
    print(f"Answer: 126 million \nYour score: {score}/10 \n")
    print("\n\n Japan has one of the largest populations in the world.")
    print("However it is also one of the fastest declining populations.")
    print("There are many factors that contribute to this..")
    print("most prominently being the high demograohic of elderly people.\n\n")
    print("Loading next question...")
    

# Score is a UnboundLocalError: local variable 'score' referenced before assignment
# Need to figure out how to 
def myMain():
   
    quest_1()
    quest_2()





myMain()
