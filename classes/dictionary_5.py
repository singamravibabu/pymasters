# When we use unspecified key then dictionary returns key error
num_to_text = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five",
               6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten"}

text_to_num = {"one":1, "two":2, "three":3, "four":4, "five":5,
               "six":6, "seven":7, "eight":8, "nine":9, "ten":10}

num_to_text[12]
text_to_num["eleven"]