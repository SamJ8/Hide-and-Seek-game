import time
import random
import inquirer
from colorama import Fore, init
init(autoreset=True)


print(Fore.LIGHTBLACK_EX + '''
      

██╗  ██╗██╗██████╗ ███████╗     █████╗ ███╗   ██╗██████╗     ███████╗███████╗███████╗██╗  ██╗
██║  ██║██║██╔══██╗██╔════╝    ██╔══██╗████╗  ██║██╔══██╗    ██╔════╝██╔════╝██╔════╝██║ ██╔╝
███████║██║██║  ██║█████╗      ███████║██╔██╗ ██║██║  ██║    ███████╗█████╗  █████╗  █████╔╝ 
██╔══██║██║██║  ██║██╔══╝      ██╔══██║██║╚██╗██║██║  ██║    ╚════██║██╔══╝  ██╔══╝  ██╔═██╗ 
██║  ██║██║██████╔╝███████╗    ██║  ██║██║ ╚████║██████╔╝    ███████║███████╗███████╗██║  ██╗
╚═╝  ╚═╝╚═╝╚═════╝ ╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝     ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
                                                                                             
''')





hiding_places_list = ["Bedroom 1", 
                      "Bedroom 2", 
                      "Bedroom 3", 
                      "Bedroom 4", 
                      "Living room", 
                      "Dining room", 
                      "Kitchen", 
                      "Garage", 
                      "Shed", 
                      "Cupboard under the stairs"]

#! ^ made my hiding places list

print(Fore.LIGHTYELLOW_EX + "\nWelcome to the hide and seek game!\n") #! welcome message
while True: #! while loop to ensure user types in a name
        user_name = input(Fore.MAGENTA + "To start please enter your name!: ").capitalize()
        if user_name:
            print(Fore.MAGENTA + f"\nHello {user_name}!\n")
            break #! will break out of loop once user types in name
        else:
            print(Fore.RED + "Please enter valid name.") #! error message will keep displaying if condition not met
        
hiding_places = [
    inquirer.List("hiding_place",
                    message = Fore.YELLOW + "It's time to pick your hiding place! Select from the list below!",
                    choices = hiding_places_list
    ),
] #! incorporarted the inquirer library to help make a nicer list for the user to go through and select
    
users_choice = inquirer.prompt(hiding_places)
users_hiding_place = users_choice["hiding_place"] #! this will be the variable that has stored the users choice from the hiiding place list
print(Fore.LIGHTMAGENTA_EX + "Your hiding place is: " + users_hiding_place + "\n") #! will display the choice the user made
      
print(Fore.LIGHTRED_EX + "You'll now have 10 seconds to hide! Once the counter reaches 0, I'll be coming to get you!")
print(input(Fore.YELLOW + "\nPress enter when you're ready! ")) 

for seconds in range(10, -1, -1): #! countdown will be shown when the user hits enter
        print(seconds)
        time.sleep(1)

print(Fore.LIGHTRED_EX + "\nREADY OR NOT, HERE I COME!")
for seconds in range(2, -1, -1):
            time.sleep(1)

attempts = 0 #! attempts set to 0 for the computer
computer = random.choice(hiding_places_list) #! imported the random library so the computer will be making a random choice from the list
remaining_hiding_places = hiding_places_list.copy() #! made a copy from the hiding place list

while attempts < 5:
    computer = random.choice(remaining_hiding_places) 
    remaining_hiding_places.remove(computer) #! used the .remove method so it won't be able to make the same choice twice and will remove the item from the list when it's been randomly picked

    if computer == users_hiding_place: #! if the computer matches the users hiding place, program ends
        print(Fore.LIGHTRED_EX + "YES! I've found you!")
        break
    else: 
        print(Fore.LIGHTRED_EX + f"\nHmm, not in {computer}.\n") #! if computer doesn't randomly choose our users choice then message will print
        for seconds in range(2, -1, -1):
            time.sleep(1) #! timer inbetween computer checking the rooms
        attempts +=1 #! for every place that computer checks, the attempts will go up by 1

if attempts == 5: #! if attempts hits 5 then program ends and print message is displayed
        print(Fore.GREEN + "You win! I can't find you!")

#! end of program