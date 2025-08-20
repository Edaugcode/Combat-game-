import random
import stats
def damage_calc():
    dmg_range = random.randint(stats.player_stats["damage_min"], stats.player_stats["damage_max"])
    return dmg_range
def monstai(min_dmg, max_dmg, health):
    if health >= 50:
        dmg_range = random.randint(min_dmg, max_dmg)
        return {"action": "damage", "value": dmg_range}
    elif health < 50:
        die_roll = random.randint(1, 100)
        if die_roll >= 60:
            monstheal = random.randint(1, 10)
            return {"action": "heal", "value": monstheal}
        elif die_roll < 60:
             dmg_range = random.randint(min_dmg, max_dmg)
        return {"action": "damage", "value": dmg_range}
def xp_calc():
    checking = True
    while checking:
        lvl_up_xp = stats.player_stats["xp_mult"] * 100 * (stats.player_stats["level"] * 0.75)
        if stats.player_stats["xp"] >= lvl_up_xp:
            stats.player_stats["xp"] -= lvl_up_xp
            stats.player_stats["level"] += 1
            return True
        elif stats.player_stats["xp"] < lvl_up_xp:
            checking = False
            return False
def plyer_heal():
    die_roll = random.randint(8, 20)
    return die_roll

def bssply_heal():
    die_roll = random.randint(15, 50)
    return die_roll

def boss_ai():
    if stats.boss_stats["health"] >= 200:
        def boss_attack():
            dmg_range = random.randint(stats.boss_stats["damage_min"], stats.boss_stats["damage_max"])
            return {"action": "attack", "damage": dmg_range}
    elif stats.boss_stats["health"] < 200:
        die_roll = random.randint(1, 100)
        if die_roll >= 80:
            boss_heal = random.randint(1, 60)
            return{"action": "heal", "amount": boss_heal}
        elif die_roll < 80:
            boss_dmg = boss_attack()
            return {"action": "attack", "damage": boss_dmg}
    elif stats.boss_stats["health"] < 100:
        die_roll = random.randint(1, 100)
        if die_roll >= 60:
            boss_dmg1 = boss_attack
            return {"action": "attack", "damage": boss_dmg1}
        else: 
            boss_heal = random.randint(1, 60)
            return{"action": "heal", "amount": boss_heal}



            

