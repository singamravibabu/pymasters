# delete items from a dictionary
num_to_text = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five",
               6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten"}

# del - to an item using its key form a dictionary
del num_to_text[10]
print(num_to_text)

# pop() - deletes item for a key by returning its value then deletes it
# pop(key[, default_value])
output = num_to_text.pop(9)
print(output)
print(num_to_text)

# clear() - it deletes all items from a dictionary
num_to_text.clear()
print(num_to_text)