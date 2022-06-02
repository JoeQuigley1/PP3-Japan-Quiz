import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    print("Welcome to my Japan Quiz")
    print("Please enter one of the following options: \n")

    # Options for the user to choose from.
    print("If you want to play the game, press: 1")
    print("If you want to view the scoreboard, press: 2")
    print("If you want to quit, press: 3 \n")
    option = input("Please enter you choice here: ")

    if option == "1":
        print("Great let's play!\n")
    elif option == "2":
        print("Let's take a look at the scoreboard \n")
        display_scoreboard()
    elif option == "3":
        quit_game()
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
            print("Data Valid")
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
        if len(values) > 6:
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
    print("Logging username...")
    scoreboard_worksheet_update = SHEET.worksheet("scoreboard")
    scoreboard_worksheet_update.append_row([player_username])
    
    print("Username successfully updated. \n")

def display_scoreboard():
    scoreboard_worksheet_display = SHEET.worksheet("scoreboard").get_all_values()
    print(scoreboard_worksheet_display)


def quit_game():
    """
    Gives the user an option to exit the game menu
    """
    print("Thanks for using my quiz. \n")
    print("Please come back and try again soon!")


game_menu()
