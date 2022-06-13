import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
import quiz

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('pp3-quiz')

def game_menu():
    """
    Give the user options to initiate the game, quit 
    or view the scoreboard
    """
    # Options for the user to choose from.
    print("If you want to play the game, press: 1")
    print("If you want to view the scoreboard, press: 2")
    print("If you want to quit, press: 3 \n")
    option = input("Please enter you choice here: ")

    if option == "1":
        print("Great let's play!\n")
        get_player_username()
    elif option == "2":
        print("Let's take a look at the scoreboard \n")
        display_scoreboard()
    elif option == "3":
        print("\nThanks for using my quiz. \n")
        print("Please come back and try again soon!")
        quit()
    else:
        print("Invalid choice. Please choose 1, 2 or 3")
        return game_menu()

def get_player_username():
    """
    Gets the player to input a username
    """
    while True:
        print("Please enter a username.")
        print("The username should consist of between 3 and 6 characters.\n")
        print("Example:  Ken \n")

        player_username = input("Enter your username here: ")
        

        if check_username(player_username):
            print("Logging username...")
            update_scoreboard(player_username)
            break
    check_username(player_username)

def check_username(values):
    """
    Using try, checks the length and type of username to ensure that a
    valid username is chosen.
    """
    try:
        if len(values) < 3:
            raise ValueError(
                f"Username is too short! \nYour username only has {len(values)} character(s)"
            )
        if len(values) > 8:
            raise ValueError(
                f"Username is too long! \nYour username has {len(values)} characters"
            )
    except ValueError as e:
        print(f"Invalid data: {e}. Please try again! \n")
        return False

    return True
def update_scoreboard(player_username):
    """
    Update the scoreboard with the username and score
    """
    score = quiz.start_quiz()
    print("Logging score...")

    scoreboard_worksheet = SHEET.worksheet("scoreboard")
    scoreboard_worksheet.append_row([player_username, score])
    
    print("Scoreboard successfully updated. \n")


def display_scoreboard():
    """
    Displays the scoreboard before the player logs a username
    """
    scoreboard_worksheet_display = SHEET.worksheet("scoreboard").get_all_values()
    pprint(scoreboard_worksheet_display)
    print("\n \n")
    game_menu()

def end_game_scoreboard():
    """
    Displays the scoreboard after the user has played
    """
    print("Thank you for playing!")
    print("I hope you enjoyed...let's have a look at the scoreboard... \n \n")
    scoreboard_worksheet_display = SHEET.worksheet("scoreboard").get_all_values()
    pprint(scoreboard_worksheet_display)
    print("\n \n")

    
def end_game_menu():
    """
    Gives the user a different menu than the pregame menu
    """
    print("Thank you for playing \n")
    print("Please chose from the options below\n")
    print("1: Give some feedback ")
    print("2: Replay the Quiz") 
    print("3: Quit the game!")

    choice = input("\nPlease type here: ")
    
    if choice == "1":
        user_feedback()
    elif choice == "2":
        print("\nLet's Try again for fun!\n")
        quiz.start_quiz()
    elif choice == "3":
        quit()
    else:
        print("Invalid choice. Please choose 1, 2 or 3")
        return end_game_menu()

def user_feedback():
    """
    Takes and stores the user rating and any feedback in a google sheet
    """
    print("\nPlease rate the quiz out of 10")
    while True:
        rating = input("\nRating: ")
        try:
            user_rating = int(rating) 
        except ValueError:
            print("please enter a number")
            continue
        if 1 <= user_rating <= 10:
            print("Thanks for rating")
            break
        print("Please use a number between 1-10")

    print("\nPlease share your thoughts on the quiz. (200 characters max)")
    while True:
        suggestion = input("\nSuggestion: ")
        suggestion_len = len(suggestion)
        if len(suggestion) > 200:
            print(f"\nYour feedback was too long {suggestion_len} (200 chars max)")
            print("Please Try again")
        elif len(suggestion) < 200:
            print("\nFeedback is always important!\n")
            print("\nThanks for rating my quiz, I hope you enjoyed! \n \n")
            break

    scoreboard_worksheet = SHEET.worksheet("feedback")
    scoreboard_worksheet.append_row([rating, suggestion])

def main():
    game_menu()
    end_game_scoreboard()
    end_game_menu()
#BUGs
# Bug where scoreboard will go to menu before asking feedback after 
# What happens when there are too many scores in the scoreboard

print("Welcome to my Japan Quiz")
print("Please enter one of the following options: \n")

main()