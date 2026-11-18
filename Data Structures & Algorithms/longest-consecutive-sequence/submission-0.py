class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        nums_set = set(nums)

        for num in nums_set:
            if (num - 1) not in nums_set:
                current_streak = 1
                while (num + current_streak) in nums_set:
                    current_streak += 1
                result = max(result, current_streak)
        return result
