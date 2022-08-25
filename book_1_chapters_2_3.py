print('Print a string that uses double quotation marks inside the string')
print('double quote " inside')

print('\nPrint a string that uses an apostrophe (single quote) inside the string')
print("apostrophe ' inside")

print('\nPrint a string that spans across multiple lines')
print('''string, that spans
across multiple lines''')

print('\nPrint a one-line string that you have written out on multiple lines')
print('one-line string \
that has been written out \
on multiple lines')

print('\nCreate a string and print its length using the len() function')
my_string = 'Lich King'
print(len(my_string))

print('\nCreate two strings, concatenate them (add them next to each other) and print the combination of the two strings')
string_1 = 'Lich'
string_2 = 'King'
print(string_1 + string_2)

print('\nCreate two string variables, then print one of them after the other (with a space added in between) using a comma in your print statement')
string_1 = 'Arthas'
string_2 = 'Lich King'
print(string_1, string_2)

print('\nprint the string "zing" by using subscripting and index numbers on the string "bazinga" to specify the correct range of characters')
bazinga = 'bazinga'
print(bazinga[2:6])

print('\nWrite a script that takes input from the user and displays that input back')
my_input = input('Enter your input: ')
print(f'Your input: {my_input}')

print('\nUse CTRL+SPACE to view all the methods of a string object, then write a script that returns the lower-case version of a string')
my_string = 'SIBIRSKIY LOS'
print(my_string.lower())

print("\nAssignment: Pick apart your user's input")
user_input = input('Tell me your password: ')
print(user_input[0].upper())
