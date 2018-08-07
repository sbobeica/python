
def isum(*args):
    print('args ->', args)
    total = 0
    for arg in args:
        total += arg
    return total

def ilist(alpha, betta = 'default', gamma = 'assumed'):
    return alpha, betta, gamma

def iflex(**kwargs):
    print('kwargs ->', kwargs)
    for key in kwargs:
        print(key, '->', kwargs[key])
    return tuple(kwargs.values())

num = (1,2,3,3)
isum(*num)
print(isum(*num))

alphabet = {'alpha': '12', 'betta': '132', 'gamma': 'asd'}

iflex(**alphabet)

print(alphabet.values())

if __name__ == '__name__':
    print(alphabet)
