"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""
import math

x = 10
y = 2.24552
z = "I like turtles!"

# Using the print operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

def round_up(n, decimals=0): 
    multiplier = 10 ** decimals 
    return math.ceil(n * multiplier) / multiplier

print('Printed Using Print Method')
print('x is '+ str(x)+', y is '+str(round_up(y-(2.25% y),2))+', z is "'+z+'"')

# Use the 'format' string method to print the same thing
print('Printed Using format Method')
print('x is {}, y is {}, z is "{}"'.format(str(x),str(round_up(y-(2.25% y),2)),z))

# Finally, print the same thing using an f-string
print('Printed Using f-string Method')
print(f'x is {str(x)}, y is {str(round_up(y-(2.25% y),2))}, z is "{z}"')