#Import Shelve to allow the opening of the shelved file
import shelve

#Define the character_viewer function
def character_viewer():
    print("Character Viewer")
    print("Which Character do you want to view?")
    try:
        PlayerName = input()
        d = shelve.open(PlayerName, 'r')
        print('Name: ' +d['PlayerName'])
        print('Gender: ' +d['PlayerGender'] + ' | Race: ' +d['PlayerSubrace'] +' ' +d['PlayerRace'] +' | Class: ' +d['PlayerClass'] +' | Background: ' +d['PlayerBackground'] +' | Alignment: ' +d['PlayerAlignment'] +' | Experience: ' +str(d['PlayerExperience']))
        print('')
        print('Strength:     ' +str(d['PlayerStr']).rjust(2, '0') +' | Modifier: ' +str(d['PlayerStrMod']).rjust(2, '0')) #+" | Save: " +str(STRS).rjust(2, '0'))
        print('Dexterity:    ' +str(d['PlayerDex']).rjust(2, '0') +' | Modifier: ' +str(d['PlayerDexMod']).rjust(2, '0')) #+" | Save: " +str(DEXS).rjust(2, '0'))
        print('Constitution: ' +str(d['PlayerCon']).rjust(2, '0') +' | Modifier: ' +str(d['PlayerConMod']).rjust(2, '0')) #+" | Save: " +str(CONS).rjust(2, '0'))
        print('Intelligence: ' +str(d['PlayerInt']).rjust(2, '0') +' | Modifier: ' +str(d['PlayerIntMod']).rjust(2, '0')) #+" | Save: " +str(INTS).rjust(2, '0'))
        print('Wisdom:       ' +str(d['PlayerWis']).rjust(2, '0') +' | Modifier: ' +str(d['PlayerWisMod']).rjust(2, '0')) #+" | Save: " +str(WISS).rjust(2, '0'))
        print('Charisma:     ' +str(d['PlayerCha']).rjust(2, '0') +' | Modifier: ' +str(d['PlayerChaMod']).rjust(2, '0')) #+" | Save: " +str(CHAS).rjust(2, '0'))
        print('')
        print('Skills')
        #print("     Acrobatics: " +str(ACRO).rjust(2, '0') +"  | Animal Handling: " +str(ANIM).rjust(2, '0') +"  |        Arcana: " +str(ARCA).rjust(2, '0'))
        #print("      Athletics: " +str(ATHL).rjust(2, '0') +"  |       Deception: " +str(DECE).rjust(2, '0') +"  |       History: " +str(HIST).rjust(2, '0'))
        #print("        Insight: " +str(INSI).rjust(2, '0') +"  |    Intimidation: " +str(INTI).rjust(2, '0') +"  | Investigation: " +str(INVE).rjust(2, '0'))
        #print("       Medicine: " +str(MEDI).rjust(2, '0') +"  |          Nature: " +str(NATU).rjust(2, '0') +"  |    Perception: " +str(PERC).rjust(2, '0'))
        #print("    Performance: " +str(PERF).rjust(2, '0') +"  |      Persuasion: " +str(PERS).rjust(2, '0') +"  |      Religion: " +str(RELI).rjust(2, '0')) 
        #print("Sleight of Hand: " +str(SLEI).rjust(2, '0') +"  |         Stealth: " +str(STEA).rjust(2, '0') +"  |      Survival: " +str(SURV).rjust(2, '0'))

        #print PlayerProficiency, PlayerWeaponProf, PlaayerToolProf, PlayerArmorProf, PlayerAbilities, PlayerClassFeatures
        d.close()
    except:
        print('No Character Found')
    finally:
        None
#Uncomment to allow to run the character_viewer function directly
character_viewer()
