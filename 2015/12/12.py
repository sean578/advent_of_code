import re

string = open('input.txt', 'r').readlines()[0]
print(string, '\n\n\n\n')

all_the_numbers = sum(list(map(int, re.findall(r'-?\d+', string))))
print('all the numbers = ', all_the_numbers)

# red_bits = re.findall(r'\{[^[\}\[]*\"red\"[^\}]*\}', string)
red_bits = re.findall(r'\{[^\}]*\:\"red\"[^\}]*\}', string)

numbers_with_red = 0
for string in red_bits:
    print(string)
    numbers_with_red = numbers_with_red + sum(list(map(int, re.findall(r'-?\d+', string))))

print('numbers with red', numbers_with_red)
print('good numbers = ', all_the_numbers - numbers_with_red)

# 96196 too high
# 90737 too high
