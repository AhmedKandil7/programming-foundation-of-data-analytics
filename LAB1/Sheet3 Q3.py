vowels = ["a", "e", "i", "o", "u"]
statement = input("Enter a statement: ")
vowelnum = 0
for i in statement:
  if i in vowels:
    vowelnum += 1

if vowelnum == 0:
  print("No vowels found.")
else:
  print("The number of vowels in the statement is:", vowelnum)