print("Hello world")

hello = "Hello"
name = input("What's your name?\n")
greeting = hello + " "+ name
print(greeting)

age = int(input("How old are you?\n"))
decades = age // 10
years = age % 10 
print("You are "+ str(decades) + "decades and" + years + "year(s) old.")