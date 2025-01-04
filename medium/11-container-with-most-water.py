class Solution:
    def maxArea(self, height: List[int]) -> int:
      left = 0
      right = len(height) - 1
      max_vol = 0
      while (left != right):
        max_vol = max(max_vol, (right - left) * min(height[right], height[left]))
        # going to the tallest height out of the next options
        if height[left] < height[right]:
          left += 1
        else:
          right -= 1
      return max_vol

        