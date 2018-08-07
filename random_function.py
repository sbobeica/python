import random

sayings = ('Hi', 'Hello', 'Salut', 'Buna', 'Hey', 'Aloha', 'Ceau')
def greet():
    return random.choice(sayings)

def test_greet():
    for loop in range(11):
        print(greet(), end=' ')

def just_print():
    print('Print something')
    print('Print something')

if __name__ == '__main__':
   print(greet(), '\ngreet test completed\n')

if __name__ == '__main__':
   print(test_greet(), '\ngreetings test completed\n')

if __name__ == '__main__':
   print(just_print(), '\njust_print test completed')