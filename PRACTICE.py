# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 15:05:38 2024

@author: meenu
"""
import numpy as np
from sklearn.impute import SimpleImputer

SimpleImputer(missing_values=np.nan, strategy='mean')

from sklearn.preprocessing import StandardScaler

nums = set([1, 2, 3, 4, 5])
nums.add(6)
new_nums = {7}

nums += new_nums
print(nums)

x = {(1, 2): 'a', (3, 4): 'b'}
y = x[(1, 2)] de
print(y)

x = "aswsome"
def myfunc():
    x = "fantastic"
myfunc()
print("Python is " + x)

def myfunc():
    global x
    x ='fantastic'
myfunc()
print('Python is ' + x)

def myfunction():
    print("Hello Vijayalakshmi")
    
myfunction()
    
def myfunction(**girl):
    print("Her last name is " + girl["lname"])
    
myfunction(fname = "Vijayalakshmi", lname = "Meenuga")

def myfunc(country = "India"):
    print("I am from " + country)
    
myfunc("norway")
myfunc("new yark")
myfunc()
myfunc("America")

def tableOfContents(text):
    lines = text.strip().split('\n')
    toc_lines = []
    
    for line in lines:
        if line.startswith('Chapter'):
            _, chapter_info = line.split(' ', 1)
            chapter_number, title = chapter_info.split(':', 1)
            chapter_number = chapter_number.strip()
            title = title.strip()
            toc_lines.append(f"{chapter_number}. {title}")
toc = generate_toc(markup_content)
print(toc)    
return '\n'.join(toc_lines)
    
    
def myfunc(food):
    for x in food:
        print(x)
        
fruits = ["apple", "sapota", "cherry"]
myfunc(fruits)
    
def myfunc(*, x):
    print(x)
myfunc(x = 3)

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
 
print("\n\nrecursion Example Results")
tri_recursion(8)
    


list = "aaaaaaaaaaaaaaabbbbbbccccccccc"

for i in list:
    if list(i) in list:
        list = list(i) + i
else:
    list(i) =+ i
    print(i)
        
letter = "A"
if letter == "B":
    print("letter is B")
else:
    if letter == "C":
        print("letter is c")
    else:
        if letter == "A":
            print("letter is A")
        else:
            print("letter isn't A, B and C")
            
X = 15

if X > 5:
    print("X is greater than 5")
elif X == 5:
    print("X is eual to 5")
else:
    print("X is .less than 5")  
    
result = "High" if X > 15 else "low"
print(result)

while X < 20:
    print(X)
    X += 1       

while X < 50:
    print(X)
    X += 2

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

list = ["aaaaaaaaaaaabbbbbbbbbbbbbbeeeeeeeeeeedddddddddddd"]

if i in list:
    list[i] = list[i] + 1
else:
    list[i] = 1
print(list)
    
# elements list
list = ['a', 'a', 'a', 'a', 'a', 'b', 'a', 'c', 'b', 'a', 'd', 'b', 'c', 'a', 'b', 'd']
# create empty dictionary
list_dict = {}
# iterate through the list and count occurrences
for item in list:
    if item in list_dict:
        list_dict[item] += 1
    else:
        list_dict[item] = 1
# print the counts       
print(list_dict)
## output {'a': 8, 'b': 4, 'c': 2, 'd': 2}

##### list ####
n = int(input("Enter the size of list : "))

lst = list(map(int, input("Enter the integer\elements:").strip().split()))[:n]

print('The list is:', lst)
    
List = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
print(List)

List.extend([4, 'vijetha', 'giri'])
print(List)

List.reverse()
print(List)    

List.remove(5)
print(List)    

for i in range(1, 5):
    List.remove(i)
print(List)    
    
lst = []

n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input())
    lst.append(ele) 
print(lst)

try:
    my_list = []
    while True:
        my_list.append(int(input()))
        
except:
    print(my_list)

list_of_numbers = list(range(1, 101))
print(list_of_numbers)

range_list = list(range(1, 11))
print(range_list)

import random

random_list = [random.randint(1, 100) for _ in range(10)]  # List of 10 random numbers from 1 to 100
print(random_list)









    
    
    
    
    
    