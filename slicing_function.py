# Slicing allows access one or more elements of a sequence

# Immutable sequences include tuple, strings, and bytes
a_tuple = ('a', 1, 2, (3, 4))
a_string = 'immutable'
a_bytes = b'sequence'

# Mutable sequences include lists and bytearrays
a_list = [5,6,7,8,(4,5)]
a_byte_array = bytearray(b'mutable')

# Accessing is allowed in all sequences
print('a_tuple[0] ->', a_tuple[0])
print(a_tuple)
print(a_tuple[-1])
print('a_string[1] ->', a_string[1])
print(a_string)
print('a_bytes[2] ->', a_bytes[2])
print(a_bytes)
print('a_list[3] ->', a_list[3])
print(a_list)
print('a_byte_array[4] ->', a_byte_array[4])
print(a_byte_array)

# Negative indexs are from the end
print('a_tuple[-1] ->', a_tuple[-1])
print('a_string[-2] ->', a_string[-2])
print('a_bytes[-3] ->', a_bytes[-3])
print('a_list[-4] ->', a_list[-4])
print('a_byte_array[-5] ->', a_byte_array[-5])

# Subslices can be accessed with two indexs 
print('a_list[0:2] ->', a_list[0:2]) #it will display elements starting from index 0 up to but not including index 2
print('a_list[:2] ->', a_list[:2]) #if we do not have anyting before : it means starting from index 0
print('a_list[2:5] ->', a_list[2:5]) #it will display elements starting from index 2 up to but not including index 5
print('a_list[2:] ->', a_list[2:]) #it will display elements starting from index 2 up to the end
print('a_list[:] ->', a_list[:]) #it will display all elements, it's called "full slice notation"

list_ref = a_list   #it will make a reference to the list "a_list". Whenever we make changes into "list_ref" it would affect the "a_list" as well, and viceversa.
print('a_list is list_ref ->', a_list is list_ref)
list_copy = a_list[:] # using full slice notation ([:]) it will get a copy of the "a_list" and changes made into the "list_copy" would not affect "a_list" and viceversa.
print('a_list is list_copy ->', a_list is list_copy)

# Steps can be taken with a third parameter
print('a_list[::2] ->', a_list[::2]) #it will pick up every other element
print('a_list[1:4:2] ->', a_list[1:4:2]) #you can start at a particular index, stop at a particular index, and specify the step as well
print('a_string[::-1] ->', a_string[::-1]) # "-1" means to reverse and in this case because of the "full slice notation" it will reverce entire sequences

# Use additional slices to access elements with sequences
print('a_list ->', a_list) 
print('a_list[4] ->', a_list[4])       # it dyslais the elements from the index 4, there are 2 elements
print('a_list[4][0] ->', a_list[4][0]) # because index 4 contains 2 elements, we can slice further. It means show the element at index 0 from index 4
print('a_list[4][1] ->', a_list[4][1]) # because index 4 contains 2 elements, we can slice further. It means show the element at index 1 from index 4

# Mutable sequences can be updated with slice
print('a_list ->', a_list) 
a_list[0] = 'five' #it will change element from index 0 with word "five"
print('a_list ->', a_list) 
a_list[1:4] = [10,11,12] #it will change elements from index 0 up to but not including index 4 with 10, 11 and 12 
print('a_list ->', a_list) 

# A slice object can be used in the [ ] for slicing
a_slice = slice(4) # it creates a slice object "a_slice" that has just stop index which is 4, it do not have neither starting index nor a steping value
print('a_slice ->', a_slice)
print('a_list[a_slice] ->', a_list[a_slice])

a_slice = slice(1,5) # it creates a slice object "a_slice" that has a start index which is 1, a stop index which is 5, it do not a steping value
print('a_slice ->', a_slice)
print('a_list[a_slice] ->', a_list[a_slice])

a_slice = slice(1,5,2) # it creates a slice object "a_slice" that has a start index which is 1, a stop index which is 5, and a step value of 2
print('a_slice ->', a_slice)
print('a_list[a_slice] ->', a_list[a_slice])





