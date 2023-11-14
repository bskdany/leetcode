from types import *

class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s)==0 or len(s)%2==1):
            return False

        complements = {
            ")":"(",
            "}":"{",
            "]":"[",
        }

        stack = [s[0]]
        for letter in s[1:]:
            if(len(stack)!=0 and letter in complements and complements[letter]==stack[-1]):
                stack.pop()
            else:
                stack.append(letter)

        if(len(stack)>0):
            return False
        return True
            
S1 = Solution
print(S1.isValid(S1, "{}{}{}{}[()()]"))