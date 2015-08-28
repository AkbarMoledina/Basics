__author__ = 'Akbar'

#My six pokemon to challenge the Pokemon League
myPokemon = {"Charizard":94, "Arcanine":76, "Houndoom":70, "Pikachu":79, "Groundon":86, "Kyogre":84, "Rayquaza":90}
print(myPokemon)

myItems = {"Hyper Potion": 3, "Full Heal":2, "Revive":6, "Full Restore":2, "Lemonade":5}
print(myItems)

#Rayquaza leveled up
myPokemon["Rayquaza"] = 91

#I want to swap Arcanine and Houndoom for Zapdos and Mewtwo since I have a lot of fire damage already
del myPokemon["Arcanine"]
del myPokemon["Houndoom"]
subPokemon = {"Zapdos": 77, "Mewto" :89}
myPokemon.update(subPokemon)
print(myPokemon)

#Oops, I have seven Pokemon!
del myPokemon["Pikachu"]

#Nice now I have 6 Pokemon
print("I have", len(myPokemon), "Pokemon in my team")

#Lowest level in my team and highest level in my team
print("The lowest level Pokemon in my team is level ", min(myPokemon.values()), ". " , "The highest level Pokemon in my team is level " ,max(myPokemon.values()), ".", sep="")

#Make a tuple of the Pokemon Team that I plan to use
finalPokemonTeam = (myPokemon)
print(finalPokemonTeam)