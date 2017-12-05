from CharacterCreation import character_creation
from CharacterViewer import character_viewer

def ModuleSelection():
    InstalledModules = ['CharacterCreation','CharacterViewer']
    print('The Pit and Python')
    print('What do you want to do?', InstalledModules)
    ModuleSelection = input()
    try:
        if ModuleSelection == 'CharacterCreation':
            character_creation()
        if ModuleSelection == 'CharacterViewer':
            character_viewer()
        if ModuleSelection not in InstalledModules:
            raise ValueError()
    except ValueError:
        print('Module Not installed')

ModuleSelection()
