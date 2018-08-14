# First class functions allow us to treat functions like any other object, so for example we can pass functions as an
# argument to another function, we can returns functions and we can assign functions to variables
def square(x):
    return x * x
def cube(x):
    return x * x * x

'''

1. f = square(x) - here the result of the function would be assignet to the variable f 
2. f = square - here the function is assigned to the variable f 

The difference btw these 2 statements is that in the first one we execute it, 
and in the second we just assign the function to the variable f. 
#f = square(3)  # first example from above
f = square      # second example from above

print(square)
print(f)
print(f(4))
'''

'''
def my_map(funct, arg_list):
    result = []
    for i in arg_list:
        result.append(funct(i))
    return result

squares = my_map(cube, [1,2,3,4,5])     #here 'cube' function is passed as an argument to the my_map function
#squares = my_map(square, [1,2,3,4,5])  #here 'square' function is passed as an argument to the my_map function
print(squares)
'''

'''
def logger(msg):
    def log_message():
        print('Log:', msg)
    return log_message # no paranthesis here because we want to return the function itself not to execute it
log_hi = logger #here logger function is assigned to log_hi variable, but not executed
print(logger)
print(log_hi)

log_hi = logger('hi') #here logger function is executed, and log_hi variable is equal to log_message variable
print(logger)
print(log_hi)
log_hi()
'''

def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}</{0}>' .format(tag, msg))
    return wrap_text

print_h1 = html_tag('h1')
print_h1('Test Headline!')
print_h1('Another Headline!')

print_p = html_tag('p')
print_p('Test Paragraph!')










