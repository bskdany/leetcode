from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:  
    for number_index in range(0,len(nums)):
        next_index = number_index+1
        number_to_find = target - nums[number_index] 
        if(number_to_find in nums[next_index:]):
            return [number_index,nums.index(number_to_find,next_index)]

print(twoSum([3,2,4], 6))