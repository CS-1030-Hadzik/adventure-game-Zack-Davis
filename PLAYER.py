import random
class Player:
    def __init__(self, name,location):
        self.name = name
        self.location = location
        self.player_health = 100
        self.inventory = []

    def check_lose(self):
        if self.player_health <= 0:
            print(f'Your health has reached 0 and you have now died....')
            quit()

    def add_inventory(self,item):
        self.inventory.append(item)
        print(f'{item} is now in your inventory')

    def show_inventory(self):
        if self.inventory:
            for item in self.inventory:
                print(f'-{item}')
        else:
            print('You do not have anything in your inventory....')

    def check_location(self):
        print(self.location)


    def check_win(self):
        if 'TREASURE' in self.inventory and 'MAGICAL HERB' in self.inventory:
            print(f'{self.name}, you have collected this islands greatest treasures and rarest herbs. You have won!')
            quit()

    def take_damage(self, damage):
        self.player_health -= damage
        print(f'{self.name}, you have taken damage!! You now have {self.player_health} remaining!')
        self.check_lose()

    def stand_still(self):
        print('Your inability to make a decision makes you flustered.')
        self.take_damage(10)

    def move_location(self, choice1, choice2):
        while True:
            choose = input(f'{self.name} would you like to go to {choice1} or {choice2}?\n').strip().lower()
            if choose == choice1.lower():
                print(f'{self.name}, you have chosen {choice1}')
                self.move(choice1)
                break
            elif choose == choice2.lower():
                print(f'{self.name}, you have chosen {choice2}')
                self.move(choice2)
                break
            else:
                print(f'{self.name} please choose between {choice1} or {choice2}')

    def move(self,new_location):
        self.location = new_location.lower()

    def explore(self):
        if self.location == 'beach':
            self.explore_beach()
            return
        if self.location == 'dark woods':
            self.explore_dark_woods()
            return
        if self.location == 'mountain pass':
            self.explore_mountain_pass()
            return
        if self.location == 'cave':
            self.explore_cave()
            return
        if self.location == 'hidden valley':
            self.explore_hidden_valley()
            return

    def explore_beach(self):
        print('There is nothing of interest here on the beach maybe we should explore elsewhere')
        self.move_location('Dark Woods', 'Mountain Pass')

    def explore_dark_woods(self):
        print(f'You find yourself walking in the dark area of the woods.')
        if not "MAP" in self.inventory:
            print(f'You stumble across an abandoned camp and find a odd MAP')
            add = input('Would you like to add the MAP to your inventory? 1.Yes 2.No\n')
            if add == '1':
                self.add_inventory('MAP')
                print("You study the MAP.\n It looks like it leads to a valley beyond the mountains!")
            elif add == '2':
                print('You do not take the MAP')
            else:
                print('Please choose between 1 or 2')

        else:
            print('You come across the abandoned camp.\n There seems to be nothing else of use here. ')

        if not 'LANTERN' in self.inventory:
            print('You find a path that splits. Where would you like to go?')
            self.move_location("Beach","Mountain Pass")

        if 'LANTERN' in self.inventory:
            print('You find a path that splits. The lantern lights the way to a new area. Where would you like to go?')
            self.move_location("Mountain Pass","Cave")

    def explore_mountain_pass(self):
        print('The mountain pass is dangerous and there is no room for a mis-step here.')
        if not "LANTERN" in self.inventory:
            print(f'You come across an old mine shaft that is completely caved in.\n By the entrance there is an old lantern. ')
            add = input('Would you like to add the LANTERN to your inventory? 1.Yes 2.No')
            if add == '1':
                self.add_inventory('LANTERN')
                print("You light the LANTERN.\n I wonder if this could help me further explore the dark woods?")
            elif add == '2':
                print('You do not take the LANTERN')
            else: print('Please choose between 1 or 2')

        else:
            print('You come across the caved in mine shaft.\nThere seems to be nothing else of use here. ')

        if not 'MAP' in self.inventory:
            print('The pass is too dangerous to continue without knowing where you are going.\n You must turn around and explore elsewhere.')
            self.move_location("Beach","Dark Woods")

        if 'MAP' in self.inventory:
            print('With the map in hand you can continue forward or you can explore elsewhere')
            self.move_location("Dark Woods","Hidden Valley")

    def explore_cave(self):
        print('The LANTERN illuminates the entrance to the cave')
        while True:
            choice = input("Would you like to go deeper into the cave? 1.Yes 2.No")
            if choice == '1':
                print('You try to explore deeper parts of the cave')
                roll = random.randint(0,1)
                if roll == 0:
                    print('You get very lost in the cave and it mentally and physically drains you')
                    self.take_damage(30)
                    continue
                elif roll == 1:
                    if not 'TREASURE' in self.inventory:
                        print('You reach the very back of the cave to a big door.\n You push it open and inside.....\n a TREASURE!!!')
                        add = input('Would you like to add the TREASURE to your inventory? 1.Yes 2.No')
                        if add == '1':
                            self.add_inventory('TREASURE')
                            print("You fill your pockets with the TREASURE.\n Your pockets never seem to be filled and you were able to take the entire pile\n You then retrace your steps to the dark woods.")
                            self.check_win()
                            self.move('dark woods')
                            break

                        elif add == '2':
                            print('You do not take the TREASURE and return to the dark woods.')
                            self.move('dark woods')
                            break

                        else:
                            print('Please choose between 1 or 2')

                    else:
                        print('You already looted the treasure room....')
                        self.move('dark woods')
                        break
            elif choice == '2':
                print("You're too scared to explore the cave and return to the dark woods")
                self.take_damage(10)
                self.move('dark woods')
                break

            else:
                print('Please choose between 1 or 2')

    def explore_hidden_valley(self):
        print('The map leads you through the mountain pass into a hidden valley.')
        if not 'MAGICAL HERB' in self.inventory:
            print('The valley is vast but you can see something in the middle')
            add = input('You find a giant herb. You dont know what it is but the plant feels magical.... \nWould you like to add the MAGICAL HERB to your inventory? 1.Yes 2.No')
            if add == '1':
                self.add_inventory('MAGICAL HERB')
                print("You feel a sense of peace and good health now.")
                self.check_win()
                print("You make your way back to the mountain pass")
                self.move('mountain pass')

            elif add == '2':
                print('You do not take the MAGICAL HERB and make your way back to the mountain pass')
                self.move('mountain pass')
 
            else:
                print('Please choose between 1 or 2')
        else:
            print('There seems to be nothing else of use here.\nYou make your way back to the mountain pass')
            self.move('mountain pass')

    def start_game(self):
        while True:
            game_choice = input(f'{self.name}, you are currently at {self.location} what would you like to do \n1.Explore\n2.Stand Still\n3.Check Health\n4.Display Inventory\n')
            if game_choice == '1':
                self.explore()
            elif game_choice == '2':
                self.stand_still()
            elif game_choice == '3':
                print(f'{self.name}, you currently have {self.player_health} HP.')
            elif game_choice == '4':
                self.show_inventory()
            else:
                print('Please choose between 1,2,3,4........')


