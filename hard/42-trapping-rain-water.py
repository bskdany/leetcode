class Solution1: #slowest
    def trap(self, height: List[int]) -> int:
      left = 0
      right = len(height) - 1
      max_left = 0
      max_right = 0

      volume = 0

      while left != right:
        volume += max(0, max_left - height[left])
        max_left = max(height[left], max_left)

        volume += max(0, max_right - height[right])
        max_right = max(height[right], max_right)

        if max_left < max_right:
          left+=1
        
        if max_right <= max_left:
          right-=1

      return volume

class Solution2: #faster
    def trap(self, height: List[int]) -> int:
      left = 0
      right = len(height) - 1
      max_left = 0
      max_right = 0

      volume = 0

      while left <= right:
      
        if max_left < max_right:
          max_left = max(height[left], max_left)
          volume += max_left - height[left]
          left+=1
        
        elif max_right <= max_left:
          max_right = max(height[right], max_right)
          volume += max_right - height[right]
          right-=1

      return volume

#fastest
class Solution:
    def trap(self, height: List[int]) -> int:
      left = 0
      right = len(height) - 1
      max_left = 0
      max_right = 0

      volume = 0

      while left <= right:
      
        if max_left < max_right:
          max_left = max(height[left], max_left)
          volume += max_left - height[left]
          left+=1
        
        else:
          max_right = max(height[right], max_right)
          volume += max_right - height[right]
          right-=1

      return volume

