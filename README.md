
## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!

# Japan Quiz



# The Goal for this project

# UX

## User Goals 
+ To be amused by testing my facts and learn a variety of useful facts about Japan.

## Site owner's Goals
+ To create a fun and somewhat challenging quiz.
+ To create a quiz with an intuative design.
+ To wrote code that follows best practice.
+ The code can be easily understood and adapted.

## Requirements 

+ Easy to play and understand
+ Should work on any device.


# Features

## Game menu
The game menu has 3 options for the user.
1- Play the game
2- View the scoreboard
3- Quit

### Play game 

    
# Technologies Used 

## Languages 

+ [HTML](https://en.wikipedia.org/wiki/HTML "HTML") - Provided in the Code Institute template
+ [CSS](https://en.wikipedia.org/wiki/CSS "CSS") - Provided in the Code Institute template
+ [JavaScript](http://en.wikipedia.org/wiki/JavaScript "JavaScript") - Provided in the Code Institute template
+ [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Python")

Python libraries and api used
- [Google auth](https://google-auth.readthedocs.io/en/master/index.html)

## Data storage

The scoreboard which contains a username and their score is stored in Google Sheets using:

- [Google Drive API](https://developers.google.com/drive/api)
- [Google Sheet API](https://developers.google.com/sheets/api)


# credits 
https://www.rickshawtravel.co.uk/blog/10-fun-facts-japan/ Facts about Japan
https://www.buzzfeed.com/eviecarrick/cool-facts-about-japan

https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/  Quit function

https://stackoverflow.com/questions/52153215/how-do-i-define-limits-for-my-inputs-in-python rating parameters stack overflow