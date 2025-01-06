class MinStack: # two stacks, fast but not that fast
    def __init__(self):
      self.min_arr = []
      self.stack = []
        
    def push(self, val: int) -> None:
      self.stack.append(val)
      if len(self.min_arr) == 0:
        self.min_arr.append(val)
      else:
        self.min_arr.append(min(val, self.min_arr[len(self.min_arr)-1]))

    def pop(self) -> None:
      if len(self.stack) == 0:
        return 

      self.stack.pop()
      self.min_arr.pop()

    def top(self) -> int:
      if len(self.stack) == 0:
        return 0

      return self.stack[len(self.stack)-1]
        
    def getMin(self) -> int:
      if len(self.stack) == 0:
        return 0
      
      return self.min_arr[len(self.min_arr)-1]
        

class MinStack: # one stack, fasster
    def __init__(self):
      self.min = 0
      self.stack = []
        
    def push(self, val: int) -> None:
      if len(self.stack) == 0:
        self.min = val
        self.stack.append(0)
      else:
        self.stack.append(val - self.min)
        if(val < self.min):
          self.min = val

    def pop(self) -> None:
      if len(self.stack) == 0:
        return 

      val = self.stack.pop()
      if val < 0:
        self.min -= val

    def top(self) -> int:
      val = self.stack[len(self.stack)-1]
      if val < 0:
        return self.min
      else:
        return self.min + val
        
    def getMin(self) -> int:
      return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()