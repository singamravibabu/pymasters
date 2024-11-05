text_to_num = {"one":1, "two":2, "three":3, "four":4, "five":5,
               "six":6, "seven":7, "eight":8, "nine":9, "ten":10}

# loop through keys using for statement
for key in text_to_num:
    print(key, end=" ")

print()   
# loop through keys using keys() method
for key in text_to_num.keys():
    print(key, end=" ")
    
print()
# loop through values using values() method
for vl in text_to_num.values():
    print(vl, end=" ")
    
print()
# loop through items in a dictionary using items() method
for item in text_to_num.items():
    print(item)