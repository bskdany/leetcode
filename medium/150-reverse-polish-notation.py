class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
      stack = []

      for token in tokens:
        match token:
          case "+":
            stack[-2] += stack[-1]
            stack.pop()

          case "-":
            stack[-2] -= stack[-1]
            stack.pop()

          case "/":
            stack[-2] = int(stack[-2]/stack[-1])
            stack.pop()

          case "*":
            stack[-2] *= stack[-1]
            stack.pop()
          
          case _:
            stack.append(int(token))        

      return stack[-1]