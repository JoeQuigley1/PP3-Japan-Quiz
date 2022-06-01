import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('pp3-quiz')


# def game_menu():
"""
Give the user options to initiate the game, quit 
or view the scoreboard
"""

def get_player_username():
    """
    Gets the player to input a username
    """
    print("Please enter a username.")
    print("The username should be at least 3 letters.\n")
    print("Example:  Ken \n")

    player_username = input("Enter your username here: ")
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
    except ValueError as e:
        print(f"Invalid data: {e}. Please try again! \n")
        



get_player_username()