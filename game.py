from player import Player
import CharacterCreation
import shelve


def play():
        print("The Pit and the Python")
        print("Which Character will you play?")
        PlayerName = input()
        try:
                d = shelve.open (PlayerName, 'wb')
        except:
                print('No Character found, creating new Character')
                CharacterCreation.character_creation()
                d = shelve.open (PlayerName, 'wb')
        finally:
                d.close
        player = Player()
        while True:
                action_input = get_player_command()
                if action_input in ['n', 'N']:
                        print("Go North!")
                elif action_input in ['s' 'S']:
                        print("Go South!")
                elif action_input in ['e' 'E']:
                        print("Go East!")
                elif action_input in ['w' 'W']:
                        print("Go West!")
                elif action_input in ['i', 'I']:
                        player.print_inventory()
                elif action_input in ['c', 'C']:
                        player.print_sheet()
                else:
                        print("Invalid action!")


def get_player_command():
        return input('Action: ')

play()
