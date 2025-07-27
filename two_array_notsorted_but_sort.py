from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        end = len(nums)-1
        hash = {}
        for i in range(0, len(nums)):
            if hash.get(nums[i]) is not None:
                hash[nums[i]].append(i)
            else:
                hash[nums[i]] = [i]

        
        nums = self.merge_sort(nums)
        
        i=0
        while True:
            if i>end:
                break
            if nums[i]+nums[end]>target:
                end = end-1
                continue
            if nums[i]+nums[end]==target:
                if len(hash[nums[i]])==2:
                    return [hash[nums[i]][0], hash[nums[i]][1]]
                else:
                    return [hash[nums[i]][0], hash[nums[end]][0]]
            i = i+1

    def merge_sort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = self.merge_sort(arr[:mid])
        right_half = self.merge_sort(arr[mid:])

        return self.merge(left_half, right_half)

    def merge(self,left: List[int], right: List[int]) -> List[int]:
        sorted_array = []
        left_index = right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                sorted_array.append(left[left_index])
                left_index += 1
            else:
                sorted_array.append(right[right_index])
                right_index += 1

        sorted_array.extend(left[left_index:])
        sorted_array.extend(right[right_index:])

        return sorted_array



print(Solution().twoSum([2,7,11,15], 9))