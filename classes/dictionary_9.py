# Avoid key error with dictionary using get() method
# normally errors terminate the code from executing further

text_to_num = {"one":1, "two":2, "three":3, "four":4, "five":5,
               "six":6, "seven":7, "eight":8, "nine":9, "ten":10}

print(text_to_num.get('one'))
print(text_to_num.get('ten'))
print(text_to_num.get('twenty'))
print(text_to_num.get('hundred', "Not a known number"))