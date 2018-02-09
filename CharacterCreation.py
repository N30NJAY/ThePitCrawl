import shelve
import math

def character_creation():
        #<Initialize Character Options>
        PointsSpent = 0
        PlayerStr = 8
        PlayerDex = 8
        PlayerCon = 8
        PlayerInt = 8
        PlayerWis = 8
        PlayerCha = 8
        StrPs = 0
        DexPs = 0
        ConPs = 0
        IntPs = 0
        WisPs = 0
        ChaPs = 0
        PlayerRace = ''
        PlayerGender = ''
        PlayerClass = ''
        PlayerBackground = ''
        PlayerAlignment = ''
        PlayerExperience = 0
        PlayerLevel = 1
        PlayerProf = math.floor((PlayerLevel + 7)/4)
        PlayerSkillProf = []
        PlayerSaveProf = []
        PlayerWeaponProf = []
        PlayerToolProf = []
        PlayerArmorProf = []
        PlayerAbilities = []
        PlayerFeatures = []

        #Create Dictionaries
        Languages = ['Common','Dwarvish','Elvish','Giant','Gnomish','Goblin','Halfling','Orc','Abyssal','Celestial','Draconic','Infernal']
        GamingSets = ['Dice Set','Playing Card Set']
        ArtisansTools = ['Alchemists Supplies','Brewers Supplies','Calligraphers Supplies','Carpenters Tools','Cartographers Tools','Cobblers Tools','Cooks Utensils','Glassblowers Tools','Jewelers Tools','Leatherworkers Tools','Masons Tools','Painters Tools','Potters Tools','Smiths Tools','Tinkers Tools','Weavers Tools','Woodcarvers Tools']

        
        #<Character Name>
        print("What is your name?")
        PlayerName = input()
        while True:
                try:
                        print('How many points for attributes? (27 is standard)')
                        MaxPoints = int(input())
                        if not (-1 < MaxPoints):
                                raise ValueError()
                        break
                except ValueError:
                        print('Invalid Entry')
        #<Point Buy> Runs in a loop until MaxPoints are spent| Maybe reset points spent if invalid?
        while PointsSpent != MaxPoints:
                while True:
                        try:
                                print('Strength: ',PlayerStr)
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
                                print ('Points Spent: ',PointsSpent,'/',MaxPoints,)
                                print()
                                break
                        except ValueError:
                                print('Invalid Entry')
                while True:
                        try:
                                print('Dexterity: ',PlayerDex)
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
                                print()                                
                                break
                        except ValueError:
                                print('Invalid Entry')
                while True:
                        try:
                                print('Constitution: ',PlayerCon)
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
                                print()                                
                                break
                        except ValueError:
                                print('Invalid Entry')
                while True:
                        try:
                                print('Intelligence: ',PlayerInt)
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
                                print()                                
                                break
                        except ValueError:
                                print('Invalid Entry')
                while True:
                        try:
                                print('Wisdom: ',PlayerWis)
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
                                print()                                
                                break
                        except ValueError:
                                print('Invalid Entry')
                while True:
                        try:
                                print('Charisma: ',PlayerCha)
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
                                print()                                
                                break
                        except ValueError:
                                print('Invalid Entry')
        else:
                print('Your Base Attributes are: STR:',PlayerStr,' DEX:',PlayerDex,' CON:',PlayerCon,' INT:',PlayerInt,' WIS',PlayerWis,' CHA:',PlayerCha)
        #<Enable Race Selection>
        #Define Races to select from
        PlayerRaces = ['Dwarf','Elf','Halfling','Human']
        while PlayerRace not in PlayerRaces:
        	print('First, choose a RACE: ', PlayerRaces)
        	PlayerRace = input()
        	
        if PlayerRace == "Dwarf":
                DwarfSubraces = ['Hill','Mountain']
                PlayerSubrace = ''
                PlayerCon = PlayerCon + 2
                PlayerSize = 'Medium'
                PlayerSpeed = '25'
                PlayerLang = ['Common','Dwarven']
                Languages.remove('Common')
                Languages.remove('Dwarven')
                PlayerAbilities = ['Darkvision','Dwarven Resilience','Dwarven Combat Training','Tool Proficiency','Stonecunning']
                while PlayerSubrace not in DwarfSubraces:
                       print('Choose a SUBRACE: ', DwarfSubraces)
                       PlayerSubrace = input()
                if PlayerSubrace == 'Hill':
                        PlayerWis = PlayerWis + 1
                        PlayerAbilities.extend ('Dwarven Toughness')
                if PlayerSubrace == 'Mountain':
                        PlayerStr = PlayerStr + 2
                        PlayerAbilities.extend ('Dwarven Armor Training')

        elif PlayerRace == 'Elf':
                ElfSubraces = ['High','Wood']
                PlayerSubrace = ''
                PlayerDex = PlayerDex + 2
                PlayerSize = 'Medium'
                PlayerSpeed = '30'
                PlayerLang = ['Common','Elvish']
                Languages.remove('Common')
                Languages.remove('Elvish')
                PlayerAbilities = ['Darkvision','Keen Senses','Fey Ancestry','Trance']
                while PlayerSubrace not in ElfSubraces:
                        print('Choose a SUBRACE: ', ElfSubraces)
                        PlayerSubrace = input()
                if PlayerSubrace == 'High':
                        PlayerInt = PlayerInt + 1
                        PlayerAbilities.extend (('Elf Weapon Training','Cantrip','Extra Language'))
                        choice = (input('Select a Language' + str(Languages)))
                        if choice not in Languages:
                                raise ValueError()
                        PlayerLang.extend ([choice])
                        Languages.remove(choice)
                if PlayerSubrace == 'Wood':
                        PlayerWis = PlayerWis + 1
                        PlayerAbilities.extend (('Elf Weapon Training','Fleet of Foot','Mask of the Wild'))

        elif PlayerRace == 'Halfling':
                HalflingSubraces = ['Lightfoot','Stout']
                PlayerSubrace = ''
                PlayerDex = PlayerDex + 2
                PlayerSize = 'Small'
                PlayerSpeed = '25'
                PlayerLang = ['Common','Halfling']
                Languages.remove('Common')
                Languages.remove('Halfling')
                PlayerAbilities = ['Lucky','Brave','Halfling Nimbleness']
                while PlayerSubrace not in HalflingSubraces:
                        print('Choose a SUBRACE: ', HalflingSubraces)
                        PlayerSubrace = input()
                if PlayerSubrace == 'Lightfoot':
                        PlayerCha = PlayerCha + 1
                        PlayerAbilities.extend ('Naturally Stealthy')
                if PlayerSubrace == 'Stout':
                        PlayerCon = PlayerCon + 1
                        PlayerAbilities.extend ('Stout Resilience')
                             
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
                Languages.remove ('Common')
                
                while True:
                        try:
                                choice = (input('Select a Language' + str(Languages)))
                                if choice not in Languages:
                                        raise ValueError()
                                PlayerLang.extend ([choice])
                                Languages.remove(choice)
                                break
                        except ValueError:
                                'Print Invalid Selection'
                                             
        #<Enable Gender Selection>
        PlayerGenders = ['Female','Male','Other']
        while PlayerGender not in PlayerGenders:
        	print('Secondly, choose your GENDER: ', PlayerGenders)
        	PlayerGender = input()
        
        #<Enable Class Selection>
        PlayerClasses = ['Cleric','Fighter','Rogue','Wizard']
        while PlayerClass not in PlayerClasses:
                print('Next, choose your CLASS: ', PlayerClasses)
                PlayerClass = input()
        if PlayerClass == 'Cleric':
                ClericSkills = ['History','Insight','Medicine','Persuasion','Religion']
                while True:
                        try:
                                choice = (input('Select a Skill Proficiency:' + str(ClericSkills)))
                                if choice not in ClericSkills:
                                        raise ValueError()
                                PlayerSkillProf.extend ([choice])
                                ClericSkills.remove(choice)
                                break
                        except ValueError:
                                print('Invalid Selection')             
                while True:
                        try:
                                choice = (input('Select a second Skill Proficiency:' + str(ClericSkills)))
                                if choice not in ClericSkills:
                                        raise ValueError()
                                PlayerSkillProf.extend ([choice])
                                break
                        except ValueError:
                                print('Invalid Selection')                    
                PlayerSaveProf.extend (['Wisdom','Charisma'])
                PlayerArmorProf.extend (['Light Armor','Medium Armor','Shields'])
                PlayerWeaponProf.extend (['Simple Weapons'])
                PlayerPrimaryAbility = 'Wisdom'
                PlayerHitDie = 'd8'
                PlayerFeatures.extend (['Spellcasting','Divine Domain'])
		#Equipment
        if PlayerClass == 'Fighter':
                FighterSkills = ['Acrobatics','Animal Handling','Athletics','History','Insight','Intimidation','Perception','Survival']
                while True:
                        try:
                                choice = (input('Select a Skill Proficiency:' + str(FighterSkills)))
                                if choice not in FighterSkills:
                                        raise ValueError()
                                PlayerSkillProf.extend ([choice])
                                FighterSkills.remove(choice)
                                break
                        except ValueError:
                                print('Invalid Selection')
                while True:
                        try:
                                choice = (input('Select a second Skill Proficiency:' + str(FighterSkills)))
                                if choice not in FighterSkills:
                                        raise ValueError()
                                PlayerSkillProf.extend ([choice])
                                break
                        except ValueError:
                                print('Invalid Selection')
                PlayerSaveProf.extend (['Strength','Constitution'])
                PlayerArmorProf.extend (['Light Armor','Medium Armor','Heavy Armor','Shields'])
                PlayerWeaponProf.extend (['Simple Weapons','Martial Weapons'])
                FighterPrimaryAbilities = ['Strength','Dexterity']
                while True:
                        try:
                                choice = (input('Select a Primary Ability: ' + str(FighterPrimaryAbilities)))
                                if choice not in FighterPrimaryAbilities:
                                        raise ValueError()
                                PlayerPrimaryAbility = choice
                                break
                        except ValueError:
                                print('Invalid Selection')
                PlayerHitDie = 'd10'
                PlayerFeatures.extend (['Fighting Style','Second Wind'])
		#Equipment
        if PlayerClass == 'Rogue':
                RogueSkills = ['Acrobatics','Athletics','Deception','Insight','Intimidation','Investigation','Perception','Performance','Persuasion','Sleight of Hand','Stealth']
                while True:
                        try:
                                choice = (input('Select a Skill Proficiency:' + str(RogueSkills)))
                                if choice not in RogueSkills:
                                        raise ValueError()
                                PlayerSkillProf.extend ([choice])
                                RogueSkills.remove(choice)
                                break
                        except ValueError:
                                print('Invalid Selection')
                while True:
                        try:
                                choice = (input('Select a second Skill Proficiency:' + str(RogueSkills)))
                                if choice not in RogueSkills:
                                        raise ValueError()
                                PlayerSkillProf.extend ([choice])
                                RogueSkills.remove(choice)
                                break
                        except ValueError:
                                print('Invalid Selection')
                while True:
                        try:
                                choice = (input('Select a third Skill Proficiency:' + str(RogueSkills)))
                                if choice not in RogueSkills:
                                        raise ValueError()
                                PlayerSkillProf.extend ([choice])
                                RogueSkills.remove(choice)
                                break
                        except ValueError:
                                print('Invalid Selection')
                while True:
                        try:
                                choice = (input('Select a fourth Skill Proficiency:' + str(RogueSkills)))
                                if choice not in RogueSkills:
                                        raise ValueError()
                                PlayerSkillProf.extend ([choice])       
                                RogueSkills.remove(choice)
                                break
                        except ValueError:
                                print('Invalid Selection')
                PlayerSaveProf.extend (['Dexterity','Intelligence'])
                PlayerArmorProf.extend (['Light Armor'])
                PlayerWeaponProf.extend (['Simple Weapons','Hand Crossbows','Longswords','Rapiers','Shortswords'])
                PlayerPrimaryAbility = 'Dexterity'
                PlayerHitDie = 'd8'
                PlayerFeatures.extend (['Expertise','Sneak attack','Thieves Cant'])
                PlayerToolProf.extend (['Thieves tools'])
		#Equipment
        if PlayerClass == 'Wizard':
                WizardSkills = ['Arcana','History','Insight','Investigation','Medicine','Religion']
                while True:
                        try:
                                choice = (input('Select a Skill Proficiency:' + str(WizardSkills)))
                                if choice not in WizardSkills:
                                        raise ValueError()
                                PlayerSkillProf.extend ([choice])
                                WizardSkills.remove(choice)
                                break
                        except ValueError:
                                print('Invalid Selection')
                while True:
                        try:
                                choice = (input('Select a second Skill Proficiency:' + str(WizardSkills)))
                                if choice not in WizardSkills:
                                        raise ValueError()
                                PlayerSkillProf.extend ([choice])
                                break
                        except ValueError:
                                print('Invalid Selection')
                PlayerSaveProf.extend (['Intelligence','Wisdom'])
                PlayerArmorProf.extend ([''])
                PlayerWeaponProf.extend (['Daggers','Darts','Slings','Quarterstaffs','Light Crossbows'])
                PlayerPrimaryAbility = 'Intelligence'
                PlayerHitDie = 'd6'
                PlayerFeatures.extend (['Spellcasting','Arcane Recovery'])
		#Equipment
        #<Enable Background Selection>
        PlayerBackgrounds = ['Acolyte','Criminal','Folk Hero','Noble','Sage','Soldier']
        while PlayerBackground not in PlayerBackgrounds:
                print('Now, choose your BACKGROUND: ', PlayerBackgrounds)
                PlayerBackground = input()
        if PlayerBackground == 'Acolyte':
                PlayerSkillProf.extend (['insight','religion'])
                while True:
                        try:
                                choice = (input('Select a Language' + str(Languages)))
                                if choice not in Languages:
                                        raise ValueError()
                                PlayerLang.extend ([choice])
                                Languages.remove(choice)
                                break
                        except ValueError:
                                print('Invalid Selection')
                while True:
                        try:
                                choice = (input('Select another Language' + str(Languages)))
                                if choice not in Languages:
                                        raise ValueError()
                                PlayerLang.extend ([choice])
                                Languages.remove(choice)
                                break
                        except ValueError:
                                print('Invalid Selection')
                PlayerAbilities.extend (['Shelter Of The Faithful'])
		#equipment
        if PlayerBackground == 'Criminal':
                PlayerSkillProf.extend (['Deception','Stealth'])
                while True:
                        try:
                                choice = (input('Select a Gaming Set Proficiency: ' + str(GamingSets)))
                                if choice not in GamingSets:
                                        raise ValueError()
                                PlayerToolProf.extend ([choice])
                                break
                        except ValueError:
                                print('Invalid Selection')
                PlayerToolProf.extend(['Thieves Tools'])
                PlayerAbilities.extend (['Criminal Contact'])
                #equipment
        if PlayerBackground == 'Folk Hero':
                PlayerSkillProf.extend (['Animal Handling','Survival'])
                while True:
                        try:
                                choice = (input('Select a Artisans Tools Proficiency: ' + str(ArtisansTools)))
                                if choice not in ArtisansTools:
                                        raise ValueError()
                                PlayerToolProf.extend ([choice])
                                break
                        except ValueError:
                                print('Invalid Selection')
                PlayerToolProf.extend(['Land Vehicles'])
                PlayerAbilities.extend (['Rustic Hospitality'])
                #equipment
        if PlayerBackground == 'Noble':
                PlayerSkillProf.extend (['History','Persuasion'])
                while True:
                        try:
                                choice = (input('Select a Gaming Set Proficiency: ' + str(GamingSets)))
                                if choice not in GamingSets:
                                        raise ValueError()
                                PlayerToolProf.extend ([choice])
                                break
                        except ValueError:
                                print('Invalid Selection')
                while True:
                        try:
                                choice = (input('Select a Language' + str(Languages)))
                                if choice not in Languages:
                                        raise ValueError()
                                PlayerLang.extend ([choice])
                                Languages.remove(choice)
                                break
                        except ValueError:
                                'Print Invalid Selection'
                PlayerAbilities.extend (['Position of Privilege'])
                #equipment
        if PlayerBackground == 'Sage':
                PlayerSkillProf.extend (['Arcana','History'])
                while True:
                        try:
                                choice = (input('Select a Language' + str(Languages)))
                                if choice not in Languages:
                                        raise ValueError()
                                PlayerLang.extend ([choice])
                                Languages.remove(choice)
                                break
                        except ValueError:
                                print('Invalid Selection')
                while True:
                        try:
                                choice = (input('Select another Language' + str(Languages)))
                                if choice not in Languages:
                                        raise ValueError()
                                PlayerLang.extend ([choice])
                                Languages.remove(choice)
                                break
                        except ValueError:
                                print('Invalid Selection')
                PlayerAbilities.extend (['Researcher'])
                #equipment
        if PlayerBackground == 'Soldier':
                PlayerSkillProf.extend (['Athletics','Intimidation'])
                while True:
                        try:
                                choice = (input('Select a Gaming Set Proficiency: ' + str(GamingSets)))
                                if choice not in GamingSets:
                                        raise ValueError()
                                PlayerToolProf.extend ([choice])
                                break
                        except ValueError:
                                print('Invalid Selection')
                PlayerToolProf.extend(['Land Vehicles'])
                PlayerAbility.extend(['Military Rank'])
                #equipment
        #<Enable Alignment Selection>
        PlayerAlignments = ['Lawful Good','Neutral Good','Chaotic Good','Lawful Neutral','True Neutral','Chaotic Neutral','Lawful Evil','Neutral Evil','Chaotic Evil']
        while PlayerAlignment not in PlayerAlignments:
                print('Choose your ALIGNMENT: ', PlayerAlignments)
                PlayerAlignment = input()

        #CalculateAttribute Mods
        PlayerStrMod = PlayerStr//2-5; PlayerDexMod = PlayerDex//2-5; PlayerConMod = PlayerCon//2-5; PlayerIntMod = PlayerInt//2-5; PlayerWisMod = PlayerWis//2-5; PlayerChaMod = PlayerCha//2-5
        #Create the Character file
        d = shelve.open(PlayerName, 'c')
        d.update({'PlayerName':PlayerName})
        #Convert lists to sets and back to remove duplicates
        PlayerSkillProf = set(PlayerSkillProf)
        PlayerSkillProf = list(PlayerSkillProf)

        #Calculate Skill Mods
        if 'Acrobatics' in PlayerSkillProf:
                PlayerAcro = PlayerProf + PlayerDexMod
        else:
                PlayerAcro = PlayerDexMod

        if 'Animal Handling' in PlayerSkillProf:
                PlayerAnim = PlayerProf + PlayerWisMod
        else:
                PlayerAnim = PlayerWisMod

        if 'Arcana' in PlayerSkillProf:
                PlayerArca = PlayerProf + PlayerIntMod
        else:
                PlayerArca = PlayerIntMod
        
        if 'Athletics' in PlayerSkillProf:
                PlayerAthl = PlayerProf + PlayerStrMod
        else:
                PlayerAthl = PlayerStrMod
        
        if 'Deception' in PlayerSkillProf:
                PlayerDece = PlayerProf + PlayerChaMod
        else:
                PlayerDece = PlayerChaMod
        
        if 'History' in PlayerSkillProf:
                PlayerHist = PlayerProf + PlayerIntMod
        else:
                PlayerHist = PlayerIntMod
        
        if 'Insight' in PlayerSkillProf:
                PlayerInsi = PlayerProf + PlayerWisMod
        else:
                PlayerInsi = PlayerWisMod
 
        if 'Intimidation' in PlayerSkillProf:
                PlayerInti = PlayerProf + PlayerChaMod
        else:
                PlayerInti = PlayerChaMod
        
        if 'Investigation' in PlayerSkillProf:
                PlayerInve = PlayerProf + PlayerIntMod
        else:
                PlayerInve = PlayerIntMod 
        
        if 'Medicine' in PlayerSkillProf:
                PlayerMedi = PlayerProf + PlayerIntMod
        else:
                PlayerMedi = PlayerIntMod

        if 'Nature' in PlayerSkillProf:
                PlayerNatu = PlayerProf + PlayerIntMod
        else:
                PlayerNatu = PlayerIntMod
        
        if 'Perception' in PlayerSkillProf:
                PlayerPerc = PlayerProf + PlayerWisMod
        else:
                PlayerPerc = PlayerWisMod

        if 'Performance' in PlayerSkillProf:
                PlayerPerf = PlayerProf + PlayerChaMod
        else:
                PlayerPerf = PlayerChaMod
        
        if 'Persuasion' in PlayerSkillProf:
                PlayerPers = PlayerProf + PlayerChaMod
        else:
                PlayerPers = PlayerChaMod

        if 'Religion' in PlayerSkillProf:
                PlayerReli = PlayerProf + PlayerIntMod
        else:
                PlayerReli = PlayerIntMod
        
        if 'Sleight of Hand' in PlayerSkillProf:
                PlayerSlei = PlayerProf + PlayerDexMod
        else:
                PlayerSlei = PlayerDexMod
        
        if 'Stealth' in PlayerSkillProf:
                PlayerStea = PlayerProf + PlayerDexMod
        else:
                PlayerStea = PlayerDexMod
        
        if 'Survival' in PlayerSkillProf:
                PlayerSurv = PlayerProf + PlayerWisMod
        else:
                PlayerSurv = PlayerWisMod

        #Write Variables to Character Dictionary
        d.update({'PlayerGender':PlayerGender,'PlayerRace':PlayerRace,'PlayerSubrace':PlayerSubrace,'PlayerClass':PlayerClass,'PlayerBackground':PlayerBackground,'PlayerAlignment':PlayerAlignment,'PlayerExperience':PlayerExperience,'PlayerLevel':PlayerLevel})
        d.update({'PlayerProf':PlayerProf,'PlayerSkillProf':PlayerSkillProf,'PlayerSaveProf':PlayerSaveProf,'PlayerWeaponProf':PlayerWeaponProf,'PlayerToolProf':PlayerToolProf,'PlayerArmorProf':PlayerArmorProf,'PlayerAbilities':PlayerAbilities,'PlayerFeatures':PlayerFeatures})
        d.update({'PlayerStr':PlayerStr,'PlayerDex':PlayerDex,'PlayerCon':PlayerCon,'PlayerWis':PlayerWis,'PlayerInt':PlayerInt,'PlayerCha':PlayerCha})
        d.update({'PlayerStrMod':PlayerStrMod,'PlayerDexMod':PlayerDexMod,'PlayerConMod':PlayerConMod,'PlayerWisMod':PlayerWisMod,'PlayerIntMod':PlayerIntMod,'PlayerChaMod':PlayerChaMod})
        d.update({'PlayerAcro':PlayerAcro,'PlayerAnim':PlayerAnim,'PlayerArca':PlayerArca,'PlayerAthl':PlayerAthl,'PlayerDece':PlayerDece,'PlayerHist':PlayerHist,'PlayerInsi':PlayerInsi,'PlayerInti':PlayerInti,'PlayerInve':PlayerInve,'PlayerMedi':PlayerMedi,'PlayerNatu':PlayerNatu,'PlayerPerc':PlayerPerc,'PlayerPerf':PlayerPerf,'PlayerPers':PlayerPers,'PlayerReli':PlayerReli,'PlayerSlei':PlayerSlei,'PlayerStea':PlayerStea,'PlayerSurv':PlayerSurv})
        
        print ('Character' +' ' + PlayerName +' has been created.')
        #Close the character file
        d.close()

#Uncomment to allow to run the character_creation function directly.
character_creation()
