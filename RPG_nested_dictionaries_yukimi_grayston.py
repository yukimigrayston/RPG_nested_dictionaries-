#RPG nested dictionaries - Yukimi Grayston

#This code prints out all of the class, location, action and inventory information

#Dictionary for classes
classes = {
    'fighter' : {
    'description' : 'The fighter is the main attacker of the party.', 
    'actions' : ['shield', 'sword_attack'],
    },
    
    'mage' : {
    'description' : 'The mage is the main spell caster of the party.', 
    'actions' : ['fireball', 'magic_missile'],
    },
    
    'druid' : {
    'description' : 'The Druid is the main healer of the party.', 
    'actions' : ['vine trap', 'heal'],
    }, 
    }

#Dictionary for actions 
actions = {
    'fighter_actions' : {
        'attack_1' : 'Sheild: The sheild blocks attacks from enemies.',
        'attack_2' : 'Sword Attack: The sword deals 50 damage to enemies.',
        },
    'druid_actions' : {
        'attack_1' : 'Heal: The heal spell can heal 50 damage points.',
        'attack_2' : 'Vine trap: The vines trap the enemy making the unable to move and attack.',
        },
    'mage_actions' : {
        'attack_1' : 'Magic Missile: Three magic missles shoot out, each doing 20 damage.',
        'attack_2' : 'Fireball: A massive ball of fire is launches doing 60 damage, may injure any creature nearby.',
        }, 
    }

#Dictionary for locations 
locations = {
    'beginning_room' : {
        'items' : 'Key for trapped door.',
        'room_description' : 'The room is dark and damp with a faint light comming from the hallway.', 
        },
     'beginning_hallway' : {
        'items' : 'none',
        'room_description' : 'The hall is dimly lit with a torch being the only source of light.',
        },
     'left_code_room' : {
        'items' : 'Code for left room in the fork in the road room',
        'room_description' : 'A mostly empty room, there are numbers carved into the walls.', 
        },
     'goblin_room' : {
        'items' : 'none',
        'room_description' : '4 goblins attack the players who interrupt their card game.', 
        },
    'fork_in_the_road' : {
        'items' : 'none',
        'room_description' : 'This room leads to three hallways', 
        },
    'left_room' : {
        'items' : 'If the code is used the player can recieve treasure',
        'room_description' : 'A door locks this room, if the correct code is entered the player can leave the dungeon and recieve a smal treasure chest.',
        },
    'middle_room' : {
        'items' : 'none',
        'room_description' : 'A pit trap is in this room, if a player walks in they immediatly fall inside.',
        },
    'right_room' : {
        'items' : 'Treasure pile',
        'room_description' : 'There is a trapped door, the player can open it if they choose, a pile of gold awaits them below but so does a monster.', 
        },
    }
#Dictionary for inventory 
inventory = {
    'room_code' : {
        'use' :'Unlocks the room with the small treasure chest.',
        'item_description' :'The numbers one the walls are 4265, this must be a code.',
        },
           'trapped_door_key' : {
        'use' :'Opens the trapped door in right_room.',
        'item_description' :'The key is small and rusted.',
        },
           'small_treasure_chest' : {
        'use' :'The player recieves, 50 gold coins and 5 gems.',
        'item_description' :'The chest is small but hefty.',
        },
           'treasure_pile' : {
        'use' :'The player recieves 1000 gold coins, 50 gems, and 5 pieces of jewlery.',
        'item_description' :'The glittering mound underneath the great beast beckons for you, though you may not be able to carry all the riches.',
        },
    }

#Prints off class information
for role, options in classes.items():
    print(f"\n{role.title()}")
    print(f"Description: {options['description']}")
    for acts in options['actions']:
        print("Actions: " + acts.title())

#Prints off action information
for attacks, attack_description in actions.items():
    print(f"\n{attacks.title()}")
    print(attack_description['attack_1'])
    print(attack_description['attack_2'])

#Prints off location information
for location, location_description in locations.items():
    print(f'\n{location.title()}')
    print(f"Items: {location_description['items']}")
    print(f"Description: {location_description['room_description']}")
    
#Prints off inventory information   
for item, item_desc in inventory.items():
    print(f'\n{item.title()}')
    print(f"Use: {item_desc['use']}")
    print(f"Description: {item_desc['item_description']}")

    
    
