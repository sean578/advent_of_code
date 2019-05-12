input_filename = 'input.txt'

# Open the file and get the data:

input_file = open(input_filename, 'r')
input_data = input_file.readlines()
input_file.close()

wrapping_paper_to_buy = 0
ribbon_length_to_buy = 0

for line in input_data:
    the_dimensions = list(map(int, line.rstrip().split('x')))
    surface_area = 2*(the_dimensions[0]*the_dimensions[1]
                    + the_dimensions[1]*the_dimensions[2]
                    + the_dimensions[2]*the_dimensions[0])
    
    the_dimensions.sort()
    extra_paper = the_dimensions[0] * the_dimensions[1]
    wrapping_paper_to_buy = wrapping_paper_to_buy + surface_area + extra_paper
    
    volume = the_dimensions[0] * the_dimensions[1] * the_dimensions[2]
    perimeters = [2*(the_dimensions[0] + the_dimensions[1]),
                  2*(the_dimensions[1] + the_dimensions[2]),
                  2*(the_dimensions[2] + the_dimensions[0])]
    perimeter_min = min(perimeters)
    ribbon_length_to_buy = ribbon_length_to_buy + perimeter_min + volume
    
print('Wrapping paper = {} feet'.format(wrapping_paper_to_buy))
print('Ribbon length = {} feet'.format(ribbon_length_to_buy))
