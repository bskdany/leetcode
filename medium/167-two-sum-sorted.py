
class Solution_1:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        slow = len(numbers) - 1

        while (slow > 0):
            temp_target = target - numbers[slow]

            # binary search the number
            min_i = 0
            max_i = slow - 1
            while (max_i - min_i > 1):
                half = (max_i + min_i) // 2
                if numbers[half] == temp_target:
                    return [half+1, slow+1]

                elif (numbers[half] > temp_target):
                    max_i = half-1
                else:
                    min_i = half+1

            if numbers[min_i] == temp_target:
                return [min_i + 1, slow+1]

            elif numbers[max_i] == temp_target:
                return [max_i + 1, slow+1]

            slow -= 1


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while (right > left):
            sum = numbers[left] + numbers[right]
            if (sum == target):
                return [left+1, right+1]
            elif sum > target:
                right -= 1
            else:
                left += 1
