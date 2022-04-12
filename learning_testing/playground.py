# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 17:39:54 2019

@author: jaredalbert
"""

import math
from functools import reduce
l1 = [1,3,4,5,8,9,0,1,2]
l2 = [1,2,3,4, 6,7,8,9,0]
l6 = [3,4,5,2,1,3,4,5,6,6]
l4 = [i for i in zip(l1, l2)]

#l5 = reduce(lambda x, y,z: x if  x[1] > y[1] > z[1] else y, l4)
print(l4)

l3 ='DataCamp'
#
#def test(l):
#    while l:
#        return (l.pop())
#def average(nums):
#
#    # Base case
#    if len(nums) == 1:
#        return nums[0]
#
#    # Recursive call
#    n = len(nums)
#    print(n, nums[-1], nums)
#    return (nums[0] + (n - 1) * average(nums[1:])) / n
#
#print(average(l2))

# Write an expression to get the k-th element of the series
#get_elmnt = lambda k: ((-1)**k)/(2*k+1)
#
#def calc_pi(n):
#    curr_elmnt = get_elmnt(n)
#
#    # Define the base case
#    if n == 0:
#    	return 4
#
#    # Make the recursive call
#    print(curr_elmnt, n)
#    return  (4 * curr_elmnt  +  calc_pi(n-1))
#
#
## Compare the approximated Pi value to the theoretical one
#print("approx = {}, theor = {}".format(calc_pi(500), math.pi))
#def average(nums):
#
#    # Base case
#    if len(nums) == 1:
#        return nums[0]
#
#    # Recursive call
#    n = len(nums)
#    #print(n, nums[-1], nums)
#    return (nums.pop() + average(nums[1:]))/(n)

# Testing the function
#print (average([1, 2, 3, 4, 5]))

#def my_zip(*args):
#
#    # Retrieve Iterable lengths and find the minimal length
##    lengths = list(map(lambda *l:[len(i) for i in l], args))
#    lengths = list(map(len, args))
#    min_length =len(lengths)
#    #return (lengths, min_length)
#
#    tuple_list = []
#    for i in range(0, min_length):
#        # Append new items to the 'tuple_list'
#        tuple_list.append(tuple(map(lambda x: x[i], args)))
#
#    return tuple_list
#print(my_zip([1, 2, 3], ['a', 'b', 'c', 'd'], 'DataCamp'))
#def gcd(a, b):
#    # Define the while loop as described
#    while b != 0:
#        temp_a = a
#        a = b
#        b = temp_a % b
#
#    # Complete the return statement
#    return a
#print([(i,j) for i in l1 for j in l2 if gcd(i,j)==1])

#def cp(a, b):
#    #find co-primes
#    while b != 0:
#        print(f'a: {a}, b: {b}')
#        temp_a = a
#        a = b
#        b = temp_a % b
#
#
#    return(a)
#
#print(cp(27,23))
#
#
#class Camel():
#    def __init__(self, num, *non):
#        self.num = num
#        self.bath = non
#camel = Camel(3, 'bath', 'red')
#
#
#lambda3 = lambda *num: math.sqrt(sum([n**2 for n in num]))
#print(lambda3(2,3,4))
##
#word = ['applec', 'refuge']
#print(list(filter(lambda x:x.count('e')>1, word)))


#print(reduce(lambda x, y : y + x, 'watermeloon'))

#string = 'watermelon'
##print(string[::-1])
#lists = [[1, 4, 8, 9], [2, 4, 6, 9, 10, 1], [9, 0, 1, 2, 4]]
#lists = [[1, 4, 8, 9], [2, 4, 6, 9, 10, 1], [9, 0, 1, 2, 4]]
#common_items = reduce(
#        (lambda x,y:set(x).intersection(set(y))), lists)
#
#print('common items = ' + str(common_items))

# Convert a number sequence into a single number
#nums = [5, 6, 0, 1]
#num = reduce((lambda y, x:str(x)+str(y)), nums)
#print(str(nums) + ' is converted to ' + str(num))
#
#def fact(num):
#    total = num
#    while num >1:
#        total = total * (num-1)
#        num -=1
#    return (total)
##print(fact(4))
#
#def fact2(num):
#    if num ==1:
#        return 1
#
#    return num * fact2(num-1)
#print(fact2(1))
#
#
#def fib(n):
#  print ('n:', n)
#  if n < 2:
#    print(f'first return tuple: {(n, 1)}')
#    return (n, 1)
#
#  fib1 = fib(n-1); print (f'fib1: {fib1}')
#  fib2 = fib(n-2); print (f'fib2: {fib2}')
#
#  return (fib1[0] + fib2[0], fib1[1] + fib2[1] + 1)




