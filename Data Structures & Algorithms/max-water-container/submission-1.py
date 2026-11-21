class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        best_container = -1
        while l < r:
            width = r - l
            height = min(heights[l],heights[r])
            container = width * height
            if height == heights[l]:
                l += 1
            else:
                r -= 1
            best_container = max(best_container, container)
        return best_container
