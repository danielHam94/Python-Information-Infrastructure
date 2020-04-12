scores = {"Dave": 125, "Abby": 100, "Carrie": 275, "Ben": 150}

print("Current Players:\n" + "".join(sorted(scores.keys())))

name = input("Please enter a Player Name:")

print("The score for", name, "is", scores.get(name, "not found") + ".")
