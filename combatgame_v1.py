import random
playing = True
enemy_health = 100
player_health = 100
def health(damage, health):
    return health - damage

Open_menu = input("Fight or Exit: ")
Open_menu = Open_menu.lower()

while playing:
    healamt = random.randint(1, 5)
    dmgdone = random.randint(1, 15)
    enhealamt = random.randint(1, 5)
    endmgdone = random.randint(1, 15)
    if Open_menu == "fight":
        print("=====================================")
        print("Enemy has", enemy_health, "health")
        print("You have", player_health, "health")
        fight_option = input("Would you like to attack or heal?: ")
        fight_option = fight_option.lower()
        if fight_option == "attack":
            print("=====================================")
            print("You attack the enemy")
            missorhit = random.randint(1, 8)
            if missorhit == 8:
                print("You missed")
            else:
                print("You delt", dmgdone, "damage")
                enemy_health -= dmgdone
        elif fight_option == "heal":
            print("You healed for", healamt, "health")
            player_health += healamt
        print("======================================")
        print("It is the enemies turn")
        if enemy_health <= 20:
            print("The enemy heals for", enhealamt, "health")
            enemy_health += enhealamt
        else:
            print("The enemy attacks for", endmgdone, "health")
            player_health -= endmgdone
        if player_health == 0:
            print("=====================================")
            print("The enemy has won the battle")
            game_again = input("Would you like to play again?: ")
            game_again = game_again.lower() 
            if game_again == "yes":
                pass
            else:
                print("Thanks for playing")
                playing = False
        elif enemy_health == 0:
            print("=====================================")
            print("You have vanquished the enemy!")
            game_again = input("Would you like to play again?: ")
            game_again = game_again.lower() 
            if game_again == "yes":
                pass
            else:
                print("Thanks for playing:")
                playing = False