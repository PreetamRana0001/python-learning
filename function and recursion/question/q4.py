'''
sum(1) = 1
sum(2) = 2 + 1
sum(3) = 3 + 2 + 1
sum(4) = 4 + 3 + 2 + 1
sum(n) = n + n-1 + n-2 + ...... + 3 + 2 + 1
'''

def sum(n):
    if n==1:
        return 1
    return  sum(n-1) + n
print(sum(4))