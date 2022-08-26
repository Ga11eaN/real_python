# Create a string object that stores an integer as its value, then convert that string into
# an actual integer object using int() ; test that your new object is really a number
# by multiplying it by another number and displaying the result

number_string = '5'
number_int = int(number_string)
print('5 * 3 = ',number_int * 3)

# Repeat the previous exercise, but use a floating-point number and float()

number_float_str = '4.2'
number_float = float(number_float_str)
print('4.2 * 2 = ', number_float * 2)

# Create a string object and an integer object, then display them side-by-side with a
# single print statement by using the str() function

str_object = 'my_str'
int_object = 7
print(str_object + str(int_object))
print()
# Create a "float" object (a decimal number) named weight that holds the value 0.2,
# and create a string object named animal that holds the value "newt", then use
# these objects to print the following line without using the format() string method:
# 0.2 kg is the weight of the newt.

animal = 'newt'
weight = 0.2
print(weight, 'kg is the weight of the', animal)

# Display the same line using format() and empty {} place-holders
print('{} kg is the weight of the {}'.format(weight, animal))

# Display the same line using {} place-holders that use the index numbers
print('{0} kg is the weight of the {1}'.format(weight, animal))

# Display the same line by creating new string and float objects inside of the
# format() method
print('{weight} kg is the weight of the {animal}'.format(weight=weight, animal=animal))

# BONUS METHOD: f-string
print(f'{weight} kg is the weight of the {animal}')
print()
# In one line, display the result of trying to find() the substring "a" in the string
# "AAA"; the result should be -1
print('AAA'.find('a'))

# Create a string object that contains the value "version 2.0"; find() the first
# occurrence of the number 2.0 inside of this string by first creating a "float" object that
# stores the value 2.0 as a floating-point number, then converting that object to a
# string using the str() function
my_object = 'version 2.0'
needed_float_number = 2.0
print(my_object.find(str(needed_float_number)))

# Write and test a script that accepts user input using input() , then displays the
# result of trying to find() a particular letter in that input
my_input = input('Enter you input: ')
search_letter = 'a'
print(my_input.find(search_letter))

# Assignment: Turn your user into a l33t h4x0r
some_text = input('Enter some text: ')
some_text = some_text.replace('a', '4')
some_text = some_text.replace('b', '8')
some_text = some_text.replace('e', '3')
some_text = some_text.replace('l', '1')
some_text = some_text.replace('o', '0')
some_text = some_text.replace('s', '5')
some_text = some_text.replace('t', '7')
print(some_text)
