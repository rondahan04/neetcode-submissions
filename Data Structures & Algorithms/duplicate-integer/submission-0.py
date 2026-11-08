class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups_map = {}
        for num in nums:
            if num in dups_map:
                return True
            dups_map[num] = num
        return False
        