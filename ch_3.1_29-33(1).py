"""
Group Member 1 : Rami Kroma 
Group member 2 : Long Nguyen
Group member 3 : suhaib Chaudhry
"""

#Define function prob_29 and pass list L into it
#Create new dictionary called modes
#	Run a for loop for the items in list L
#		If it finds a key in modes
#			Increment the value by one
#		Else
#			Set the value to one
#	Create variables big_key and big_value and set them both to zero
#	Run a for loop for the items in modes
#		If current value in modes is larger than big value ???
#			Set big value to current value in modes ???
#			Set big key to the current value ???
#	Return big key and big value ???

def prob_29(L):
    modes = {}

    for thing in L:
        if thing in modes:
            modes[thing] += 1
        else:
            modes[thing] = 1

    big_key, big_value = 0, 0
    for thing in modes:
        if modes[thing] > big_value:
            big_value = modes[thing]
            big_key = thing

    return big_key, big_value

#Define function prob_30 and pass list L into it
#	Create new dictionary called modes
#	Run a for loop that runs through the items in list L
#		If it finds a key in modes
#			Increment the value by one
#		Else
#			Set the value to one
#	Return the dictionary

def prob_30(L):
    modes = {}

    for thing in L:
        if thing in modes:
            modes[thing] += 1
        else:
            modes[thing] = 1

    return modes

#Define a function called prob_31 and pass list L into it
#	Create a new array called repeated
#	Run a for loop that goes through the items in list L
#		If the value in L is not inside the array repeated
#			Add value to the end of the array repeated
#		Else
#			Return the value
#	Return statement “no term fits the criteria” if the array is empty

def prob_31(L):
    repeated = []

    for thing in L:
        if thing not in repeated:
            repeated.append(thing)
        else:
            return thing

    return 'No term fits the criteria.'

#Define a function called prob_32 and past the list L into it
#	Create a variable called big_sum and set it to 0
#	Run a for loop that goes through the items in list L
#		Add the current value to big_sum
#		If the current value is larger than big sum
#			Return the current value
#	Return statement “no term fits the criteria” if the big sum is zero

def prob_32(L):
    big_sum = 0

    for thing in L:
        big_sum += thing
        if thing > big_sum:
            return thing

    return 'No term fits the criteria.'

#Define a function named prob_33 and past the list L into it
#	Run a for loop that runs through the list of values in the list L
#		If the current value is less than the previous value of L
#			Return the current value
#	Return statement “no term fits the criteria” if nothing is returned

def prob_33(L):

    for i in range(1, len(L)):
        if L[i] < L[i - 1]:
            return L[i]

    return 'No term fits the criteria.'

#Define a function named selection_sort and past the list L into it
#	Run a for loop that runs through the list of values in the list L
#		Create a second for loop that rusn through the list backwards
#			If the current element is less than the previous element
#				swap the values of the current current index and the previous index
#	return the list L

def selection_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1, i, -1):
            if L[j] < L[j-1]:
                L[j], L[j-1] = L[j-1], L[j]
    return L


l= [3,4,1,9,3,6,5,8]
#Shaker Sort 
"""First we creat a function that performs a swap 
initiate the highest_index and lowest_index variables referring to indexes,
and no swap to false
enter while loop if NOT noswap and highest_index - lowest_index is greater than one 
for j is in range lowest_index to highest_index compare both indecies and if the increment 
is higher thant the selected index algorathim will swap 
enter a second for loop going from the highest_index limit to the lowest_index limit from the
index , swapping the index if the number before the selected index is higher
increment the lowest_index index by one """
def shaker_sort(l):
    def swap(i, j):
        l[i], l[j] = l[j], l[i]
 
    highest_index = len(l) - 1
    lowest_index = 0
 
    swapNot = False
    while (not swapNot and highest_index - lowest_index > 1):
        swapNot = True
        for j in range(lowest_index, highest_index):
            if l[j + 1] < l[j]:
                swap(j + 1, j)
                swapNot = False
        highest_index = highest_index - 1
 
        for j in range(highest_index, lowest_index, -1):
            if l[j - 1] > l[j]:
                swap(j - 1, j)
                swapNot = False
        lowest_index = lowest_index + 1
        

#Matrix and Vectors dot product 
"""Since matrices are represented as multi dimentional arrays the most convenient
way of representing matrecies is using the "numpy" class and its predefined 
matrix operations
step 1: import class numpy as np
step 2:
set __matrix__ = a multi dimentional array using the np. function
set __vector__  = a vector 
step 3:
    use the .dot function to perform the operation"""
import numpy as np
__matrix__ = np.array([[ 5, 1 ,3], 
                  [ 1, 1 ,1], 
                  [ 1, 2 ,1]])
__vector__ = np.array([1, 2, 3])
result = __matrix__.dot(__vector__)
print(result)
# The dictionary below holds the above function to be executed. They're executed in the print statement inside of the f-string itself with the above list "l" being passed.

# When you iterate through objects in a dictionary, you iterate through the dictionary's keys by default. So in the below, "n" refers to the strings in the dictionary.

thingstodo = {'29': prob_29, '30': prob_30, '31': prob_31, '32': prob_32, '33': prob_33, 'selection sort': selection_sort}
for n in thingstodo:
    print(f'Problem {n}:\n  Output: {thingstodo[n](l)}')
