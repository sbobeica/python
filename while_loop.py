# The while loop executes a suite of code if its condition is True

counter = 3
while counter > 0:
    print('Counting down:', counter)
    counter -= 1

while counter > 0:
    print('Never executes suite')
    print('When condition is False')
print('counter ->', counter)

while 1: # every number but zero is considered as True
    print('Executes at least once')
    if not counter:
        break
print('counter ->', counter)

names = ['Tom', 'Ellen']
while names: # while "names" is true (while there are names in "names" list)
    print(names.pop(),'is going') # pop will pop out names

results = [1, 0, 1]
processed = 0
passed = 0
while results:
    processed += 1
    result = results.pop()
    if not result: # here when "result" is False (zero), "if not False" then it is "True", so the "continue" will be taken into consideration, which means "while" will start again without "passed" to be executed
        continue
    passed += 1
else:
    print('Processed:', processed, 'Passed:', passed)
