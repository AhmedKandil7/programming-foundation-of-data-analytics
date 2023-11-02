n = int(input('Enter the number of numbers:'))
numbers = []
for i in range(n):
  number = int(input("Enter a number: "))
  numbers.append(number)
oddsum = 0
evensum = 0
for number in numbers:
  if number % 2 != 0:
    oddsum += number
  else:
    evensum += number
print("The sum of the odd elements is:", oddsum)
print("The sum of the even elements is:", evensum)