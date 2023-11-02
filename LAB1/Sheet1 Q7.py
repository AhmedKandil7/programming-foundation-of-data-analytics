x = int(input('enter x'))
y = int(input('enter y'))
N = x // y
if x % y != 0:
    N += 1
print(N)