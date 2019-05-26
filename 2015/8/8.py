input_file = 'input.txt'
input_data = open(input_file, 'r')
the_strings = []
for line in input_data:
    the_strings.append(line.strip())
input_data.close()

code_length = 0
for string in the_strings:
    code_length = code_length + len(string)

print('code_length', code_length)

memory_length = 0
for string in the_strings:
    exec('a_string =' + string)
    memory_length = memory_length + len(a_string)
    
print('memory_length = \t', memory_length)

print('difference =\t', code_length - memory_length)