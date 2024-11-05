text_to_num = {"one":1, "two":2, "three":3, "four":4, "five":5,
               "six":6, "seven":7, "eight":8, "nine":9, "ten":10}

# list() function to convert an object to a list
keys_list = list(text_to_num.keys())
print(keys_list)
values_list = list(text_to_num.values())
print(values_list)

# tuple() functions converts an object to uple
values_tuple = tuple(text_to_num.values())
print(values_tuple)