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
        print('Strength:     ' +str(d['PlayerStr']).rjust(2, '0') +' | Modifier: ' +str(d['PlayerStrMod']).rjust(2, '0') +" | Save: " +str(d['PlayerStrSave']).rjust(2, '0'))
        print('Dexterity:    ' +str(d['PlayerDex']).rjust(2, '0') +' | Modifier: ' +str(d['PlayerDexMod']).rjust(2, '0') +" | Save: " +str(d['PlayerDexSave']).rjust(2, '0'))
        print('Constitution: ' +str(d['PlayerCon']).rjust(2, '0') +' | Modifier: ' +str(d['PlayerConMod']).rjust(2, '0') +" | Save: " +str(d['PlayerConSave']).rjust(2, '0'))
        print('Intelligence: ' +str(d['PlayerInt']).rjust(2, '0') +' | Modifier: ' +str(d['PlayerIntMod']).rjust(2, '0') +" | Save: " +str(d['PlayerIntSave']).rjust(2, '0'))
        print('Wisdom:       ' +str(d['PlayerWis']).rjust(2, '0') +' | Modifier: ' +str(d['PlayerWisMod']).rjust(2, '0') +" | Save: " +str(d['PlayerWisSave']).rjust(2, '0'))
        print('Charisma:     ' +str(d['PlayerCha']).rjust(2, '0') +' | Modifier: ' +str(d['PlayerChaMod']).rjust(2, '0') +" | Save: " +str(d['PlayerChaSave']).rjust(2, '0'))
        print('')
        print('Skills')
        print("Acrobatics:      " +str(d['PlayerAcro']).rjust(2, '0') +"  | Animal Handling: " +str(d['PlayerAnim']).rjust(2, '0') +"  | Arcana:         " +str(d['PlayerArca']).rjust(2, '0'))
        print("Athletics:       " +str(d['PlayerAthl']).rjust(2, '0') +"  | Deception:       " +str(d['PlayerDece']).rjust(2, '0') +"  | History:        " +str(d['PlayerHist']).rjust(2, '0'))
        print("Insight:         " +str(d['PlayerInsi']).rjust(2, '0') +"  | Intimidation:    " +str(d['PlayerInti']).rjust(2, '0') +"  | Investigation:  " +str(d['PlayerInve']).rjust(2, '0'))
        print("Medicine:        " +str(d['PlayerMedi']).rjust(2, '0') +"  | Nature:          " +str(d['PlayerNatu']).rjust(2, '0') +"  | Perception:     " +str(d['PlayerPerc']).rjust(2, '0'))
        print("Performance:     " +str(d['PlayerPerf']).rjust(2, '0') +"  | Persuasion:      " +str(d['PlayerPers']).rjust(2, '0') +"  | Religion:       " +str(d['PlayerReli']).rjust(2, '0')) 
        print("Sleight of Hand: " +str(d['PlayerSlei']).rjust(2, '0') +"  | Stealth:         " +str(d['PlayerStea']).rjust(2, '0') +"  | Survival:       " +str(d['PlayerSurv']).rjust(2, '0'))
        print('')
        print('Proficiency: +' +str(d['PlayerProf']))
        print('Weapon Proficiency: ' +str(d['PlayerWeaponProf']))
        print('Armor Proficiency: ' +str(d['PlayerArmorProf']))
        print('Tool Proficiency: ' +str(d['PlayerToolProf']))
        print('Abilities: ' +str(d['PlayerAbilities']))
        print('Class Features: ' +str(d['PlayerFeatures']))
        d.close()
    except:
        print('No Character Found')
    finally:
        None
#Uncomment to allow to run the character_viewer function directly
character_viewer()
