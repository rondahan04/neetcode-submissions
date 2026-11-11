class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            key_check = target - num
            if key_check in num_map:
                return [num_map[key_check], i]
            num_map[num] = i # The key is the number and the value is the index
        