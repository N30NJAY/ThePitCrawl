#Import Shelve to allow the opening of the shelved file
import shelve

#Define the character_viewer function
def character_viewer():
    print("Character Viewer")
    print("Which Character do you want to view?")
    try:
        PlayerName = input()
        d = shelve.open(PlayerName, 'r')
        player = d['player']
        print('Name: ' +player['PlayerName'])
        print('Gender: ' +player['PlayerGender'] + ' | Race: ' +player['PlayerSubrace'] +' ' +player['PlayerRace'] +' | Class: ' +player['PlayerClass'] +' | Background: ' +player['PlayerBackground'] +' | Alignment: ' +player['PlayerAlignment']) #+' | Experience: " +str(XP))
        print(" ")
        print('Strength:     ' +str(player['PlayerStr'])) #+' | Modifier: " +str(STRM).rjust(2, '0') +" | Save: " +str(STRS).rjust(2, '0'))
        print('Dexterity:    ' +str(player['PlayerDex'])) #+" | Modifier: " +str(DEXM).rjust(2, '0') +" | Save: " +str(DEXS).rjust(2, '0'))
        print('Constitution: ' +str(player['PlayerCon'])) #+" | Modifier: " +str(CONM).rjust(2, '0') +" | Save: " +str(CONS).rjust(2, '0'))
        print('Intelligence: ' +str(player['PlayerInt'])) #+" | Modifier: " +str(INTM).rjust(2, '0') +" | Save: " +str(INTS).rjust(2, '0'))
        print('Wisdom:       ' +str(player['PlayerWis'])) #" | Modifier: " +str(WISM).rjust(2, '0') +" | Save: " +str(WISS).rjust(2, '0'))
        print('Charisma:     ' +str(player['PlayerCha'])) #" | Modifier: " +str(CHAM).rjust(2, '0') +" | Save: " +str(CHAS).rjust(2, '0'))
        print(' ')
        #print('Skills')
        #print("     Acrobatics: " +str(ACRO).rjust(2, '0') +"  | Animal Handling: " +str(ANIM).rjust(2, '0') +"  |        Arcana: " +str(ARCA).rjust(2, '0'))
        #print("      Athletics: " +str(ATHL).rjust(2, '0') +"  |       Deception: " +str(DECE).rjust(2, '0') +"  |       History: " +str(HIST).rjust(2, '0'))
        #print("        Insight: " +str(INSI).rjust(2, '0') +"  |    Intimidation: " +str(INTI).rjust(2, '0') +"  | Investigation: " +str(INVE).rjust(2, '0'))
        #print("       Medicine: " +str(MEDI).rjust(2, '0') +"  |          Nature: " +str(NATU).rjust(2, '0') +"  |    Perception: " +str(PERC).rjust(2, '0'))
        #print("    Performance: " +str(PERF).rjust(2, '0') +"  |      Persuasion: " +str(PERS).rjust(2, '0') +"  |      Religion: " +str(RELI).rjust(2, '0')) 
        #print("Sleight of Hand: " +str(SLEI).rjust(2, '0') +"  |         Stealth: " +str(STEA).rjust(2, '0') +"  |      Survival: " +str(SURV).rjust(2, '0'))

        d.close
    except:
        print('No Character Found')
    finally:
        None
#Run the character_viewer function
character_viewer()
