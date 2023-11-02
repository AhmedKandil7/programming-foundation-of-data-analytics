n = int(input('enter number : '))
s = 0
if n < 0 :
    print('The number is negative ')
else :
    for i in range(1, n + 1):
        s += i
    print('summation of numbers = ',s)
