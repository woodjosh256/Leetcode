from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0

        left = 0
        right = len(height) - 1
        while left < right - 1:
            if height[left + 1] > height[left]:
                left += 1
            elif height[right - 1] > height[right]:
                right -= 1
            else:
                pool_elev = min(height[left], height[right])
                if height[left] < height[right]:
                    while height[left] <= pool_elev and left < right:
                        volume += pool_elev - height[left]
                        left += 1
                else:
                    while height[right] <= pool_elev and right > left:
                        volume += pool_elev - height[right]
                        right -= 1

        return volume
