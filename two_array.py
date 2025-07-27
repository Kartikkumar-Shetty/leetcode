from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(0, len(nums)):
            if hash.get(nums[i]) is not None:
                hash[nums[i]].append(i)
            else:
                hash[nums[i]] = [i]

        for i in range(0, len(nums)):
            if target-nums[i] == nums[i]:
                if len(hash[nums[i]])==2:
                    return [hash[nums[i]][0], hash[nums[i]][1]]
            else:                
                if hash.get(target-nums[i]) is not None:
                    return [i, hash[target-nums[i]][0]]
            
print(Solution().twoSum([3,3], 6))