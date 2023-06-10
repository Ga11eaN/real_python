my_string = input('Enter yout string: ')
if len(my_string) < 5:
    print('string len less than 5')
elif len(my_string) > 5:
    print('string len greater than 5')
else:
    print('string len equal 5')


def factors(num):
    for i in range(1, num + 1):
        if not num % i:
            print(f'{i} is a divisor of {num}')

my_num = input('Enter a positive integer: ')
factors(int(my_num))


# p84
while True:
    user_input = input('Press "q" or "Q" to exit: ')
    if user_input in ('q', 'Q'):
        break

for i in range(1, 51):
    if not i % 3:
        continue
    else:
        print(i)

# p88
while True:
    user_input = input('Enter the integer: ')
    try:
        input_int = int(user_input)
        print(f'Your number {input_int} is integer')
        break
    except ValueError:
        print('You wrote not integer! Try again, you bastard!')

# p91
from random import randint
print(f'Your toss is {randint(1, 6)}')
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
for i in range(10_000):
    toss = randint(1, 6)
    if toss == 1:
        one += 1
    elif toss == 2:
        two += 1
    elif toss == 3:
        three += 1
    elif toss == 4:
        four += 1
    elif toss == 5:
        five += 1
    else:
        six += 1
print(f'one: {one}, two: {two}, three: {three}, four: {four}, five: {five}, six: {six}')
print(f'average number of tosses: {(one * 1 + two * 2 + three * 3 + four* 4 + five * 5 + six * 6) / 10000}')
