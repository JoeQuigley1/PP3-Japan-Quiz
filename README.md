
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

I thought it would be interesting to do a quiz on Japan. I spent over 4 years living and working in Japan, between Tokyo and Hiroshima. It is a country that will always be special to me.


# The Goal for this project

# UX

## User Goals 
+ To be amused by testing my facts and learn a variety of useful facts about Japan.

## User stories

+ As a user, I want to see my score and be able to compare it with others
+ As a user, I want to do a quiz that has an intuitive flow.
+ As a user, I want to learn something about Japan.
+ As a user, I want to have my knowledge tested.

## Site owner's Goals
+ To create a fun and somewhat challenging quiz.
+ To create a quiz with an intuative design.
+ To wrote code that follows best practice.
+ The code can be easily understood and adapted.

## Requirements 

+ Easy to play and understand
+ Should work on any device.
+ Should use libraries/API and be deployed to a cloud-based platform. 


# Features

## Game menu
The game menu has 3 options for the user.
+ - Play the game
+ - View the scoreboard
+ - Quit

### Play game 
 
 + Store a username in google sheets.
 + Do a quiz about Japan.
 + Cycle through 10 questions about Japan.


 ### View the scoreboard

+ - Displays the scoreboard which consists of the username and score.

### Quit

+ - This gives the user an option to leave the game.
+ - It contains a thank you message.

## End Game Menu
The end game menu has a similar menu to the Pregame menu except it offers a feedback choice.

### Feedback
 + - Give a rating out of 10 on the quiz.
 + - Comment on the quiz with a max of 200 characters.


    
# Technologies Used 

## Languages 

+ [HTML](https://en.wikipedia.org/wiki/HTML "HTML") - Provided in the Code Institute template
+ [CSS](https://en.wikipedia.org/wiki/CSS "CSS") - Provided in the Code Institute template
+ [JavaScript](http://en.wikipedia.org/wiki/JavaScript "JavaScript") - Provided in the Code Institute template
+ [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Python")

Python libraries and api used
- [Google auth](https://google-auth.readthedocs.io/en/master/index.html)
- [Pprint](https://docs.python.org/3/library/pprint.html)

## Data storage

The scoreboard which contains a username and their score is stored in Google Sheets using:

- [Google Drive API](https://developers.google.com/drive/api)
- [Google Sheet API](https://developers.google.com/sheets/api)


# credits 
https://www.rickshawtravel.co.uk/blog/10-fun-facts-japan/ Facts about Japan
https://www.buzzfeed.com/eviecarrick/cool-facts-about-japan
https://interacnetwork.com/fax-machines-in-japan-how-to-use-them/#:~:text=You%20might%20be%20thinking%2C%20%E2%80%9Cdo,won't%20let%20them%20go!

https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/  Quit function

https://stackoverflow.com/questions/52153215/how-do-i-define-limits-for-my-inputs-in-python rating parameters stack overflow

https://stackoverflow.com/questions/5997987/is-there-an-operator-to-calculate-percentage-in-python