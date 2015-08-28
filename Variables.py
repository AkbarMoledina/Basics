__author__ = 'Akbar'

#Assigning 4 different names to 4 different variables
Name1, Name2, Name3, Name4 = "Akbar Moledina", "Prameeth Edirisinge", "Felix Yik Long Tsang", "Foyjun Azher"

#Assigning a single age to 3 different variables
Age1 = Age2 = Age3 = 23
#And a different age to a different variable
Age4 = 25

#Print Names with their respective ages
print(Name1, ":", Age1, ",", Name2, ":", Age2, ",", Name3, ":", Age3, ",", Name4, ":", Age4)

#Slicing the strings to only print first names
print(Name1[0:5], Name2[0:8], Name3[0:5], Name4[0:6])

#Slicing the strings to print other names and last names
print(Name1[6:], Name2[9:], Name3[6:], Name4[7:])