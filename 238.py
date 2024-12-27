class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      n = len(nums)
      product = [1] * n

      pre = 1
      for i in range(n):
        product[i] = pre
        pre *= nums[i]

      post = 1
      for i in range(n-1, -1, -1):
        product[i] = product[i] * post
        post *= nums[i]

      return product