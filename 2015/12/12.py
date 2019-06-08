import json

string = open('input.txt', 'r').readlines()[0]
json_object = json.loads(string)

def sum_fn(json_object):

    if type(json_object) == type(dict()):
        
        if "red" in json_object.values():
            return 0
        else:
            # do this sum function for each element
            return sum(map(sum_fn, json_object.values()))
        
    elif type(json_object) == type(list()):
        
        # do this sum function for each element
        return sum(map(sum_fn, json_object))
  
    else:
        
        # do this sum function for the single element
        if type(json_object) == type(0):
            return json_object # an int
        else:
            return 0
        
print(sum_fn(json_object))

# 96196 too high
# 90737 too high
