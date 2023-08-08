acronym = input("What acronym would you like?")
definition = input("What definition would you like?")

with open("softwareacronyms.txt", "a") as file:
    file.write(acronym + " - " + definition + "\n")