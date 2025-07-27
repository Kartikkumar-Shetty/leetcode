def contains_duplicate(nums):
        dnums = {}
        for i in range(0, len(nums)):
                if nums[i] not in dnums:
                    dnums[nums[i]] = 1
                else:
                    return True
        return False
    
print(contains_duplicate([1,2,3,4,5,1]))