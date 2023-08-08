#expenses = [10.50, 8, 5, 15, 20, 5, 3]

#sum = 0 

#for x in expenses:
#    sum = sum + x

#print("You spent $", sum, sep = "")

## or 

#total = sum(expenses)

#print(total)

total = 0 
expenses = []

num_expense = int(input("Enter number of expenses"))

for i in range(num_expense):
    expenses.append(float(input("Enter an expense:")))

total = sum(expenses)

print(total)