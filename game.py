"""
Adventure Game
Author: Zack Davis
Version 1.0
Description:
This is a text-based adventure game where the player makes choices to navigate through a mysterious forest
"""
#Welcome message and introduction
print('Welcome, Adventurer!')
name = input('What is your name?')
# print(name , ', you have woken up in a strange castle. There is a dark presence here. Suddenly, you can hear something coming from outside the room!')

alive = 'true'
while 'true':
    print(name, ', you have woken up in a strange castle. There is a dark presence here. Suddenly, you can hear something coming from outside the room!')
    a_b = input('The sound is approaching fast. Do you (a) Hide or (b) Confront the presence? ').lower()
    if a_b == "a" or  a_b == "hide":
        print("You run and quickly slide under the bed just as a giant winged demon burst through the door, narrowly avoiding discovery")
        print('The demon looks around with great intent like it was expecting to find something....')

        c_d = input("But you see a brief moment to make a move do you (a) Dart towards the window to try and make an escape or (b) Continue hiding and hope you are not discovered?").lower()
        if c_d == "a":
            print('''You quickly rush towards the window and dive through it. You hear the demon yell "There is no escape" and the world fades to black around you. You wake up in the castle again. 
                            The nightmare continues''')
            continue
        elif c_d == "b":
            print(name , 'You have chosen to remain hidden. As you continue to watch the demon he seems to stop. He found what he is looking for. Its a sword of some kind!')
            print('As the demon is distracted by his find you see the key to door. He left it on the desk beside you!')

            g_h = input('Do you (a) steal the key and try to slip out undetected or (b) distract the demon by throwing the key and steal the sword?').lower()

            if g_h == "a":
                print("You steal the key and quietly make your way towards the door")
                print('The demon hears you unlock it and snaps around but you are too fast and you dart out the door')
                print('The demon does not give chase. He just yells "There is no escape for you!" your world then fades to black around you. You wake up in the castle again')
                print('                  The nightmare continues')
                continue
            elif g_h == "b":
                print("You grab the key and throw it across the room. Startling the demon.")
                print('You quickly dash towards the sword when the demon sees you. You dive and grab the pommel and when you do the memories of the blade flow into you')
                print('The "Dreamsever" sword. Powerful enough to slash through dreams and even powerful enough to harm the God of nightmares himself, Phobetor')
                print('Phobetor draws his sword into a clash with yours. You trade blow after blow until you see your opening and throw a powerful slash!')
                print('*Just misses*')
                print('The god fades away with a laugh. I know when I am outmatched but dreams are endless and I am a god.')
                print('This is my domain.')
                print('You will be back night after night and you cannot defeat me forever.')
                print('Your world fades to black as you awake in your bed. Clutching the dreamsever. You have defeated your sleeping nightmare this time.')
                print('Now', name , 'can you handle the waking one?')
                exit()

    elif a_b == 'b':
        print(name , 'You have decided to show your bravery and confront whatever is coming towards you')
        print('BOOM!! A giant winged demon burst through the door')
        e_f = input('As you stand there terrified do you (a) try to talk to the demon or (b) quickly attack the demon').lower()
        if e_f == 'b':
            print('You throw yourself at the demon fighting for the knife on his belt. You somehow manage to wrangle it away and slash the demon.')
            print('The knife just passes through the demon like a dream. It then grabs you by the neck and says "There is no escape for you.')
            print('Your world fades to black and you wake up back in the castle')
            print('      The nightmare continues....')
            continue
        elif e_f == 'a':
            print('You attempt to talk to the demon and figure out what is going on here')
            print('The winged beast ignores you and starts aggressively attacking you')
            print('You see that the demon left the door open but you dont want to leave without knowing what is going on')
            i_j = input('Do you (a) try to make an escape through the open door or (b) continue to try and reason with the demon?')
            if i_j == 'a':
                print('You dodge one last attack and make a scramble towards the door.')
                print('You are able to make it through the door and as you do the door slams shut behind you!')
                print('You hear the demon yell from behind the door "There is no escape for you!"')
                print('You wake up back in the castle.')
                print('         The nightmare continues......')
            elif i_j == 'b':
                print('You continually dodge the demon attacks trying to communicate with the demon.')
                print('You tell him "This all feels like a dream".')
                print('This comment stirs something in the demon as he lets up attacking for just a moment.')
                print('But as one moment went by he swings again striking you down.')
                print('As you lay there your world fades to black. You wake up back in the castle...')
                print('          The nightmare continues........')
                continue

