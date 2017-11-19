import items, shelve

class Player():
    
    def print_sheet(self):
        d = shelve.open('Jay', 'r')
        try:
            player = d['player']
        finally:
            d.close
        print(player['PlayerGender'] + " " + player['PlayerRace'])


