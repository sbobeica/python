# examle 1
first_name = input('What is you first name? ')
last_name = input('What is you last name? ')

print(first_name, last_name)
print(last_name[::-1], first_name[::-1])


# examle 2
name = input('What is you first and last name? ')

words = name.split(" ")

for word in words:
    lastindex = len(word) - 1
    for index in range(lastindex, -1, -1):
        print(word[index], end='')
    print(end=' ')
print(end='\n')

if __name__ == '__main__'