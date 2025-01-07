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


class Solution: # this one is faster
    def isValid(self, s: str) -> bool:
      stack = []
      complement = {
        ")": "(",
        "]": "[",
        "}": "{"
      }

      for string in s:
        if string in complement.keys():
          if not stack or stack.pop() != complement[string]:
            return False
        else:
          stack.append(string)

      if stack:
        return False
      return True
        