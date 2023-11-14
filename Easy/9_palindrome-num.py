class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_num = str(x)
        while(len(str_num)!=0):
            if(str_num[0] != str_num[-1]):
                return False
            str_num = str_num[1:-1]
        return True
        

S1 = Solution
print(S1.isPalindrome(S1,1234321))