def shop():
    while True:
        print("========================================")
        playershp1 = input("What wares would you like to view? Armor, Weapons, inventory, or Exit: ")
        playershp1 = playershp1.lower()
        if playershp1 == "weapons":
            print("========================================")
            print("You have", stats.player_stats["gold"], "gold")
            print("1. Basic sword (+2 - 5 dmg) 5 gold")
            print("2. Long sword (+5 - 10 dmg) 15 gold")
            print("3. Schimitar (+15 - 20 dmg) 25 gold")
            print("4. Back")
            playershpopt1 = int(input("Enter choice here: "))
            if playershpopt1 == 4:
                continue
            elif playershpopt1 == 1:
                if stats.player_stats["gold"] >= 5:
                    pass
                else:
                    print("You dont have enough money to buy this you only have", stats.player_stats["gold"], "gold")
                    continue
                if stats.basic_sword["name"] in stats.player_stats["weapons"]:
                    print("You already have this in your inventory")
                    continue
                elif stats.long_sword["name"] in stats.player_stats["weapons"]:
                    print("You already have a better weapon in your inventory")
                    continue
                elif stats.schimitar_stats["name"] in stats.player_stats["weapons"]:
                    print("You already have a better weapon in your inventory")
                    continue
                else:
                    print("The Basic Sword has been added to your inventory!")
                    stats.player_stats["gold"] -= 5
                    stats.player_stats["weapons"].append(stats.basic_sword["name"])
                    stats.player_stats["damage_min"] += stats.basic_sword["damage_min"]
                    stats.player_stats["damage_max"] += stats.basic_sword["damage_max"]
            elif playershpopt1 == 2:
                if stats.player_stats["gold"] >= 15:
                    pass
                else:
                    print("You dont have enough money to buy this you only have", stats.player_stats["gold"], "gold")
                    continue
                if stats.long_sword in stats.player_stats["weapons"]:
                    print("You already have this in your inventory")
                elif stats.schimitar_stats["name"] in stats.player_stats["weapons"]:
                    print("You already have a better weapon in your inventory")
                    continue
                else:
                    print("The Long sword has been added to your inventory!")
                    stats.player_stats["gold"] -= 15
                    stats.player_stats["weapons"].append(stats.long_sword["name"])
                    stats.player_stats["damage_min"] += stats.long_sword["damage_min"]
                    stats.player_stats["damage_max"] += stats.long_sword["damage_max"]
                    if stats.basic_sword["name"] in stats.player_stats["weapons"]:
                        stats.player_stats["weapons"].remove(stats.basic_sword["name"])
                        stats.player_stats["damage_min"] -= stats.basic_sword["damage_min"]
                        stats.player_stats["damage_max"] -= stats.basic_sword["damage_max"]
            elif playershpopt1 == 3:
                if stats.player_stats["gold"] >= 25:
                    pass
                else:
                    print("You dont have enough money to buy this you only have", stats.player_stats["gold"], "gold")
                if stats.schimitar_stats in stats.player_stats["weapons"]:
                    print("You already have this in your inventory")
                else:
                    print("The Schimitar has been added to your inventory!")
                    stats.player_stats["gold"] -= 5
                    stats.player_stats["weapons"].append(stats.schimitar_stats["name"])
                    stats.player_stats["damage_min"] += stats.schimitar_stats["damage_min"]
                    stats.player_stats["damage_max"] += stats.schimitar_stats["damage_max"]
                    if stats.basic_sword["name"] in stats.player_stats["weapons"]:
                        stats.player_stats["weapons"].remove(stats.basic_sword["name"])
                        stats.player_stats["damage_min"] -= stats.basic_sword["damage_min"]
                        stats.player_stats["damage_max"] -= stats.basic_sword["damage_min"]
                    if stats.long_sword["name"] in stats.player_stats["weapons"]:
                        stats.player_stats["weapons"].remove(stats.long_sword["name"])
                        stats.player_stats["damage_min"] -= stats.long_sword["damage_min"]
                        stats.player_stats["damage_max"] -= stats.long_sword["damage_max"]
        
        elif playershp1 == "armor":
            print("========================================")
            print("You have", stats.player_stats["gold"], "gold")
            print("1. Chainmail Armor (+25 health) 10 gold")
            print("2. Heavy Armor (+50 health, -5 damage) 25 gold")
            print("3. Enchanted Armor (+100 health, +15 - 25 dmg) 50 gold")
            print("4. Back")
            shpopt2 = int(input("Enter choice here: "))
            if shpopt2 == 1:
                if stats.player_stats["gold"] >= 10:
                    pass
                else:
                    print("You dont have enough money to buy this you only have", stats.player_stats["gold"], "gold")
                    continue
                if stats.chainmail_stats in stats.player_stats["armor"]:
                    print("You already have this in your inventory")
                elif stats.heavy_armor["name"] in stats.player_stats["armor"]:
                    print("You already have a better piece of armor in your inventory")
                    continue
                elif stats.enchanted_armor["name"] in stats.player_stats["armor"]:
                    print("You already have a better piece or armor in your inventory")
                    continue
                else:
                    print("The Chainmail Armor has been added to your inventory!")
                    stats.player_stats["gold"] -= 10
                    stats.player_stats["armor"].append(stats.chainmail_stats["name"])
                    stats.player_stats["health"] += stats.chainmail_stats["health"]
            elif shpopt2 == 2:
                if stats.player_stats["gold"] >= 25:
                    pass
                else:
                    print("You dont have enough money to buy this you only have", stats.player_stats["gold"], "gold")
                    continue
                if stats.heavy_armor in stats.player_stats["armor"]:
                    print("You already have this in your inventory")
                if stats.enchanted_armor in stats.player_stats["armor"]:
                    print("You already have a better piece of armor in your inventory")
                    continue
                else:
                    print("The Heavy Armor has been added to your inventory!")
                    stats.player_stats["gold"] -= 10
                    stats.player_stats["armor"].append(stats.heavy_armor["name"])
                    stats.player_stats["health"] += stats.heavy_armor["health"]
                    stats.player_stats["damage"] += stats.heavy_armor["damage"]
                    if stats.chainmail_stats["name"] in stats.player_stats["armor"]:
                        stats.player_stats["armor"].remove(stats.chainmail_stats["name"])
                        stats.player_stats["health"] -= stats.chainmail_stats["health"]
                    
            elif shpopt2 == 3:
                if stats.player_stats["gold"] >= 35:
                    pass
                else:
                    print("You dont have enough money to buy this you only have", stats.player_stats["gold"], "gold")
                    continue
                if stats.enchanted_armor in stats.player_stats["armor"]:
                    print("You already have this in your inventory")
                else:
                    print("The Enchanted Armor has been added to your inventory!")
                    stats.player_stats["gold"] -= 10
                    stats.player_stats["armor"].append(stats.enchanted_armor["name"])
                    stats.player_stats["health"] += stats.enchanted_armor["health"]
                    stats.player_stats["damage_min"] += stats.enchanted_armor["damage_min"]
                    stats.player_stats["damage_max"] += stats.enchanted_armor["damage_max"] 
                    if stats.chainmail_stats["name"] in stats.player_stats["armor"]:
                        stats.player_stats["armor"].remove(stats.chainmail_stats["name"])
                        stats.player_stats["health"] -= stats.chainmail_stats["health"]
                    if stats.heavy_armor["name"] in stats.player_stats["armor"]:
                        stats.player_stats["armor"].remove(stats.heavy_armor["name"])
                        stats.player_stats["health"] -= stats.heavy_armor["health"]
                        stats.player_stats["damage"] -= stats.heavy_armor["damage"]
            elif shpopt2 == 4:
                continue
        elif playershp1 == "inventory":
            print("Weapon: ", stats.player_stats["weapons"])   
            print("Armor: ", stats.player_stats["armor"])
        elif playershp1 == "exit": 
            break 
