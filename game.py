from PLAYER import Player

"""
Adventure Game
Author: Zack Davis
Version 1.0
Description:
This is a text-based adventure game where the player makes choices to navigate through a mysterious forest
"""
starting_location = 'beach'
print('Welcome, Adventurer!')
player_name = input('What is your name?\n')
player = Player(player_name,starting_location)
print("You wake up dazed and confused on a beach....\nYou have a feeling you should be looking for something.....")
player.start_game()
