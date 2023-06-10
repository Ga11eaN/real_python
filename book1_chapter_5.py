def cube(num):
    return num * num * num

print(cube(2))
print(cube(5))
print(cube(-6))


def multiply(num1, num2):
    return num1 * num2

print(multiply(2, 3))
print(multiply(4, 8))
print(multiply(1234, 21435))


def celsius_to_farenheit(temp_cel):
    temp_farenheit = temp_cel * 9 / 5 + 32
    return temp_farenheit

def farenheit_to_celsius(temp_far):
    temp_celsius = (temp_far - 32) * 5 / 9
    return temp_celsius

input_cel = 37
input_far = 72

far = celsius_to_farenheit(input_cel)
cel = farenheit_to_celsius(input_far)

print(f'{input_far} degrees F = {cel} degrees C')
print(f'{input_cel} degrees C = {far} degrees F')
    
# p.59 1
for i in range(2, 10):
    print(i)

# p59 2
n = 2
while n < 10:
    print(n)
    n += 1

def doubles(num):
    for i in range(3):
        print(num ** (i + 2))

doubles(2)


def invest(amount, rate, time):
    print(f'principal amount: ${amount}')
    print(f'annual rate of return: {rate}')
    for i in range(time):
        year = i +1
        amount = amount * (1 +rate)
        print(f'year {year}: ${amount}')

invest(100, .05, 8)
invest(2000, .025, 5)