def adventure():
    while True: 
        print("========================================")
        plyad1 = input("Monsters, Stats, Boss, or Exit: ")
        plyad1 = plyad1.lower()
        if plyad1 == "exit":
            break
        if plyad1 == "monsters":
            print("========================================")
            print("Who would you like to fight?")
            plyad2 = input("Goblin or Orc: ")
            plyad2 = plyad2.lower()
            
            
            if plyad2 == "goblin":
                original_health = stats.player_stats["health"]
                gob_og_health = stats.goblin_stats["health"]
                print("========================================")
                print("You encounter a goblin and engage it in battle.")
                goblin_living = True
                stats.player_stats["health"] = original_health
                stats.goblin_stats["health"] = gob_og_health
                while goblin_living:
                    print("========================================")
                    print("The enemy has", stats.goblin_stats["health"], "health remaining")
                    print("You have", stats.player_stats["health"], "health remaining")
                    print("What would you like to do?")
                    gobin1 = input("Attack, Heal, or Run: ")
                    gobin1 = gobin1.lower()
                    
                    if gobin1 == "attack":
                        print("========================================")
                        gobclc = damage_calc()
                        print("You did", gobclc, "damage!")
                        stats.goblin_stats["health"] -= gobclc
                        input("Press enter when you are ready to go on: ")
                        print("========================================")
                    if stats.goblin_stats["health"] <= 0:
                        print("========================================")
                        print("The goblin has been defeated!")
                        print("You have been awarded with 100 xp and 5 gold")
                        stats.player_stats["xp"] += 100
                        stats.player_stats["gold"] += 5
                        stats.goblin_stats["health"] = gob_og_health
                        stats.player_stats["health"] = original_health
                        gobxpck = xp_calc()
                        if gobxpck == True:
                            print("========================================")
                            print("You have leveled up!")
                            stats.player_stats["xp_mult"] += .5
                            goblin_living = False
                    
                    elif gobin1 == "heal":
                            helamt = plyer_heal()
                            print("========================================")
                            print("You healed for", helamt, "health")
                            stats.player_stats["health"] += helamt
                    
                    elif gobin1 == "run":
                            goblin_living = False  
                    if stats.player_stats["health"] <= 0:
                        print("========================================") 
                        print("You have lost!")
                        print("You have not gained or lost anything, you just need to get better ❌")
                        input("Press enter to continue")
                        goblin_living = False
                    if goblin_living == True:
                        gob_act = monstai(stats.goblin_stats["damage_min"], stats.goblin_stats["damage_max"], stats.goblin_stats["health"])
                        if gob_act["action"] == "damage":
                            print("========================================")
                            print("The goblin attacked for", gob_act["value"], "damage!")
                            stats.player_stats["health"] -= gob_act["value"]
                            input("Press enter when you are ready to go on")
                        elif gob_act["action"] == "heal":
                            print("========================================")
                            print("The goblin healed for", gob_act["value"], "health!")
                            stats.goblin_stats["health"] += gob_act["value"]
                            input("Press enter when you are ready to go on")
            
            
            elif plyad2 == "orc":      
                original_health = stats.player_stats["health"]
                orc_og_health = stats.orc_stats["health"]
                print("========================================")
                print("You encounter an orc and engage it in battle.")
                orc_living = True
                stats.player_stats["health"] = original_health
                stats.orc_stats["health"] = orc_og_health
                while orc_living:
                    if stats.player_stats["health"] <= 0:
                        print("========================================")
                        print("You lost to the orc. 👎💥")
                        print("Try buying new gear in the shop. You have", stats.player_stats["gold"], "gold")
                        input("Press enter to continue")
                        stats.player_stats["health"] = original_health
                        stats.orc_stats["health"] = orc_og_health
                        orc_living = False
                    if orc_living:
                        print("========================================")
                        print("The enemy has", stats.orc_stats["health"], "health remaining")
                        print("You have", stats.player_stats["health"], "health remaining")
                        print("What would you like to do?")
                        gobin1 = input("Attack, Heal, or Run: ")
                        gobin1 = gobin1.lower()
                       
                        if gobin1 == "attack":
                            print("========================================")
                            gobclc = damage_calc()
                            print("You did", gobclc, "damage!")
                            stats.orc_stats["health"] -= gobclc
                            input("Press enter when you are ready to go on: ")
                            print("========================================")
                    if stats.orc_stats["health"] <= 0:
                        print("========================================")
                        print("The orc has been defeated!")
                        print("You have been awarded with 150 xp and 10 gold")
                        stats.player_stats["xp"] += 150
                        stats.player_stats["gold"] += 10
                        stats.orc_stats["health"] = orc_og_health
                        stats.player_stats["health"] = original_health
                        gobxpck = xp_calc()
                        if gobxpck == True:
                            print("========================================")
                            print("You have leveled up!")
                            orc_living = False
                    
                    elif gobin1 == "heal":
                            helamt = plyer_heal()
                            print("========================================")
                            print("You healed for", helamt, "health")
                            stats.player_stats["health"] += helamt
                    
                    elif gobin1 == "run":
                            orc_living = False   
                    if orc_living == True:
                        gob_act = monstai(stats.orc_stats["damage_min"], stats.orc_stats["damage_max"], stats.orc_stats["health"])
                        if gob_act["action"] == "damage":
                            print("========================================")
                            print("The orc attacked for", gob_act["value"], "damage!")
                            stats.player_stats["health"] -= gob_act["value"]
                            input("Press enter when you are ready to go on")
                        elif gob_act["action"] == "heal":
                            print("========================================")
                            print("The orc healed for", gob_act["value"], "health!")
                            stats.orc_stats["health"] += gob_act["value"]
                            input("Press enter when you are ready to go on")
        elif plyad1 == "stats":
            print("========================================")
            print("These are you current stats")        
            print("Name: ", stats.player_stats["username"])  
            print("Damage range:", stats.player_stats["damage_min"], "-", stats.player_stats["damage_max"])
            print("Health:", stats.player_stats["health"])
            print("Level:", stats.player_stats["level"])
            input("Press enter to continue")
            continue
        elif plyad1 == "boss":
            print("========================================")
            print("This is the final fight of this game.")
            print("You only get 1 attempt at this fight so be sure you are prepared.")
            bossin1 = input("Are you sure you would like to go on?: ")    
            bossin1 = bossin1.lower()
            if bossin1 == "no":
                print("========================================")
                print("Wise choice. Prepare and come back.") 
                input("Press enter to continue")   
            elif bossin1 =="yes":
                print("========================================")
                print("Boss: So you were finally brave enough to face me.")
                input("Enter to continue")
                print("========================================")
                print(stats.player_stats["username"],": Its time for your rein to come to an end, and i'm here to make sure that happens.")
                input("Enter to continue")
                print("========================================")
                print("Boss: We shall see about that.")
                input("Enter to continue")
                boss_living = True
                while boss_living:
                    if stats.player_stats["health"] <= 0:
                        print("========================================")
                        print("Boss: Pitiful effort.")
                        input("Press enter to continue")
                        print("========================================")
                        print("Your journey has come to an unfortunate end, and it seemes there will be no happy ending in this story.")
                        input("Press enter to continue.")
                        print("========================================")
                        print("Failure ending completed.")
                        input("Press enter to close the game.")
                        print("Thank you for playing")
                        quit()
                    else:
                        print("========================================")
                        print("The boss has", stats.boss_stats["health"], "health and you have", stats.player_stats["health"], "health")
                        print("What would you like to do?")
                        bossin2 = input("Attack or Heal: ")
                        bossin2 = bossin2.lower()
                        if bossin2 == "heal": 
                            helamt2 = bssply_heal()
                            print("========================================")
                            print("You healed for", helamt2, "health")
                            stats.player_stats["health"] += helamt2
                            print("Boss: Running and hiding to heal, you stand no chance.")
                            input("Press enter to continue")
                        elif bossin2 == "attack":
                            print("========================================")
                            print("Boss: I highly dount your pitiful attacks will even scatch me.")
                            pbdmg = damage_calc()
                            stats.boss_stats["health"] -= pbdmg
                            print("You hit for", pbdmg, "damage!")
                            input("Press Enter to continue")
                            print("========================================")
                    if stats.boss_stats["health"] <= 0:
                            print("========================================")
                            print("Boss: No, this cant be happening!")
                            print("Boss: This isn't how it was supposed to go!")
                            input("Enter to continue")
                            print("========================================")
                            print(stats.player_stats["username"], ": ...")
                            input("Enter to continue")
                            print("========================================")
                            print("Choose wisely.")
                            playerend1 = input("Kill or Spare: ")
                            playerend1 = playerend1.lower()
                            if playerend1 == "kill":
                                print("========================================")
                                print(stats.player_stats["username"], ": This is how it was supposed to go, and im going to make sure nobody else gets hurt by you. Never again.")
                                input("Enter to continue")
                                print("========================================")
                                print("No-Mercy ending completed.")
                                input("Press enter to close the game.")
                                print("Thank you for playing")
                                quit()
                            if playerend1 == "spare":
                                print("========================================")
                                print(stats.player_stats["username"], ": I believe that you can change for the better. I will let you go for now, but if I see any sign of you not trying to change im coming back")
                                input("Enter to continue")
                                print("========================================")
                                print("To be continued in a later update...")
                                input("Press enter to close the game.")
                                print("Thank you for playing")
                                quit()
                    #else:
                        #bssdmg = boss_ai()
                       # if bssdmg["action"] == "attack":
                     #       print("========================================")
                      #      print("You have been hit for", bssdmg["damage"], "damage")
                      #      stats.player_stats["health"] -= bssdmg["damage"]
                      #      input("Press enter to continue")
                       # elif bssdmg["action"] == "heal":
                       #     print("========================================")
                       #     print("The boss has healed for", bssdmg["amount"], "health")
                       #     stats.boss_stats["health"] += bssdmg["amount"]
                        #    input("Press enter to continue")




                

print("========================================")
username = input("Please enter your character's name (no numbers): ")
stats.player_stats["username"] = username

print("========================================")
print("Welcome to Turn Of Fate")
playeropt1 = input("What would you like to do? Play or Exit: ")
playeropt1 = playeropt1.lower()

if playeropt1 == "play":
    while True:
        print("========================================")
        playeropt2 = input("What would you like to do? Shop, Adventure, or Quit: ")
        playeropt2 = playeropt2.lower()
        if playeropt2 == "shop":
            shop()     
        elif playeropt2 == "adventure":
            adventure() 
        elif playeropt2 == "exit":
            exit()
        else:
            print("========================================")
            print("Please enter a valid option.")
            