n = int(input('Enter the number of terms :'))

n1 = 0
n2 = 1
i = 0

if n == 0:
    print("Invalid no. of terms")
elif n == 1:
    print('Fibonacci number is ', n1)
    print(n1)
else:
    print('Fibonacci numbers are : ')
    while i < n:
        print(n1)
        N = n1 + n2
        n1 = n2
        n2 = N
        i += 1