from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        end = len(numbers)-1
        i=0
        while True:
            if i>end:
                break
            if numbers[i]+numbers[end]>target:
                end = end-1
                continue
            if numbers[i]+numbers[end]==target:
                return [i, end]
            i = i+1