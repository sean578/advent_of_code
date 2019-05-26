filename = 'input.txt'

def read_file_into_memory(filename):
    """Reads the input file into a dictionary.
    Keys: The wires
    Values: The gates
    """
    
    input_data = open(filename, 'r')
    
    input_array = []
    for line in input_data:
        input_array.append(line.strip('\n'))
        
    input_data.close()
    operation_array = []
    output_array = []
    
    for item in input_array:
        operation, output = item.split(' -> ')
        operation_array.append(operation)
        output_array.append(output)
        
    input_dict = dict( zip(output_array, operation_array) )
        
    return input_dict

def calculate(wire, input_dict, results_dict):
    
    gates = ['AND', 'NOT', 'OR', 'RSHIFT', 'LSHIFT']
    
    # look up the expression for the wire in the dict
    expression = input_dict[wire].split(' ')
    
    # print(wire)
    
    for index, item in enumerate(expression):
        # print('item:\t', item)
        if not item.isdigit():                  # if not a number
            if item not in gates:               # if not a gate
                if item in results_dict:
                    expression[index] = results_dict[item]
                else:
                    expression[index] = calculate(item, input_dict, results_dict)     # need to calculate this wire
                
    # at this point should be able to evaluate the expression
    # print('expression after substitution:\t', expression)
    
    
    if len(expression) == 1: # if the expression is just an int, use it
        results_dict[wire] = int(expression[0])
        return results_dict[wire]
    elif expression[-2] == 'AND':					# else calculate
        results_dict[wire] = int(expression[0]) & int(expression[-1])
        return results_dict[wire]
    elif expression[-2] == 'NOT':
        results_dict[wire] = ~int(expression[-1])
        return results_dict[wire]
    elif expression[-2] == 'OR':
        results_dict[wire] = int(expression[0]) | int(expression[-1])
        return results_dict[wire]
    elif expression[-2] == 'RSHIFT':
        results_dict[wire] = int(expression[0]) >> int(expression[-1])
        return results_dict[wire]
    elif expression[-2] == 'LSHIFT':
        results_dict[wire] = int(expression[0]) << int(expression[-1])
        return results_dict[wire]
    else:
        # print('Performing a {}'. format(expression[-2]))
        return 'XX'
    
input_dict = read_file_into_memory(filename)
results_dict = {}

#for key, value in input_dict.items():
#    print('{}:\t{}'.format(key, value))
    
print(calculate('a', input_dict, results_dict))
    


