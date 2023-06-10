# p99
desserts = ['ice cream', 'cookies']
desserts.sort()
print(desserts.index('ice cream'))
food = desserts[:]
food.extend(['broccoli', 'turnips'])
print(food, desserts)
food.remove('cookies')
print(food[:2])
breakfast = 'cookies, cookies, cookies'.split(', ')
print(breakfast)

def one_twenty(numbers):
    output = []
    for num in numbers:
        if num >= 1 and num <= 20:
            output.append(num)
    return output

result = one_twenty([2, 4, 8, 16, 32, 64])
print(result)


def enrollment_stats(main_list):
    enroll_values = []
    tuition_fees = []
    for university in main_list:
        enroll_values.append(university[1])
        tuition_fees.append(university[2])
    return enroll_values, tuition_fees

def mean(input_list):
    my_sum = 0
    for i in input_list:
       my_sum += i
    mean_value = my_sum / len(input_list)
    return mean_value

def median(input_list):
    input_list.sort()
    median_index = len(input_list) // 2
    if not len(input_list) % 2:
        median_value = (input_list[median_index] + input_list[median_index - 1]) / 2
    else:
        median_value = input_list[median_index]
    return median_value

universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]
values, fees = enrollment_stats(universities)
print(f'Total students: {sum(values)}')
print(f'Total tuition: $ {sum(fees)}')
print()
print(f'Student mean: {mean(values)}')
print(f'Student median: {median(values)}')
print()
print(f'Tuition mean: {mean(fees)}')
print(f'Tuition median: {median(fees)}')
