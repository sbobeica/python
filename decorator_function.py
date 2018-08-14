# Decorators

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}' .format(original_function.__name__))
        return original_function(*args, **kwargs)  # here original_function is executed and than returned
    return wrapper_function

@decorator_function     # == dsplay = decorator_function(display)
def display():
    print('display function ran')

@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('John', 34)
display()

print(decorator_function)
print(display)
print(display.__name__)