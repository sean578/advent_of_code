input_file = 'input.txt'
input_data = open(input_file, 'r')
the_strings = []
for line in input_data:
    the_strings.append(line.strip())
input_data.close()

memory_length = 0
escaped_length = 0
for line in the_strings:
    memory_length = memory_length + len(line)
    print(line)
    print(len(line))
#    print('\":\t\t', line.count('"'))
#    print('\\:\t\t', line.count('\\'))
    # print('length =\t', len(line) + line.count('"') + line.count('\\') + 2)
    escaped_length = escaped_length + len(line) + line.count('"') + line.count('\\') + 2
    
print(memory_length)
print(escaped_length)
print(escaped_length - memory_length)