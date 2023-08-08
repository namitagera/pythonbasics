
contacts = {
    "number" : 4,
    "students" : 
    [
        {"name" :"Sarah", "email": "sarah@gmail.com"},
        {"name" :"Harry", "email": "harry@gmail.com"},
        {"name" :"Joe", "email": "joe@gmail.com"},
        {"name" :"liz", "email": "liz@gmail.com"}
    ]
}

print("Student emails:")

for student in contacts["students"]:
    print(student["email"])

