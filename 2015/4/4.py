import hashlib

# Find MD5 hashes that start with 5 zeros
# Add a number to the input, that will do this.
# Find the lowest number.

input_data = b'bgvyzdsv'
# a_number = b'00000'

i=0
found = False
while found == False:
    
    a_number_string = str(i)
    a_number_bytes = bytes(a_number_string, 'utf-8')
    to_hash = input_data + a_number_bytes
    
    if hashlib.md5(to_hash).hexdigest().startswith('000000'):
            print(i)
            found = True
    
    i = i + 1
            

        


