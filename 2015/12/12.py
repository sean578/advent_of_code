import json

string = open('input.txt', 'r').readlines()[0]
json_object = json.loads(string)

# json_object = [33, 2]

def look_at_item(json_object):

    if type(json_object) == type(dict()):
        
        # do this sum function for each element
        return sum(map(look_at_item, json_object.values()))
        
    elif type(json_object) == type(list()):
        
        # do this sum function for each element
        return sum(map(look_at_item, json_object))
  
    else:
        
        # do this sum function for the single element
        if type(json_object) == type(0):
            return json_object # an int
        else:
            return 0
        
print(look_at_item(json_object))


# 96196 too high
# 90737 too high
