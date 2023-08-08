movies = {"Grinch" : "11.00 am",
          "Rudolph": "1.00 pm",
          "Stars": "2.00 pm"  }

print("We have these movies:")

for key in movies:
    print(key)

movie = input("What movie do you want showtime for?\n")

showtime = movies.get(movie)

if showtime == None:
    print("Not found")
else: 
    print(movie,"is playing at", showtime)