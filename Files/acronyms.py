
def find_acronym():
    look_up = input("What acronym would you like?")
    found = False
    try:
        with open("acronyms.txt") as file:
            for line in file:
                if look_up in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print("File not found")
        return
    if not found:
        print("Does not exist")


def add_acronym():
    acronym = input("What acronym would you like?")
    definition = input("What definition would you like?")

    with open("acronyms.txt", "a") as file:
        file.write(acronym + " - " + definition + "\n")

def main():
    choice = input("Find (F) or Add (A)")
    if choice == "F":
        find_acronym()
    elif choice == "A":
        add_acronym()
    else: 
        print("Not valid")

main()