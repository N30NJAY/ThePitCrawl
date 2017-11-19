#Game Start
#Character Creation#
#print("Welcome to Character Creation")

#<Enable Race Selection>
#[
#playerRace = " "
#while playerRace != "Human":
                #and playerRace != "Elf" and playerRace != "Dwarf":
	#print("First, choose a RACE: Human")
                #, Elf, Dwarf")
	#playerRace = input()
#]

#<Enable Gender Selection>
#[
#playerGender = " "
#while playerGender != "Male":
                #and playerGender != "Female" and playerGender != "Other":
#	print("Secondly, choose your GENDER: Male")
                #, Female, Other")
#	playerGender = input()
#]

#<Enable Class Selection>
#[
#playerClass = " "
#while playerClass != "Fighter":
                #and playerClass != "Barbarian"
 #       print("Next, choose your CLASS: Fighter")
                #, Barbarian")
  #      playerClass = input()
#]

#<Enable Background Selection>
#[
#playerBackground = " "
#while playerBackground != "Soldier":
                #and playerBackground != "Acolyte"
        #print("Now, choose your BACKGROUND: Soldier")
                #, Acolyte")
        #playerBackground = input()
#]

#<Enable Alignment Selection>
#[
#playerAlignment = " "
#while playerAlignment != "NG":
                ##and playerAlignment != "LG"
        #print("Choose your ALIGNMENT: NG")
                ##, LG")
        #playerAlignment = input()
#]

#<Enable Intro>
#[ 
#Intro#        
#print("You find yourself in a tavern in the town of Adventure.")
#print("A stranger approaches you and seats himself at your table.")
#print("'Hello friend, my name is Don John Mastur, and yours?'")
#playerName = input()
#print("Ah, so you are " +playerName +", the " +playerAlignment +" " +playerGender +" " +playerRace +" " +playerBackground +" who became a " +playerClass)
#]

#DEBUG STATS#  
playerSTR = 16
playerDEX = 14
playerCON = 14
playerINT = 12
playerWIS = 10
playerCHA = 8
playerLVL = 1
playerRace = "Human"
playerClass = "Fighter"
playerBackground = "Soldier"
playerAlignment = "NG"
playerName = "Steve"
playerXP = 0
playerPROF = 0

if playerRace == "Human":
        playerSTR = playerSTR + 1
        playerDEX = playerDEX + 1
        playerCON = playerCON + 1
        playerINT = playerINT + 1
        playerWIS = playerWIS + 1
        playerCHA = playerCHA + 1

playerSIZE = "M"
playerSPD = 30
playerLANG = "Common"

if playerClass == "Fighter":
        playerHD = 10
       playerAPROF = "Light Armor " +"Medium Armor " +"Heavy Armor " +"Shields "
        playerWPROF = "Martial Weapons"
#        print(APROF)
#        print(WPROF)
elif playerClass == "Barbarian":
        print("Barbarian")
else:
        print("else")
playerSTRM = playerSTR//2-5
playerDEXM = playerDEX//2-5
playerCONM = playerCON//2-5
playerINTM = playerINT//2-5
playerWISM = playerWIS//2-5
playerCHAM = playerCHA//2-5
playerHP = playerHD+playerCONM

playerSTRS = playerSTRM + playerPROF
playerDEXS = playerDEXM + playerPROF
playerCONS = playerCONM + playerPROF
playerINTS = playerINTM + playerPROF
playerWISS = playerWISM + playerPROF
playerCHAS = playerCHAM + playerPROF

playerACRO = playerDEX + playerPROF
playerANIM = playerWIS
playerARCA = playerINT
playerATHL = playerSTR
playerDECE = playerCHA
playerHIST = playerINT
playerINSI = playerWIS
playerINTI = playerCHA
playerINVE = playerINT
playerMEDI = playerWIS
playerNATU = playerINT
playerPERC = playerWIS
playerPERF = playerCHA
playerPERS = playerCHA
playerRELI = playerINT
playerSLEI = playerDEX
playerSTEA = playerDEX
playerSURV = playerWIS

#print("Attributes")
#print(STR)
#print(DEX)
#print(CON)
#print(INT)
#print(WIS)
#print(CHA)

#print("Modifiers")
#print(STRM)
#print(DEXM)
#print(CONM)
#print(INTM)
#print(WISM)
#print(CHAM)

#print("Hit Dice")
#print("D" +str(HD))

#print("Hit Points")
#print(HP)

#Sheet#
#Def Sheet#
print("Name: " +playerName +" | Class: " +playerClass +" | Level: " +str(LVL) +" | Background: " +playerBackground )
print("Race: " +playerRace +" | Alignment: " +playerAlignment +" | Experience: " +str(XP))
print(" ")
print("Strength:     " +str(STR).rjust(2, '0') +" | Modifier: " +str(STRM).rjust(2, '0') +" | Save: " +str(STRS).rjust(2, '0'))
print("Dexterity:    " +str(DEX).rjust(2, '0') +" | Modifier: " +str(DEXM).rjust(2, '0') +" | Save: " +str(DEXS).rjust(2, '0'))
print("Constitution: " +str(CON).rjust(2, '0') +" | Modifier: " +str(CONM).rjust(2, '0') +" | Save: " +str(CONS).rjust(2, '0'))
print("Intelligence: " +str(INT).rjust(2, '0') +" | Modifier: " +str(INTM).rjust(2, '0') +" | Save: " +str(INTS).rjust(2, '0'))
print("Wisdom:       " +str(WIS).rjust(2, '0') +" | Modifier: " +str(WISM).rjust(2, '0') +" | Save: " +str(WISS).rjust(2, '0'))
print("Charisma:     " +str(CHA).rjust(2, '0') +" | Modifier: " +str(CHAM).rjust(2, '0') +" | Save: " +str(CHAS).rjust(2, '0'))
print(" ")
print("Skills")
print("     Acrobatics: " +str(ACRO).rjust(2, '0') +"  | Animal Handling: " +str(ANIM).rjust(2, '0') +"  |        Arcana: " +str(ARCA).rjust(2, '0'))
print("      Athletics: " +str(ATHL).rjust(2, '0') +"  |       Deception: " +str(DECE).rjust(2, '0') +"  |       History: " +str(HIST).rjust(2, '0'))
print("        Insight: " +str(INSI).rjust(2, '0') +"  |    Intimidation: " +str(INTI).rjust(2, '0') +"  | Investigation: " +str(INVE).rjust(2, '0'))
print("       Medicine: " +str(MEDI).rjust(2, '0') +"  |          Nature: " +str(NATU).rjust(2, '0') +"  |    Perception: " +str(PERC).rjust(2, '0'))
print("    Performance: " +str(PERF).rjust(2, '0') +"  |      Persuasion: " +str(PERS).rjust(2, '0') +"  |      Religion: " +str(RELI).rjust(2, '0')) 
print("Sleight of Hand: " +str(SLEI).rjust(2, '0') +"  |         Stealth: " +str(STEA).rjust(2, '0') +"  |      Survival: " +str(SURV).rjust(2, '0'))
##VARIABLES
#Stats: STR DEX CON INT WIS CHA
#Saves: STR DEX CON INT WIS CHA
#Mod: STRM DEXM CONM INTM WISM CHAM
#HP AC PROF LVL INIT SPEED HD XP DSS DSF
#ATTACKS SPELLS
#COIN GEAR
#INSP
#LANG
#Skills: ACRO ANIM ARCA ATHL DECE HIST INSI INTI INVE MEDI NATU PERC PERF PERS RELI SLEI STEA SURV
#Special Abilities:

#Racial Options
#Class Options
#Appearance
