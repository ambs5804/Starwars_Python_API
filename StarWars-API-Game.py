"""
This program asks the user for a number and uses this to retrieve a Star Wars character as the users 'battle opponent'.
The program then asks the user for their height, and compares this against their selected characters height to determine
the winner.
The user then gets a response based on the outcome of the battle.
Finally, a file is created containing the list of films the selected character has appeared in.
"""

import requests
import time  # I'm using the time module to include pauses for dramatic effect

# Ask the user for a number
# Use the format method to add the user input to the API url to choose our character
print('GREETINGS, JEDI. \nTHE FATE OF THE GALAXY IS IN YOUR HANDS. \nIN ORDER TO SURVIVE AND SAVE US ALL, YOU MUST DEFEAT YOUR OPPONENT. \nGOOD LUCK, JEDI. YOU WILL NEED IT.')
character_id = int(input('\nCHOOSE A NUMBER BETWEEN 1 & 15 TO DETERMINE YOUR OPPONENT: '))
url_star_wars = 'https://swapi.dev/api/people/{}'.format(character_id)
response = requests.get(url_star_wars)  # Request the character data from the API
data = response.json()

# Print the name of the character chosen (in uppercase to match the dialogue)
print('AH! YOU HAVE CHOSEN THE INFAMOUS', data['name'].upper())  # here we pull the name from the list in the API
time.sleep(2)  # 2-second delay for dramatic effect
print('\nLET US SEE HOW YOU STACK UP TO YOUR OPPONENT.')
time.sleep(2)  # 2-second delay for dramatic effect

# Ask the user for their height and define this as a variable
user_height = int(input('\nDECLARE YOUR HEIGHT, JEDI (CM): '))

time.sleep(1)  # 1-second delay for dramatic effect
print('HM! INTERESTING...')
time.sleep(2)  # 2-second delay for dramatic effect
print('\nNOW, THERE IS NO TIME TO WASTE.')
time.sleep(1.5)  # 1.5-second delay for dramatic effect
print('THE BATTLE IS UPON US.')
time.sleep(1.5)  # 1.5-second delay for dramatic effect
print('YOU HAVE 5 SECONDS TO PREPARE.')
time.sleep(1.5)  # 1.5-second delay for dramatic effect
print('USE THEM WELL.')
time.sleep(1.5)  # 1.5-second delay for dramatic effect


# Create a function for a countdown timer
def countdown_timer(seconds):
    while seconds > 0:
        print(seconds)
        time.sleep(1)  # 1-second delay
        seconds -= 1

    print("LET THE BATTLE BEGIN!!")


countdown_timer(5)  # call our countdown timer function

time.sleep(5)  # 5-second delay for dramatic effect

# An if function that determines the winner by comparing the user's inputted height with the height of the opposing character taken from the API
if user_height > int(data['height']):
    print('\nCONGRATULATIONS JEDI.')
    time.sleep(1.5)  # 1.5-second delay for dramatic effect
    print(data['name'].upper() + ' IS NO MATCH FOR YOU.')
    time.sleep(1.5)  # 1.5-second delay for dramatic effect
    print('YOU WERE LUCKY.')
    time.sleep(1.5)  # 1.5-second delay for dramatic effect
    print('THIS TIME.')
    time.sleep(3)  # 3-second delay for dramatic effect
    print('\nWE HAVE RECOVERED A LIST OF VIDEO FOOTAGE OF ' + data['name'].upper() + '.')
    print('THIS HAS BEEN BEAMED TO YOUR DEVICE. \nWATCH AND RELISH IN YOUR VICTORY. \nWHILE YOU STILL CAN.')
else:
    print('\nBAD NEWS JEDI.')
    time.sleep(1.5)  # 1.5-second delay for dramatic effect
    print('YOU ARE NO MATCH FOR ' + data['name'].upper())
    time.sleep(1.5)  # 1.5-second delay for dramatic effect
    print('YET.')
    time.sleep(3)  # 3-second delay for dramatic effect
    print('\nWE HAVE RECOVERED A LIST OF VIDEO FOOTAGE OF ' + data['name'].upper() + '.')
    print('THIS HAS BEEN BEAMED TO YOUR DEVICE. \nWATCH THIS FOOTAGE TO PREPARE FOR YOUR NEXT BATTLE. \nDO NOT LET US DOWN AGAIN.')


# Create a new .txt file named after the character
# Include some text and use a 'for' loop to list all the films the character has appeared in
with open('VIDEO FOOTAGE OF ' + data['name'].upper() + '.txt', 'a') as text_file:
    text_file.write(data['name'].upper() + ' HAS BEEN SEEN IN THE BELOW VIDEO FILES. \nWATCH WITH CAUTION.')


# We want the film names, instead of the URLs that are listed on the character's resource.
# So we use this URL to create another request in order to get the film titles, and list these in the new file using a for loop.
film_appearance = data['films']
for film in film_appearance:
    film_url = requests.get(film)
    films = film_url.json()
    with open('VIDEO FOOTAGE OF ' + data['name'].upper() + '.txt', 'a') as text_file:
        text_file.write('\n' + films['title'])
