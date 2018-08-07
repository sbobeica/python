# the bytes class provides an immutable sequence
# value must be integers from 0-255 to represent a byte

#first method of creating a bytes objects
bytes_literal = b'Copyright \xc2\xa9' # a method of creating a bytes objects is to use "bytes literal". The string should contain 'b' in front of the string, and the string shoud consist just from ASCII characters, and escaped (\) hexadecimal(\x) characters
print(b'Copyright \xc2 \xa9')
print(bytes_literal)
print (bytes_literal.decode())
bytes_encoded = b'Trademark \xc2\xae'
print(bytes_encoded)
print(bytes_encoded.decode('utf-8'))

#second method of creating a bytes objects is to use "string literal"
string_literal = 'Trademark ®' 
print(string_literal.encode())
bytes_encoded = string_literal.encode() #by encoding "string_literal", it will create a bytes object ("bytes_encoded" in this case)
print(bytes_encoded)
print(bytes_encoded.decode())

#third method of creating a bytes objects is to use "bytes constructor"
bytes_construct = bytes(string_literal, 'utf-8') #by using a "bytes constructor function" agains a "string literal" along with encoding to use (utf-8) , it will create a "bytes" object
print(bytes_construct)
print(bytes_construct.decode())

#fourth method of creating a bytes objects is to use "hexadecimal byte value"
bytes_from_hex = bytes.fromhex('54 72 61 64 65 6d 61 72 6d 20 c2 ae') # this hexadecimal string, using "fromhex method", will create a bytes object
print(bytes_from_hex.decode()) # thi will decode bytes object (bytes_from_hex) into ASCII string of characters

# a bytes sequence behaves similar to a string
print(string_literal.count('T'))
print(string_literal.index('T'))

#however, byte values are used instead of string values
print(bytes_encoded.count(0x54))
print(bytes_encoded.index(0x54))



