"""Create a character."""
import shelve
import math

def character_creation():
    """Create a character."""
    # Initialize Character Options
    points_spent = 0
    player_str = 8
    player_dex = 8
    player_con = 8
    player_int = 8
    player_wis = 8
    player_cha = 8
    str_ps = 0
    dex_ps = 0
    con_ps = 0
    int_ps = 0
    wis_ps = 0
    cha_ps = 0
    player_race = ''
    player_gender = ''
    player_class = ''
    player_background = ''
    player_alignment = ''
    player_experience = 0
    player_level = 1
    player_prof = math.floor((player_level + 7)/4)
    player_skill_prof = []
    player_save_prof = []
    player_weapon_prof = []
    player_tool_prof = []
    player_armor_prof = []
    player_abilities = []
    player_features = []

    # Create Dictionaries
    languages = (['Common', 'Dwarvish', 'Elvish', 'Giant', 'Gnomish', 'Goblin', 'Halfling',
                  'Orc', 'Abyssal', 'Celestial', 'Draconic', 'Infernal'])
    gaming_sets = ['Dice Set', 'Playing Card Set']
    artisans_tools = (['Alchemists Supplies', 'Brewers Supplies', 'Calligraphers Supplies',
                       'Carpenters Tools', 'Cartographers Tools', 'Cobblers Tools',
                       'Cooks Utensils', 'Glassblowers Tools', 'Jewelers Tools',
                       'Leatherworkers Tools', 'Masons Tools', 'Painters Tools',
                       'Potters Tools', 'Smiths Tools', 'Tinkers Tools',
                       'Weavers Tools', 'Woodcarvers Tools'])
    # Character Name
    print("What is your name?")
    player_name = input()
    while True:
        try:
            print('How many points for attributes? (27 is standard)')
            max_points = int(input())
            if -1 > max_points:
                raise ValueError()
            break
        except ValueError:
            print('Invalid Entry')
    # Point Buy Runs in a loop until max_points are spent| Maybe reset points spent if invalid?
    while points_spent != max_points:

        while True:
            try:
                print('Strength: ', player_str)
                choice = int(input('Choose a Strength Score: 8, 9, 10, 11, 12, 13, 14, 15: '))
                if not 8 <= choice <= 15:
                    raise ValueError()
                player_str = choice
                if 7 <= player_str <= 14:
                    str_ps = player_str - 8
                if player_str == 14:
                    str_ps = player_str - 7
                if player_str == 15:
                    str_ps = player_str - 6
                points_spent = str_ps + dex_ps + con_ps + int_ps + wis_ps + cha_ps
                print('Points Spent: ', points_spent, '/', max_points)
                print()
                break
            except ValueError:
                print('Invalid Entry')
        while True:
            try:
                print('Dexterity: ', player_dex)
                choice = int(input('Choose a Dexterity Score: 8, 9, 10, 11, 12, 13, 14, 15: '))
                if not 8 <= choice <= 15:
                    raise ValueError()
                player_dex = choice
                if 7 <= player_dex <= 14:
                    dex_ps = player_dex - 8
                if player_dex == 14:
                    dex_ps = player_dex - 7
                if player_dex == 15:
                    dex_ps = player_dex - 6
                points_spent = str_ps + dex_ps + con_ps + int_ps + wis_ps + cha_ps
                print('Points Spent: ', points_spent, '/', max_points)
                print()
                break
            except ValueError:
                print('Invalid Entry')
        while True:
            try:
                print('Constitution: ', player_con)
                choice = int(input('Choose a Constitution Score: 8, 9, 10, 11, 12, 13, 14, 15: '))
                if not 8 <= choice <= 15:
                    raise ValueError()
                player_con = choice
                if 7 <= player_con <= 14:
                    con_ps = player_con - 8
                if player_con == 14:
                    con_ps = player_con - 7
                if player_con == 15:
                    con_ps = player_con - 6
                points_spent = str_ps + dex_ps + con_ps + int_ps + wis_ps + cha_ps
                print('Points Spent: ', points_spent, '/', max_points)
                print()
                break
            except ValueError:
                print('Invalid Entry')
        while True:
            try:
                print('Intelligence: ', player_int)
                choice = int(input('Choose a Intelligence Score: 8, 9, 10, 11, 12, 13, 14, 15: '))
                if not 8 <= choice <= 15:
                    raise ValueError()
                player_int = choice
                if 7 <= player_int <= 14:
                    int_ps = player_int - 8
                if player_int == 14:
                    int_ps = player_int - 7
                if player_int == 15:
                    int_ps = player_int - 6
                points_spent = str_ps + dex_ps + con_ps + int_ps + wis_ps + cha_ps
                print('Points Spent: ', points_spent, '/', max_points)
                print()
                break
            except ValueError:
                print('Invalid Entry')
        while True:
            try:
                print('Wisdom: ', player_wis)
                choice = int(input('Choose a Wisdom Score: 8, 9, 10, 11, 12, 13, 14, 15: '))
                if not 8 <= choice <= 15:
                    raise ValueError()
                player_wis = choice
                if 7 <= player_wis <= 14:
                    wis_ps = player_wis - 8
                if player_wis == 14:
                    wis_ps = player_wis - 7
                if player_wis == 15:
                    wis_ps = player_wis - 6
                points_spent = str_ps + dex_ps + con_ps + int_ps + wis_ps + cha_ps
                print('Points Spent: ', points_spent, '/', max_points)
                print()
                break
            except ValueError:
                print('Invalid Entry')
        while True:
            try:
                print('Charisma: ', player_cha)
                choice = int(input('Choose a Charisma Score: 8, 9, 10, 11, 12, 13, 14, 15: '))
                if not 8 <= choice <= 15:
                    raise ValueError()
                player_cha = choice
                if 7 <= player_cha <= 14:
                    cha_ps = player_cha - 8
                if player_cha == 14:
                    cha_ps = player_cha - 7
                if player_cha == 15:
                    cha_ps = player_cha - 6
                points_spent = str_ps + dex_ps + con_ps + int_ps + wis_ps + cha_ps
                print('Points Spent: ', points_spent, '/', max_points)
                print()
                break
            except ValueError:
                print('Invalid Entry')
        else:
            print('Your Base Attributes are: STR:', player_str, ' DEX:', player_dex,
                  ' CON:', player_con, ' INT:', player_int, ' WIS', player_wis, ' CHA:', player_cha)
    # Race Selection
    player_races = ['Dwarf', 'Elf', 'Halfling', 'Human']
    while player_race not in player_races:
        print('First, choose a RACE: ', player_races)
        player_race = input()
    if player_race == "Dwarf":
        dwarf_subraces = ['Hill', 'Mountain']
        player_subrace = ''
        player_con = player_con + 2
        player_size = 'Medium'
        player_speed = '25'
        player_languages = ['Common', 'Dwarvish']
        languages.remove('Common')
        languages.remove('Dwarvish')
        player_abilities = ['Darkvision', 'Dwarven Resilience',
                            'Dwarven Combat Training', 'Tool Proficiency', 'Stonecunning']
        while player_subrace not in dwarf_subraces:
            print('Choose a SUBRACE: ', dwarf_subraces)
            player_subrace = input()
        if player_subrace == 'Hill':
            player_wis = player_wis + 1
            player_abilities.extend('Dwarven Toughness')
        if player_subrace == 'Mountain':
            player_str = player_str + 2
            player_abilities.extend('Dwarven Armor Training')
    elif player_race == 'Elf':
        elf_subraces = ['High', 'Wood']
        player_subrace = ''
        player_dex = player_dex + 2
        player_size = 'Medium'
        player_speed = '30'
        player_languages = ['Common', 'Elvish']
        languages.remove('Common')
        languages.remove('Elvish')
        player_abilities = ['Darkvision', 'Keen Senses', 'Fey Ancestry', 'Trance']
        while player_subrace not in elf_subraces:
            print('Choose a SUBRACE: ', elf_subraces)
            player_subrace = input()
        if player_subrace == 'High':
            player_int = player_int + 1
            player_abilities.extend(('Elf Weapon Training', 'Cantrip', 'Extra Language'))
            while True:
                try:
                    choice = (input('Select a Language' + str(languages)))
                    if choice not in languages:
                        raise ValueError()
                    player_languages.extend([choice])
                    languages.remove(choice)
                    break
                except ValueError:
                    print('Invalid Selection')
        if player_subrace == 'Wood':
            player_wis = player_wis + 1
            player_abilities.extend(('Elf Weapon Training', 'Fleet of Foot', 'Mask of the Wild'))
    elif player_race == 'Halfling':
        halfling_subraces = ['Lightfoot', 'Stout']
        player_subrace = ''
        player_dex = player_dex + 2
        player_size = 'Small'
        player_speed = '25'
        player_languages = ['Common', 'Halfling']
        languages.remove('Common')
        languages.remove('Halfling')
        player_abilities = ['Lucky', 'Brave', 'Halfling Nimbleness']
        while player_subrace not in halfling_subraces:
            print('Choose a SUBRACE: ', halfling_subraces)
            player_subrace = input()
        if player_subrace == 'Lightfoot':
            player_cha = player_cha + 1
            player_abilities.extend('Naturally Stealthy')
        if player_subrace == 'Stout':
            player_con = player_con + 1
            player_abilities.extend('Stout Resilience')
    elif player_race == "Human":
        player_subrace = ''
        player_str = player_str + 1
        player_dex = player_dex + 1
        player_con = player_con + 1
        player_int = player_int + 1
        player_wis = player_wis + 1
        player_cha = player_cha + 1
        player_size = 'Medium'
        player_speed = '30'
        player_languages = ['Common']
        languages.remove('Common')
        while True:
            try:
                choice = (input('Select a Language' + str(languages)))
                if choice not in languages:
                    raise ValueError()
                player_languages.extend([choice])
                languages.remove(choice)
                break
            except ValueError:
                print('Invalid Selection')
    #<Gender Selection>
    player_genders = ['Female', 'Male', 'Other']
    while player_gender not in player_genders:
        print('Secondly, choose your GENDER: ', player_genders)
        player_gender = input()
    #<Class Selection>
    player_classes = ['Cleric', 'Fighter', 'Rogue', 'Wizard']
    while player_class not in player_classes:
        print('Next, choose your CLASS: ', player_classes)
        player_class = input()
    if player_class == 'Cleric':
        cleric_skills = ['History', 'Insight', 'Medicine', 'Persuasion', 'Religion']
        while True:
            try:
                choice = (input('Select a Skill Proficiency:' + str(cleric_skills)))
                if choice not in cleric_skills:
                    raise ValueError()
                player_skill_prof.extend([choice])
                cleric_skills.remove(choice)
                break
            except ValueError:
                print('Invalid Selection')
        while True:
            try:
                choice = (input('Select a second Skill Proficiency:' + str(cleric_skills)))
                if choice not in cleric_skills:
                    raise ValueError()
                player_skill_prof.extend([choice])
                break
            except ValueError:
                print('Invalid Selection')
        player_save_prof.extend(['Wisdom', 'Charisma'])
        player_armor_prof.extend(['Light Armor', 'Medium Armor', 'Shields'])
        player_weapon_prof.extend(['Simple Weapons'])
        player_primary_ability = 'Wisdom'
        player_hit_die = 'd8'
        player_features.extend(['Spellcasting', 'Divine Domain'])
        #Equipment
    if player_class == 'Fighter':
        fighter_skills = ['Acrobatics', 'Animal Handling', 'Athletics', 'History',
                          'Insight', 'Intimidation', 'Perception', 'Survival']
        while True:
            try:
                choice = (input('Select a Skill Proficiency:' + str(fighter_skills)))
                if choice not in fighter_skills:
                    raise ValueError()
                player_skill_prof.extend([choice])
                fighter_skills.remove(choice)
                break
            except ValueError:
                print('Invalid Selection')
        while True:
            try:
                choice = (input('Select a second Skill Proficiency:' + str(fighter_skills)))
                if choice not in fighter_skills:
                    raise ValueError()
                player_skill_prof.extend([choice])
                break
            except ValueError:
                print('Invalid Selection')
        player_save_prof.extend(['Strength', 'Constitution'])
        player_armor_prof.extend(['Light Armor', 'Medium Armor', 'Heavy Armor', 'Shields'])
        player_weapon_prof.extend(['Simple Weapons', 'Martial Weapons'])
        fighter_primary_abilities = ['Strength', 'Dexterity']
        while True:
            try:
                choice = (input('Select a Primary Ability: ' + str(fighter_primary_abilities)))
                if choice not in fighter_primary_abilities:
                    raise ValueError()
                player_primary_ability = choice
                break
            except ValueError:
                print('Invalid Selection')
        player_hit_die = 'd10'
        player_features.extend(['Fighting Style', 'Second Wind'])
	#Equipment
    if player_class == 'Rogue':
        rogue_skills = ['Acrobatics', 'Athletics', 'Deception', 'Insight', 'Intimidation',
                        'Investigation', 'Perception', 'Performance', 'Persuasion',
                        'Sleight of Hand', 'Stealth']
        while True:
            try:
                choice = (input('Select a Skill Proficiency:' + str(rogue_skills)))
                if choice not in rogue_skills:
                    raise ValueError()
                player_skill_prof.extend([choice])
                rogue_skills.remove(choice)
                break
            except ValueError:
                print('Invalid Selection')
        while True:
            try:
                choice = (input('Select a second Skill Proficiency:' + str(rogue_skills)))
                if choice not in rogue_skills:
                    raise ValueError()
                player_skill_prof.extend([choice])
                rogue_skills.remove(choice)
                break
            except ValueError:
                print('Invalid Selection')
        while True:
            try:
                choice = (input('Select a third Skill Proficiency:' + str(rogue_skills)))
                if choice not in rogue_skills:
                    raise ValueError()
                player_skill_prof.extend([choice])
                rogue_skills.remove(choice)
                break
            except ValueError:
                print('Invalid Selection')
        while True:
            try:
                choice = (input('Select a fourth Skill Proficiency:' + str(rogue_skills)))
                if choice not in rogue_skills:
                    raise ValueError()
                player_skill_prof.extend([choice])
                rogue_skills.remove(choice)
                break
            except ValueError:
                print('Invalid Selection')
        player_save_prof.extend(['Dexterity', 'Intelligence'])
        player_armor_prof.extend(['Light Armor'])
        player_weapon_prof.extend(['Simple Weapons', 'Hand Crossbows', 'Longswords',
                                   'Rapiers', 'Shortswords'])
        player_primary_ability = 'Dexterity'
        player_hit_die = 'd8'
        player_features.extend(['Expertise', 'Sneak attack', 'Thieves Cant'])
        player_tool_prof.extend(['Thieves tools'])
	#Equipment
    if player_class == 'Wizard':
        wizard_skills = ['Arcana', 'History', 'Insight', 'Investigation', 'Medicine', 'Religion']
        while True:
            try:
                choice = (input('Select a Skill Proficiency:' + str(wizard_skills)))
                if choice not in wizard_skills:
                    raise ValueError()
                player_skill_prof.extend([choice])
                wizard_skills.remove(choice)
                break
            except ValueError:
                print('Invalid Selection')
        while True:
            try:
                choice = (input('Select a second Skill Proficiency:' + str(wizard_skills)))
                if choice not in wizard_skills:
                    raise ValueError()
                player_skill_prof.extend([choice])
                break
            except ValueError:
                print('Invalid Selection')
        player_save_prof.extend(['Intelligence', 'Wisdom'])
        player_armor_prof.extend([''])
        player_weapon_prof.extend(['Daggers', 'Darts', 'Slings',
                                   'Quarterstaffs', 'Light Crossbows'])
        player_primary_ability = 'Intelligence'
        player_hit_die = 'd6'
        player_features.extend(['Spellcasting', 'Arcane Recovery'])
	#Equipment
    player_backgrounds = ['Acolyte', 'Criminal', 'Folk Hero', 'Noble', 'Sage', 'Soldier']
    while player_background not in player_backgrounds:
        print('Now, choose your BACKGROUND: ', player_backgrounds)
        player_background = input()
    if player_background == 'Acolyte':
        player_skill_prof.extend(['insight', 'religion'])
        while True:
            try:
                choice = (input('Select a Language' + str(languages)))
                if choice not in languages:
                    raise ValueError()
                player_languages.extend([choice])
                languages.remove(choice)
                break
            except ValueError:
                print('Invalid Selection')
        while True:
            try:
                choice = (input('Select another Language' + str(languages)))
                if choice not in languages:
                    raise ValueError()
                player_languages.extend([choice])
                languages.remove(choice)
                break
            except ValueError:
                print('Invalid Selection')
        player_abilities.extend(['Shelter Of The Faithful'])
	#equipment
    if player_background == 'Criminal':
        player_skill_prof.extend(['Deception', 'Stealth'])
        while True:
            try:
                choice = (input('Select a Gaming Set Proficiency: ' + str(gaming_sets)))
                if choice not in gaming_sets:
                    raise ValueError()
                player_tool_prof.extend([choice])
                break
            except ValueError:
                print('Invalid Selection')
        player_tool_prof.extend(['Thieves Tools'])
        player_abilities.extend(['Criminal Contact'])
        #equipment
    if player_background == 'Folk Hero':
        player_skill_prof.extend(['Animal Handling', 'Survival'])
        while True:
            try:
                choice = (input('Select a Artisans Tools Proficiency: ' + str(artisans_tools)))
                if choice not in artisans_tools:
                    raise ValueError()
                player_tool_prof.extend([choice])
                break
            except ValueError:
                print('Invalid Selection')
        player_tool_prof.extend(['Land Vehicles'])
        player_abilities.extend(['Rustic Hospitality'])
        #equipment
    if player_background == 'Noble':
        player_skill_prof.extend(['History', 'Persuasion'])
        while True:
            try:
                choice = (input('Select a Gaming Set Proficiency: ' + str(gaming_sets)))
                if choice not in gaming_sets:
                    raise ValueError()
                player_tool_prof.extend([choice])
                break
            except ValueError:
                print('Invalid Selection')
        while True:
            try:
                choice = (input('Select a Language' + str(languages)))
                if choice not in languages:
                    raise ValueError()
                player_languages.extend([choice])
                languages.remove(choice)
                break
            except ValueError:
                print('Invalid Selection')
        player_abilities.extend(['Position of Privilege'])
        #equipment
    if player_background == 'Sage':
        player_skill_prof.extend(['Arcana', 'History'])
        while True:
            try:
                choice = (input('Select a Language' + str(languages)))
                if choice not in languages:
                    raise ValueError()
                player_languages.extend([choice])
                languages.remove(choice)
                break
            except ValueError:
                print('Invalid Selection')
        while True:
            try:
                choice = (input('Select another Language' + str(languages)))
                if choice not in languages:
                    raise ValueError()
                player_languages.extend([choice])
                languages.remove(choice)
                break
            except ValueError:
                print('Invalid Selection')
        player_abilities.extend(['Researcher'])
        #equipment
    if player_background == 'Soldier':
        player_skill_prof.extend(['Athletics', 'Intimidation'])
        while True:
            try:
                choice = (input('Select a Gaming Set Proficiency: ' + str(gaming_sets)))
                if choice not in gaming_sets:
                    raise ValueError()
                player_tool_prof.extend([choice])
                break
            except ValueError:
                print('Invalid Selection')
        player_tool_prof.extend(['Land Vehicles'])
        player_abilities.extend(['Military Rank'])
        #equipment
    player_alignments = ['Lawful Good', 'Neutral Good', 'Chaotic Good', 'Lawful Neutral',
                         'True Neutral', 'Chaotic Neutral', 'Lawful Evil', 'Neutral Evil',
                         'Chaotic Evil']
    while player_alignment not in player_alignments:
        print('Choose your ALIGNMENT: ', player_alignments)
        player_alignment = input()
    player_str_mod = player_str//2-5
    player_dex_mod = player_dex//2-5
    player_con_mod = player_con//2-5
    player_int_mod = player_int//2-5
    player_wis_mod = player_wis//2-5
    player_cha_mod = player_cha//2-5
    #Create the Character file
    character = shelve.open(player_name, 'c')
    character.update({'player_name':player_name})
    #Convert lists to sets and back to remove duplicates
    player_skill_prof = set(player_skill_prof)
    player_skill_prof = list(player_skill_prof)
    #Calculate Skill Mods
    if 'Acrobatics' in player_skill_prof:
        player_acro = player_prof + player_dex_mod
    else:
        player_acro = player_dex_mod
    if 'Animal Handling' in player_skill_prof:
        player_anim = player_prof + player_wis_mod
    else:
        player_anim = player_wis_mod
    if 'Arcana' in player_skill_prof:
        player_arca = player_prof + player_int_mod
    else:
        player_arca = player_int_mod
    if 'Athletics' in player_skill_prof:
        player_athl = player_prof + player_str_mod
    else:
        player_athl = player_str_mod
    if 'Deception' in player_skill_prof:
        player_dece = player_prof + player_cha_mod
    else:
        player_dece = player_cha_mod
    if 'History' in player_skill_prof:
        player_hist = player_prof + player_int_mod
    else:
        player_hist = player_int_mod
    if 'Insight' in player_skill_prof:
        player_insi = player_prof + player_wis_mod
    else:
        player_insi = player_wis_mod
    if 'Intimidation' in player_skill_prof:
        player_inti = player_prof + player_cha_mod
    else:
        player_inti = player_cha_mod
    if 'Investigation' in player_skill_prof:
        player_inve = player_prof + player_int_mod
    else:
        player_inve = player_int_mod
    if 'Medicine' in player_skill_prof:
        player_medi = player_prof + player_int_mod
    else:
        player_medi = player_int_mod
    if 'Nature' in player_skill_prof:
        player_natu = player_prof + player_int_mod
    else:
        player_natu = player_int_mod
    if 'Perception' in player_skill_prof:
        player_perc = player_prof + player_wis_mod
    else:
        player_perc = player_wis_mod
    if 'Performance' in player_skill_prof:
        player_perf = player_prof + player_cha_mod
    else:
        player_perf = player_cha_mod
    if 'Persuasion' in player_skill_prof:
        player_pers = player_prof + player_cha_mod
    else:
        player_pers = player_cha_mod
    if 'Religion' in player_skill_prof:
        player_reli = player_prof + player_int_mod
    else:
        player_reli = player_int_mod
    if 'Sleight of Hand' in player_skill_prof:
        player_slei = player_prof + player_dex_mod
    else:
        player_slei = player_dex_mod
    if 'Stealth' in player_skill_prof:
        player_stea = player_prof + player_dex_mod
    else:
        player_stea = player_dex_mod
    if 'Survival' in player_skill_prof:
        player_surv = player_prof + player_wis_mod
    else:
        player_surv = player_wis_mod
    #Calculate Saves
    if 'Strength' in player_save_prof:
        player_str_save = player_prof + player_str_mod
    else:
        player_str_save = player_str_mod
    if 'Dexterity' in player_save_prof:
        player_dex_save = player_prof + player_dex_mod
    else:
        player_dex_save = player_dex_mod
    if 'Constitution' in player_save_prof:
        player_con_save = player_prof + player_con_mod
    else:
        player_con_save = player_con_mod
    if 'Intelligence' in player_save_prof:
        player_int_save = player_prof + player_int_mod
    else:
        player_int_save = player_int_mod
    if 'Wisdom' in player_save_prof:
        player_wis_save = player_prof + player_wis_mod
    else:
        player_wis_save = player_wis_mod
    if 'Charisma' in player_save_prof:
        player_cha_save = player_prof + player_cha_mod
    else:
        player_cha_save = player_cha_mod
    #Write Variables to Character Dictionary
    character.update({'player_gender':player_gender, 'player_race':player_race,
                      'player_subrace':player_subrace, 'player_class':player_class,
                      'player_background':player_background, 'player_alignment':player_alignment,
                      'player_experience':player_experience, 'player_level':player_level,
                      'player_prof':player_prof, 'player_skill_prof':player_skill_prof,
                      'player_save_prof':player_save_prof, 'player_weapon_prof':player_weapon_prof,
                      'player_tool_prof':player_tool_prof, 'player_armor_prof':player_armor_prof,
                      'player_abilities':player_abilities, 'player_features':player_features,
                      'player_str':player_str, 'player_dex':player_dex, 'player_con':player_con,
                      'player_wis':player_wis, 'player_int':player_int, 'player_cha':player_cha,
                      'player_str_mod':player_str_mod, 'player_dex_mod':player_dex_mod,
                      'player_con_mod':player_con_mod, 'player_wis_mod':player_wis_mod,
                      'player_int_mod':player_int_mod, 'player_cha_mod':player_cha_mod,
                      'player_str_save':player_str_save, 'player_dex_save':player_dex_save,
                      'player_con_save':player_con_save, 'player_int_save':player_int_save,
                      'player_wis_save':player_wis_save, 'player_cha_save':player_cha_save,
                      'player_acro':player_acro, 'player_anim':player_anim,
                      'player_arca':player_arca, 'player_athl':player_athl,
                      'player_dece':player_dece, 'player_hist':player_hist,
                      'player_insi':player_insi, 'player_inti':player_inti,
                      'player_inve':player_inve, 'player_medi':player_medi,
                      'player_natu':player_natu, 'player_perc':player_perc,
                      'player_perf':player_perf, 'player_pers':player_pers,
                      'player_reli':player_reli, 'player_slei':player_slei,
                      'player_stea':player_stea, 'player_surv':player_surv,
                      'player_size':player_size, 'player_speed':player_speed,
                      'player_primary_ability':player_primary_ability,
                      'player_hit_die':player_hit_die})
    print('Character' +' ' + player_name +' has been created.')
    #Close the character file
    character.close()

#Uncomment to allow to run the character_creation function directly.
character_creation()
