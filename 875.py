"""Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.



Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23


Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109"""
import math
from typing import List


class Solution:

    def calc_hours_needed(self, piles: List[int], k: int) -> int:
        hours_per_pile = [math.ceil(bananas / k) for bananas in piles]
        return sum(hours_per_pile)

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        biggest_pile = max(piles)
        min_k = 1
        max_k = biggest_pile

        while min_k < max_k:
            mid_k = min_k + (max_k - min_k) // 2
            hrs_needed = self.calc_hours_needed(piles, mid_k)
            if hrs_needed > h:
                min_k = mid_k + 1
            elif hrs_needed <= h:
                max_k = mid_k - 1

        return min_k