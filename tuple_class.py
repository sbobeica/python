# The tuple class provides an immutable sequence of elements
singleton_tuple = (2,) #even if you want to create a tuple object with just a single element, you must use a comma after it, otherwise it will not be a tuple
print(singleton_tuple) #tuples with just one element are called "singleton tuples"

empty_tuple = tuple() #epty tuple
print('empty tuple:', empty_tuple)

empty_tuple1 = () #epty tuple
print('empty tuple:', empty_tuple1)

tuple_str = tuple('hello')
print(tuple_str)

tuple_list = tuple ([1,2,3,4,[5,6]]) #tuple function converts a list into a tuple, but just the outer list into a tuple, inner list becames an element within the tuple
print(tuple_list)

tuple_list1 = tuple ([1, 2, 3, 4, 5, 6])
print(tuple_list1)
