

list1 = []
type(list1)

list1 = list()

list1 = [1, 255, "Three", 400000, True]
print(list1)

len(list1)

# Accessing Elements & Slicing

list[0]
list[3]
list[5]

list1[-1]
list1[-2]

list2 = [0,1,2,3,4,5,6,7,8,9]
len(list2)

list2[4:7]
list2[-4:-1]


planets =  ["Mercury", "Venus", "Earth"]
print(planets)
planets.append("Jupyter")
print(planets)

planets.insert(3, "Mars")
print(planets)

outer_planets = ["saturn", "Uranus", "Nepturne", "Pluto"]

planets.extend(outer_planets)
print(planets)

# Removing  Elements

print(planets)

planets.remove("Pluto")
print(planets)

del planets[2]
print(planets)

planets.pop(2)

# Finding the index of an element

planets.index("Mercury")
planets.index("Earth")
planets.index("Tatooine")

"Eatrh" in planets
"Tatooine" in planets

# Sorting Lists

planets.sort()
print(planets)

planets.sort(reverse = True)
print(planets)


# Copying Lists

list1 = [1,2,3,4]
list2 = list1

print(list1)
print(list2)

list2.append(4)

print(list1)
print(list2)


list1 = [1,2,3,4]
list2 = list1.copy()

print(list1)
print(list2)

list2.append(4)

print(list1)
print(list2)