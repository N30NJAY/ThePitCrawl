import shelve

def character_creation():
        #<Initialize Character Options>
        PointsSpent = 0
        MaxPoints = 27
        StrPs = 0
        DexPs = 0
        ConPs = 0
        IntPs = 0
        WisPs = 0
        ChaPs = 0
        PlayerRace = ""
        PlayerGender = ""
        PlayerClass = ""
        PlayerBackground = ""
        PlayerAlignment = ""
        Languages = ['Common','Dwarvish','Elvish','Giant','Gnomish','Goblin','Halfling','Orc','Abyssal','Celestial','Draconic','Infernal']
        
        #<Character Name>
        print("What is your name?")
        PlayerName = input()
        
        #<Point Buy>
        while PointsSpent != MaxPoints:
                while True:
                        try:
                                choice = int(input('Choose a Strength Score: 8, 9, 10, 11, 12, 13, 14, 15: '))
                                if not (8 <= choice <= 15):
                                        raise ValueError()
                                PlayerStr = choice
                                if 7 <= PlayerStr <= 14:
                                        StrPs = PlayerStr - 8
                                if PlayerStr == 14:
                                        StrPs = PlayerStr - 7
                                if PlayerStr == 15:
                                        StrPs = PlayerStr - 6
                                PointsSpent = StrPs + DexPs + ConPs + IntPs + WisPs + ChaPs
                                print ('Points Spent: ',PointsSpent,'/',MaxPoints)
                                break
                        except ValueError:
                                print('Invalid Entry')
                while True:
                        try:
                                choice = int(input('Choose a Dexterity Score: 8, 9, 10, 11, 12, 13, 14, 15: '))
                                if not (8 <= choice <= 15):
                                        raise ValueError()
                                PlayerDex = choice
                                if 7 <= PlayerDex <= 14:
                                        DexPs = PlayerDex - 8
                                if PlayerDex == 14:
                                        DexPs = PlayerDex - 7
                                if PlayerDex == 15:
                                        DexPs = PlayerDex - 6
                                PointsSpent = StrPs + DexPs + ConPs + IntPs + WisPs + ChaPs
                                print ('Points Spent: ',PointsSpent,'/',MaxPoints)
                                break
                        except ValueError:
                                print('Invalid Entry')
                while True:
                        try:
                                choice = int(input('Choose a Constitution Score: 8, 9, 10, 11, 12, 13, 14, 15: '))
                                if not (8 <= choice <= 15):
                                        raise ValueError()
                                PlayerCon = choice
                                if 7 <= PlayerCon <= 14:
                                        ConPs = PlayerCon - 8
                                if PlayerCon == 14:
                                        ConPs = PlayerCon - 7
                                if PlayerCon == 15:
                                        ConPs = PlayerCon - 6
                                PointsSpent = StrPs + DexPs + ConPs + IntPs + WisPs + ChaPs
                                print ('Points Spent: ',PointsSpent,'/',MaxPoints)
                                break
                        except ValueError:
                                print('Invalid Entry')
                while True:
                        try:
                                choice = int(input('Choose a Intelligence Score: 8, 9, 10, 11, 12, 13, 14, 15: '))
                                if not (8 <= choice <= 15):
                                        raise ValueError()
                                PlayerInt = choice
                                if 7 <= PlayerInt <= 14:
                                        IntPs = PlayerInt - 8
                                if PlayerInt == 14:
                                        IntPs = PlayerInt - 7
                                if PlayerInt == 15:
                                        IntPs = PlayerInt - 6
                                PointsSpent = StrPs + DexPs + ConPs + IntPs + WisPs + ChaPs
                                print ('Points Spent: ',PointsSpent,'/',MaxPoints)
                                break
                        except ValueError:
                                print('Invalid Entry')
                while True:
                        try:
                                choice = int(input('Choose a Wisdom Score: 8, 9, 10, 11, 12, 13, 14, 15: '))
                                if not (8 <= choice <= 15):
                                        raise ValueError()
                                PlayerWis = choice
                                if 7 <= PlayerWis <= 14:
                                        WisPs = PlayerWis - 8
                                if PlayerWis == 14:
                                        WisPs = PlayerWis - 7
                                if PlayerWis == 15:
                                        WisPs = PlayerWis - 6
                                PointsSpent = StrPs + DexPs + ConPs + IntPs + WisPs + ChaPs
                                print ('Points Spent: ',PointsSpent,'/',MaxPoints)
                                break
                        except ValueError:
                                print('Invalid Entry')
                while True:
                        try:
                                choice = int(input('Choose a Charisma Score: 8, 9, 10, 11, 12, 13, 14, 15: '))
                                if not (8 <= choice <= 15):
                                        raise ValueError()
                                PlayerCha = choice
                                if 7 <= PlayerCha <= 14:
                                        ChaPs = PlayerCha - 8
                                if PlayerCha == 14:
                                        ChaPs = PlayerCha - 7
                                if PlayerCha == 15:
                                        ChaPs = PlayerCha - 6
                                PointsSpent = StrPs + DexPs + ConPs + IntPs + WisPs + ChaPs
                                print ('Points Spent: ',PointsSpent,'/',MaxPoints)
                                break
                        except ValueError:
                                print('Invalid Entry')
        else:
                print('Your Base Attributes are: STR:',PlayerStr,' DEX:',PlayerDex,' CON:',PlayerCon,' INT:',PlayerInt,' WIS',PlayerWis,' CHA:',PlayerCha)

        #<Enable Race Selection>
        PlayerRaces = ['Dwarf','Elf','Halfling','Human']
        while PlayerRace not in PlayerRaces:
        	print("First, choose a RACE: Dwarf, Elf, Halfling, Human")
        	PlayerRace = input()
        	
        if PlayerRace == "Dwarf":
                DwarfSubraces = ['Hill','Mountain']
                PlayerSubrace = ''
                PlayerCon = PlayerCon + 2
                PlayerSize = 'Medium'
                PlayerSpeed = '25'
                PlayerLang = ['Common','Dwarven']
                PlayerAbilities = ['Darkvision','Dwarven Resilience','Dwarven Combat Training','Tool Proficiency','Stonecunning']
                while PlayerSubrace not in DwarfSubraces:
                       print('Choose a SUBRACE: Hill, Mountain')
                       PlayerSubrace = input()
                if PlayerSubrace == 'Hill':
                        PlayerWis = PlayerWis + 1
                        PlayerAbilities.append ['Dwarven Toughness']
                if PlayerSubrace == 'Mountain':
                        PlayerStr = PlayerStr + 2
                        PlayerAbilities.append ['Dwarven Armor Training']

        elif PlayerRace == 'Elf':
                ElfSubraces = ['High','Wood']
                PlayerSubrace = ''
                PlayerDex = PlayerDex + 2
                PlayerSize = 'Medium'
                PlayerSpeed = '30'
                PlayerLang = ['Common','Elvish']
                PlayerAbilities = ['Darkvision','Keen Senses','Fey Ancestry','Trance']
                while PlayerSubrace not in ElfSubraces:
                        print('Choose a SUBRACE: High, Wood')
                        PlayerSubrace = input()
                if PlayerSubrace == 'High':
                        PlayerInt = PlayerInt + 1
                        PlayerAbilities.extend(('Elf Weapon Training','Cantrip','Extra Language'))
                if PlayerSubrace == 'Wood':
                        PlayerWis = PlayerWis + 1
                        PlayerAbilities.append = ['Elf Weapon Training','Fleet of Foot','Mask of the Wild']

        elif PlayerRace == 'Halfling':
                HalflingSubraces = ['Lightfoot','Stout']
                PlayerSubrace = ''
                PlayerDex = PlayerDex + 2
                PlayerSize = 'Small'
                PlayerSpeed = '25'
                PlayerLang = ['Common','Halfling']
                PlayerAbilities = ['Lucky','Brave','Halfling Nimbleness']
                while PlayerSubrace not in HalflingSubraces:
                        print('Choose a SUBRACE: Lightfoot, Stout')
                        PlayerSubrace = input()
                if PlayerSubrace == 'Lightfoot':
                        PlayerCha = PlayerCha + 1
                        PlayerAbilities.append ['Naturally Stealthy']
                if PlayerSubrace == 'Stout':
                        PlayerCon = PlayerCon + 1
                        PlayerAbilities.append ['Stout Resilience']
                             
        elif PlayerRace == "Human":
                PlayerSubrace = ''
                PlayerStr = PlayerStr + 1
                PlayerDex = PlayerDex + 1
                PlayerCon = PlayerCon + 1
                PlayerInt = PlayerInt + 1
                PlayerWis = PlayerWis + 1
                PlayerCha = PlayerCha + 1
                PlayerSize = 'Medium'
                PlayerSpeed = '30'
                PlayerLang = ['Common']
                while True:
                        try:
                                choice = (input('Select a language: Common, Dwarvish, Elvish, Giant, Gnomish, Goblin, Halfling, Orc, Abyssal, Celestial, Draconic, Infernal'))
                                if choice not in Languages:
                                        raise ValueError()
                                PlayerLang.Append [choice]
                                break
                        except ValueError:
                                'Print Invalid Selection'
                                             
        #<Enable Gender Selection>
        PlayerGenders = ['Female','Male','Other']
        while PlayerGender not in PlayerGenders:
        	print("Secondly, choose your GENDER: Female, Male, Other")
        	PlayerGender = input()
        
        #<Enable Class Selection>
        PlayerClasses = ['Cleric','Fighter','Rogue','Wizard']
        while PlayerClass not in PlayerClasses:
                print("Next, choose your CLASS: Cleric, Fighter, Rogue, Wizard")
                PlayerClass = input()
        
        #<Enable Background Selection>
        PlayerBackgrounds = ['Acolyte','Criminal','Folk Hero','Sage','Soldier']
        while PlayerBackground not in PlayerBackgrounds:
                print("Now, choose your BACKGROUND: Acolyte, Criminal, Folk Hero, Sage, Soldier")
                PlayerBackground = input()
        
        #<Enable Alignment Selection>
        PlayerAlignments = ['Lawful Good','Neutral Good','Chaotic Good','Lawful Neutral','True Neutral','Chaotic Neutral','Lawful Evil','Neutral Evil','Chaotic Evil']
        while PlayerAlignment not in PlayerAlignments:
                print("Choose your ALIGNMENT: Lawful Good, Neutral Good, Chaotic Good, Lawful Neutral, True Neutral, Chaotic Neutral, Lawful Evil, Neutral Evil, Chaotic Evil")
                PlayerAlignment = input()
              
        d = shelve.open(PlayerName, 'c')
        try:
                d['player'] = { 'PlayerRace':  PlayerRace, 'PlayerGender': PlayerGender }
        finally:
                d.close()

character_creation()
