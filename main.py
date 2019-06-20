
VariablesDictionary = {"Name": "Careful", "Artist": "Paramore", "Album": "Riot!", "YearReleased": 2007, "MonthReleased":
                       "June", "DayReleased": 4, "Genre": "Pop", "Length": "3:31", "DurationInSeconds": 211,
                       "Songwriter": "Hayley Williams and Josh Farro", "Producer": "David Bendeth"}

for variables in VariablesDictionary:
    print(variables, ":", VariablesDictionary[variables])


def game(Key, Value):
    if key not in VariablesDictionary.keys():
        return False
    else:
        if value in VariablesDictionary.values():
            return True
        else:
            return False


key = input("Enter a key: ")
value = input("Enter your guess of the value: ")
print(game(key, value))
