# The range function generates a sequence of integers
a_range = range(5) #creates a range from 0 up to but not including 5
print('a_range ->', a_range) # prints the range
print('list(a_range) ->', list(a_range)) #prints the elements of the range

#It is often used to execute a "for" loop a number of times
for i in range(2, 10): # from 2 up to but but not including 10
    print(i, end=' ')
print() # line end
# It is simital to the slices function with start, stop and step
a_range =range(10) # stop only
print('list(a_range) ->', list(a_range))

a_range =range(10, 16) # start and stop 
print('list(a_range) ->', list(a_range))

a_range =range(10, -1, -1) # stop, stop and step
print('list(a_range) ->', list(a_range))
