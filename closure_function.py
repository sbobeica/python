# Closure is a inner function that remembers and has access to variables (so called free variables) in the local scope in which it was created
# even after the outer function finished its execution
# Closures allow to take advantage of first class functions
# Free variables are variables that are created into outer function but inner function have access to them even after outer function finished its execution
'''
def outer_func(msg):
    message = msg
    def inner_func():
        print(message)  # Here "message" variable is called a "free variable" because even the message variable wasn't
                        # created within inner_func but inner_func does have access to it
    return inner_func   # it returns inner_func to the outer_func waiting to be executed (it do not execute it as it would have done if there were parenthesis)

my_func = outer_func('Hi')  # my_func variable in fact is a function now, because it is equal to inner_func, because outer_func
                            # has been executed and it returned inner_func as a result
print(my_func)          # we can se here that my_func is equal to inner_func
print(my_func.__name__) # we can se here that my_func is equal to inner_func
my_func()   # what is interesting here is that when we execute my_func, outer_func has already finished its execution
            # but we still have access to its variable "message" via inner function. So that is what a "CLOSURE" does
'''

import logging
logging.basicConfig(filename='example.log', level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func # it returns the log_func function, not execute it as if there were parenthesis

def add(x, y):
    return x+y

def sub(x, y):
    return x-y

add_logger = logger(add)    #Here we execute the "logger" function and because "logger function" returns
                            #"log_func" in this way we are assigning the "log_funct" function to the "add_logger" variable.
                            #So now when we execute "add_logger" variable/function in fact we execute "log_func" function
sub_logger = logger(sub)

add_logger(3, 3)
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(20, 10)