'''
factorial(1) = 1 
factorial(2) = 2 * 1 
factorial(3) = 3 * 2 * 1
factorial(4) = 4 * 3 * 2 * 1
factorial(5) = 5 * 4 * 3 * 2 * 1

factorial(n) = n * n-1 x......3 x 2 x 1
factorial(n) = n * factorial(n-1)
'''

def factorial(n):
    if(n==1 or n==0):

        return 1

    return n * factorial(n-1)

n = int(input("Enter a number: "))
print(f"the factorail of this number is: {factorial(n)}")