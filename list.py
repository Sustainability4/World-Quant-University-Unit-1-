# -*- coding: utf-8 -*-
"""list.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q6PD5A2XxUSb6qfeBusLiCawpRjcYR_2
"""

# an example of list 
beans_recipe = ['Soak beans in water', 'Dissolve salt in water', 'Heat water and beans to boil', 
                'Drain beans when done cooking']

"""Sometimes we will store information in individual variables, but often we will be working with several pieces of information that we want to group together because of their relationship or similarity. For example, if we were shopping for groceries, we could store each item we are going to buy in separate variables or we could store all of the items in one list."""

grocery_a = 'chicken'
grocery_b = 'onions'
grocery_c = 'rice'
grocery_d = 'peppers'
grocery_e = 'bananas'

grocery_list = ['chicken', 'onions', 'rice', 'peppers', 'bananas']

# which approach is better 
def buy_groceries_individual(item_a, item_b, item_c, item_d, item_e):
    print('Buying %s...' % item_a)
    print('Buying %s...' % item_b)
    print('Buying %s...' % item_c)
    print('Buying %s...' % item_d)
    print('Buying %s...' % item_e)

def buy_grocery_list(items):
    for item in items:
        print('Buying %s...' % item)

buy_groceries_individual(grocery_a, grocery_b, grocery_c, grocery_d, grocery_e)

buy_grocery_list(grocery_list)

"""By using a list, we could use a for loop to write a much shorter function. But even more important, buy_grocery_list is much more flexible. What if instead of buying five items, we wanted to buy more or less?"""

short_grocery_list = ['chicken', 'onions', 'rice']

buy_grocery_list(short_grocery_list)

long_grocery_list = ['chicken', 'onions', 'rice', 'peppers', 'bananas', 'squash']

buy_grocery_list(long_grocery_list)

list_of_list = [[1,2,3],['a','b','c']]
list_of_list

"""we can store any type of data in the list """

int_list = [2, 6, 3049, 18, 37]
float_list = [3.7, 8.2, 178.245, 63.1]
mixed_list = [26, False, 'some words', 1.264]

print(int_list)
print(float_list)
print(mixed_list)

"""there can be any structure of list. It is highly flxible. We describe the Python `list` as _heterogeneous_ because it can hold a collection of mixed objects. This is one of the major defining properties of the Python `list`.

You may have also noticed that when we put data into a `list` in particular order, it stays in that order when we `print` or use the `list` in a `for` loop. Because `list` preserves order, we say it is _ordered_. We can use this property to retrieve particular items from a `list` based on their position (or **index**) in the list.
"""

confusing_list = [[23, 73, 50], 'some words', 12.308, [[False, True], 'more words']]
print(confusing_list)

"""Printing grocery_list[2] returned the third item in the list: 'rice'. Why did it return the third item if we asked for the item at index 2? Python lists are zero-indexed."""

print(grocery_list[0])
print(grocery_list[1])
print(grocery_list[2])

# slicing the list 
print(grocery_list[1:4])
print(grocery_list[3:])#same as a grocery_list[3:len(grocery_list)]
print(grocery_list[:3])

"""Python also has a negative indexing syntax, allowing us to access the list from the end instead of the beginning. The last element is indexed by -1."""

print(grocery_list[-1])
print(grocery_list[-3:])

"""
We can also slice a list using a step-size other than 1. For instance, we can slice every other item of the list, or even reverse the list by making negative steps."""

print(grocery_list[::2])
print(grocery_list[4:1:-1])

# How the range function works 
print(list(range(0, 10, 3)))
print(list(range(104, 100, -1)))
print(list(range(5)))

# Appending the list 
grocery_list = ['chicken', 'onions', 'rice', 'peppers', 'bananas']
print(grocery_list)
grocery_list.append('squash')
print(grocery_list)
grocery_list.append(['bread', 'salt'])
print(grocery_list) # what happened?

# this can be used to ensure that we get all the functions we can apply 
dir(grocery_list)

print(grocery_list)
print(grocery_list.pop(-3)) # remove the last item from the list and return it
#by default it will pop out the last item of the list 
print(grocery_list)

print(grocery_list)
del grocery_list[-1] # delete the last item
print(grocery_list)

grocery_list.sort()
print(grocery_list)

"""Here we assigned the name a to the value 4 and then b to be equal to a. But, b does not point to a, it points to the variable that has the name a. Thus, assigning the name b to the value of a does not cause the value of b to change when the value of a changes.

Lets see another example, here we will make use of a Python list. We will go over more about lists in the next lecture, for now, think of it as an ordered collection of Python variables (technically objects). In this case, we will do exactly what we did before, but instead of modifying where a points, we will modify the object to which it points. In this case, we will see that b does in fact change. This is because they are both pointing to the same variable in memory!

Variables and names are not the same thing in python. For instance, run the following code
"""

a = 4
b = a
print(a, b)
a = 5
print(a, b)

a = [3, 2, 1]
b = a
print(a, b)
a[1] = 5
print(a, b)

