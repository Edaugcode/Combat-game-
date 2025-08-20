import random

player_stats = {"health": 100,
                "damage_min": 5,
                "damage_max": 15,
                "gold": 200,
                "weapons": [],
                "armor": [],
                "xp": 0,
                "level": 1,
                "xp_mult": 1,
                "stat_points": 0,
                "username": ""}

# Monsters Below this line

goblin_stats = {"health": 75,
                "damage_min": 5,
                "damage_max": 10,
                "level": 1}
orc_stats = {"health": 150,
             "damage_min": 10,
             "damage_max": 25}
boss_stats = {"health": 300, 
              "damage_min": 30,
              "damage_max": 50}

# Weapons Below this line

basic_sword = {"damage_min": 3,
               "damage_max": 5,
               "cost": 5,
               "name": "basic sword"}
long_sword = {"damage_min": 5,
              "damage_max": 10,
              "cost": 15,
              "name": "long sword"}
schimitar_stats = {"damage_min": 15,
                   "damage_max": 25,
                   "cost": 25, 
                   "name": "schimitar"}

# Armor below this line

chainmail_stats = {"health": 25, 
                   "cost": 10,
                   "name": "chainmail"}
heavy_armor = {"health": 50,
               "damage": -5,
                "cost": 25,
                "name": "heavy armor"}
enchanted_armor = {"health": 100,
                    "damage_min": 15,
                    "damage_max": 20,
                    "cost": 50,
                    "name": "enchanted armor"}
