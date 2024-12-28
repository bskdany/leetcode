class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      unique = dict()
      distance = 0

      for num in nums:
        if num not in unique.keys():
          unique[num] = unique.get(num-1, 0) + unique.get(num+1, 0) + 1
          
          if num-1 in unique:
            unique[num - unique[num-1]] = unique[num]
          
          if num+1 in unique:
            unique[num + unique[num+1]] = unique[num]
            
          distance = max(distance, unique[num])

      return distance
      
