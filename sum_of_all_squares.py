"""Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors squared are: 1, 4, 9, 36, 49, 196, 441, 1764. The sum of the squared divisors is 2500 which is 50 * 50, a square!

Given two integers m, n (1 <= m <= n) we want to find all integers between m and n whose sum of squared divisors is itself a square. 42 is such a number.

The result will be an array of arrays or of tuples (in C an array of Pair) or a string, each subarray having two elements, first the number whose squared divisors is a square and then the sum of the squared divisors.

#Examples:

list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
list_squared(42, 250) --> [[42, 2500], [246, 84100]]
The form of the examples may change according to the language, see Example Tests: for more details."""

#Here is my convoluted answer that works; I think it works. It passes the codewars basic test but crashes their server on full testing.


import math


def squares(m):
  l = []
  for number in range(1, m + 1):
    if m % number == 0:
      l.append(number)
      
  return l    

def add_s(l):
  total = 0
  for i in l:
    total = total + i ** 2
  return total  

def s(x):
  return (add_s(x) ** 2)



def list_squared(m, n):
  final_list = []
 
  for i in range(m, n + 1):
    
   
    if math.sqrt(add_s(squares(i))) - round(math.sqrt(add_s(squares(i))))  == 0:
      final_list.append([i, add_s(squares(i))])
      
  return final_list
