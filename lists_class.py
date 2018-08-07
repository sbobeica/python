# The list class provides a mutable sequence of elements
# lists are sorounded by []

empty_list = list()
print(empty_list)

empty_list1 = []
print(empty_list1)

#lists based on strings
list_str = list('hello') #a list based on string, it will display each element of the string as an element within the list
print(list_str)

#lists based on tuples
list_tuple = list((1, 2, (3, 5, 7))) #
print(list_tuple)

#lists based on syntax
list_syntax = [1, 2, 'a', 'c, f']
print(list_syntax)

#membership check
print('a' in list_syntax) # with "in" operator, we can chech whether or not a character is in the string
print(3 not in list_syntax)

#append
list_syntax.append(5) #append at the end of the list
print(list_syntax)
list_syntax.append([3, 4])
print(list_syntax)
last_elem = list_syntax.pop() #it will errase last element but at the same time, last element will be stored into "last_elem" variable
print(last_elem)
print(list_syntax)

#errase
list_syntax.pop() #it will erase the last element from the list. Errase removes by index value
print(list_syntax)

#extend
list_syntax.extend([6, 7]) # it wil extend the existing list, rather then create a list within the list
print(list_syntax)

#insert
list_syntax.insert(0, 7) # it wil insert element '7'to the existing list, at the index zero
print(list_syntax)

#remove
list_syntax.remove(7) #it will remove the element with the value of 7
print(list_syntax)

#length
print('length ->', len(list_syntax))

#clear
list_syntax.clear() #it will clear entire list
print(list_syntax)

#length
print('length ->', len(list_syntax))

print(list_str)
print(min(list_str)) # display the element with the lowest value of the list
print(max(list_str)) # display the element with the highest value of the list
print(sorted(list_str)) # it sorts out the list in alfabetical order but do not store it
print(list_str)
list_str.sort() # it sorts out the list in alfabetical order and store it
print(list_str)
print(list_str.count('o'))
print(list_str.index('o'))

int_list = list((3, 6, 99, 11, 309, 0, 1, 15, 2))
print(int_list)
int_list.sort()
print(int_list)


