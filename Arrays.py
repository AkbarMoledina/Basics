__author__ = 'Akbar'

#My six pokemon to challenge the Pokemon League
myPokemon = ["Charizard", "Arcanine", "Houndoom", "Pikachu", "Groundon", "Kyogre", "Rayquaza"]
print(myPokemon)
myPokemonLevels = [94, 76, 70, 79, 86, 84, 90]
print(myPokemonLevels)
myItems = ["Hyper Potion", "Full Heal", "Revive", "Revive", "Full Restore", "Lemonade"]
print(myItems)

#Rayquaza leveled up
myPokemonLevels[6] = 91

#I want to swap Arcanine and Houndoom for Zapdos and Mewtwo since I have a lot of fire damage already
myPokemon[1], myPokemon[2] = "Zapdos", "Mewto"
myPokemonLevels[1], myPokemonLevels[2] = [77, 89]

#Oops, I have seven Pokemon!
del myPokemon[3]
print(myPokemon)
print(myPokemonLevels)

#Nice now I have 6 Pokemon
print("I have", len(myPokemon), "Pokemon in my team")

#Lowest level in my team and highest level in my team
print("The lowest level Pokemon in my team is level ", min(myPokemonLevels), ". " , "The highest level Pokemon in my team is level " ,max(myPokemonLevels), ".", sep="")

#I need to buy a Max Revive ad another Revive before I challenge the Pokemon League
myItems.append("Full Revive")
myItems.append("Revive")
print(myItems)
print("I have ", myItems.count("Revive"), " ", myItems[2], "s", sep="")

#Make a tuple of the Pokemon Team that I plan to use
finalPokemonTeam = (myPokemon)
print(finalPokemonTeam)