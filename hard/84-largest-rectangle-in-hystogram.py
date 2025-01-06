class Solution: # times out but works on small inputs, problem with loop logic
    def largestRectangleArea(self, heights: List[int]) -> int:
      stack = []
      max_area = 0

      for i in range(len(heights)):
        height = heights[i]

        while stack and height < stack[-1][0] if stack else 0:
          val = stack.pop()
          max_area = max((i - val[1])*val[0], max_area)

        for j in range((stack[-1][0] if stack else 0) + 1, height + 1):
          stack.append([j,i])

      while stack:
        val = stack.pop()
        max_area = max((i - val[1] + 1)*val[0], max_area)
      
      return max_area


class Solution:  # works and beats 15% lol
    def largestRectangleArea(self, heights: List[int]) -> int:
      stack = []
      max_area = 0

      for i in range(len(heights)):
        height = heights[i]
        
        val = [0,i]
        while stack and height < stack[-1][0]:
          val = stack.pop()
          max_area = max((i - val[1])*val[0], max_area)

        if stack:
          if stack[-1] != height:
            stack.append([height,val[1]])
        else:
          stack.append([height,val[1]])
        
        # print(stack)
        

      while stack:
        val = stack.pop()
        max_area = max((i - val[1] + 1)*val[0], max_area)
      
      return max_area


class Solution: # beats 40% not bad
    def largestRectangleArea(self, heights: List[int]) -> int:
      stack = []
      max_area = 0

      for i in range(len(heights)):
        height = heights[i]
        
        longest = i
        while stack and height < stack[-1][0]:
          val = stack.pop()
          max_area = max((i - val[1])*val[0], max_area)
          longest = val[1]

        stack.append([height,longest])
        
      for val in stack:
        max_area = max((i - val[1] + 1)*val[0], max_area)
      
      return max_area