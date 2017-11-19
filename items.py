class Weapon:
	def _init_(self):
		raise NotImplementedError("Do not create raw Weapon objects.")
	
	def _str_(self):
		return self.name

class Club(Weapon):
		def _init_(self):
				self.name = "Club"
				self.description = ""
				self.damage = 1d4
				self.damage_type = "Bludgeoning"
				self.cost = 1sp
				self.weight = 2lb.
				self.properties = "Light"
				self.weapon_type = "Simple Melee Weapon"
			
class Dagger(Weapon):
		def _init_(self):
				self.name = "Dagger"
				self.description = ""
				self.damage = 1d4
				self.damage_type = "Piercing"
				self.cost = 2gp
				self.weight = 1lb.
				self.properties = "Finesse, Light, Thrown (range 20/60)"
				self.weapon_type = "Simple Melee Weapon"

class Greatclub(Weapon):
		def _init_(self):
				self.name = "Greatclub"
				self.description = ""
				self.damage = 1d8
				self.damage_type = "Bludgeoning"
				self.cost = 2sp
				self.weight = 10lb.
				self.properties = "Two-Handed"
				self.weapon_type = "Simple Melee Weapon"
				
class Handaxe(Weapon):
		def _init_(self):
				self.name = "Handaxe"
				self.description = ""
				self.damage = 1d6
				self.damage_type = "Slashing"
				self.cost = 5gp
				self.weight = 2lb.
				self.properties = "Light, Thrown (range 20/60)"
				self.weapon_type = "Simple Melee Weapon"
	
class Javelin(Weapon):
		def _init_(self):
				self.name = "Javelin"
				self.description = ""
				self.damage = 1d6
				self.damage_type = "Piercing"
				self.cost = 5sp
				self.weight = 2lb.
				self.properties = "Thrown (range 30/120)"
				self.weapon_type = "Simple Melee Weapon"
		
class Light_Hammer(Weapon):
		def _init_(self):
				self.name = "Light Hammer"
				self.description = ""
				self.damage = 1d4
				self.damage_type = "Bludgeoning"
				self.cost = 2gp
				self.weight = 2lb.
				self.properties = "Light, Thrown (range 20/60)"
				self.weapon_type = "Simple Melee Weapon"
		
class Mace(Weapon):
		def _init_(self):
				self.name = "Mace"
				self.description = ""
				self.damage = 1d6
				self.damage_type = "Bludgeoning"
				self.cost = 5gp
				self.weight = 4lb.
				self.properties = ""
				self.weapon_type = "Simple Melee Weapon"
				
class Quarterstaff(Weapon):
		def _init_(self):
				self.name = "Quarterstaff"
				self.description = ""
				self.damage = 1d6
				self.damage_type = "Bludgeoning"
				self.cost = 2sp
				self.weight = 4lb.
				self.properties = "Versatile (1d8)"
				self.weapon_type = "Simple Melee Weapon"

class Sickle(Weapon):
		def _init_(self):
				self.name = "Sickle"
				self.description = ""
				self.damage = 1d4
				self.damage_type = "Slashing"
				self.cost = 1gp
				self.weight = 2lb.
				self.properties = "Light"
				self.weapon_type = "Simple Melee Weapon"
				
class Spear(Weapon):
		def _init_(self):
				self.name = "Spear"
				self.description = ""
				self.damage = 1d6
				self.damage_type = "Piercing"
				self.cost = 1gp
				self.weight = 3lb.
				self.properties = "Thrown (range 20/60), Versatile (1d8)"
				self.weapon_type = "Simple Melee Weapon"
				
class Unarmed_Strike(Weapon):
		def _init_(self):
				self.name = "Unarmed Strike"
				self.description = ""
				self.damage = 1
				self.damage_type = "Bludgeoning"
				self.cost = 0
				self.weight = 0
				self.properties = ""
				self.weapon_type = "Simple Melee Weapon"

class Light_Crossbow(Weapon):
		def _init_(self):
				self.name = "Light Crossbow"
				self.description = ""
				self.damage = 1d8
				self.damage_type = "Piercing"
				self.cost = 25gp
				self.weight = 5lb.
				self.properties = "Ammunition (range 80/320), Loading, Two-Handed"
				self.weapon_type = "Simple Ranged Weapon"

class Dart(Weapon):
		def _init_(self):
				self.name = "Dart"
				self.description = ""
				self.damage = 1d4
				self.damage_type = "Piercing"
				self.cost = 5cp
				self.weight = 1/4lb.
				self.properties = "Finesse, Thrown (range 20/60)"
				self.weapon_type = "Simple Ranged Weapon"		

class Shortbow(Weapon):
		def _init_(self):
				self.name = "Shortbow"
				self.description = ""
				self.damage = 1d6
				self.damage_type = "Piercing"
				self.cost = 25gp
				self.weight = 2lb.
				self.properties = "Ammunition (range 80/320), Two-Handed"
				self.weapon_type = "Simple Ranged Weapon"

class Sling(Weapon):
		def _init_(self):
				self.name = "Sling"
				self.description = ""
				self.damage = 1d4
				self.damage_type = "Bludgeoning"
				self.cost = 1sp
				self.weight = 0
				self.properties = "Ammunition (range 30/120)"
				self.weapon_type = "Simple Ranged Weapon"		

class Battleaxe(Weapon):
		def _init_(self):
				self.name = "Battleaxe"
				self.description = ""
				self.damage = 1d8
				self.damage_type = "Slashing"
				self.cost = 10gp
				self.weight = 4lb.
				self.properties = "Versatile (1d10)"
				self.weapon_type = "Martial Melee Weapon"			

class Flail(Weapon):
		def _init_(self):
				self.name = "Flail"
				self.description = ""
				self.damage = 1d8
				self.damage_type = "Bludgeoning"
				self.cost = 10gp
				self.weight = 2lb.
				self.properties = ""
				self.weapon_type = "Martial Melee Weapon"						