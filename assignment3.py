"""
calculate factorial using a function
"""


def function(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
num=int(input("Enter a number: "))

result=function(num)
print(result)


"""
using the man module for calculations
"""
import math as m

num=int(input("Enter a number: "))

res1=m.sqrt(num)
print(f"square root: {res1}")

res2=m.log(num)
print(f"logarithm :{res2}")

res3=m.sin(num)
print(f"sine :{res3}")