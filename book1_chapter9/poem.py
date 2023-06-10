with open('poem.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    text = input_file.readline()
    while text != '':
        output_file.write(text)
        text = input_file.readline()

with open('output.txt', 'a') as output_file:
    output_file.write('\nzalupka')
