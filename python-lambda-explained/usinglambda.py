'''
Created on Jun 22, 2017

@author: jwang02
'''

f = lambda x, y : x + y
print f(1,1)


# As the name suggests, filter creates a list of elements for which a function returns true. 
# The filter resembles a for loop but it is a builtin function and faster.
# Here is a short and concise example:

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# More using lambda operator in Filtering
fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2, fib)
print result

result = filter(lambda x: x % 2 == 0, fib)
print result

# Reduce is a really useful function for performing some computation on a list 
# and returning the result. It applies a rolling computation to sequential pairs of values 
# in a list. For example, if you wanted to compute the product of a list of integers.

# Iteration
product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num
    print product

# Reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print product

# More using lambda operator in Reducing a List
print reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])

f = lambda a,b: a if (a > b) else b
print reduce(f, [47,11,42,102,13])

# Using lambda operator in map() Function
def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)

# init temp to celsius
temp = (36.5, 37, 37.5,39)
F = map(fahrenheit, temp)
C = map(celsius, F)
print F
print C 


