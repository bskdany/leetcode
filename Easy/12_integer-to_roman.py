from typing import *

class Solution:
    def romanToInt(self, s: str) -> int:
        my_dict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        number = 0
        previous_val = 0
        t = s[::-1]
        for letter in t:
            int_letter = my_dict[letter]
            if(int_letter<previous_val):
                number -= int_letter
            else:
                number += int_letter
                previous_val = int_letter
        return number

S1 = Solution
print(S1.romanToInt(S1, "XVIIV"))