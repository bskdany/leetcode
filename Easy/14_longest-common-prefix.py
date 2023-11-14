from typing import *

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        smallest = strs[0]
        for word in strs[1:]:
            if len(word) < len(smallest):
                smallest = word

        prefix = ""
        strs.remove(smallest)
        prefix_len = 0
        for letter in smallest:
            for word in strs:
                if(word[prefix_len]!=letter):
                    return prefix
            prefix += letter
            prefix_len+=1
        return prefix
            

S1 = Solution
print(S1.longestCommonPrefix(S1, ["1234", "12324567", "1236578"]))