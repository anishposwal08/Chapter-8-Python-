# n! = (n-1)! * n 
# sum(n) = sum(n-1) + n

def recurSum(n):
    if n<=1:
        return n    
    return n + recurSum(n-1)
n=89
print(recurSum(n))