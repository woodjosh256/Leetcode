class Solution:

    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            width = right - left
            height = min(heights[right], heights[left])
            volume = width * height
            max_vol = max(max_vol, volume)
            if heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
        return max_vol
