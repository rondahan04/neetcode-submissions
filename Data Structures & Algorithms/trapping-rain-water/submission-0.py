class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total_water = 0

        left_wall = 0
        for i in range(1, n):
            if height[i] >= height[left_wall]:
                for j in range(left_wall + 1, i):
                    total_water += height[left_wall] - height[j]
                left_wall = i
        right_wall = n - 1
        for i in range(n - 2, left_wall - 1, -1):
            if height[i] >= height[right_wall]:
                for j in range(i + 1, right_wall):
                    total_water += height[right_wall] - height[j]
                right_wall = i
        return total_water