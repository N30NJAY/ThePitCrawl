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
        print(player['PlayerSubrace'])
        d.close
    except:
        print('No Character Found')
    finally:
        None
character_viewer()
