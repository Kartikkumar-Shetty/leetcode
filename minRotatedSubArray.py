def findMin(nums):
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        if nums[0]<nums[1]:
            return nums[0]
        else:
            return nums[1]

    mid =  len(nums)//2
    if nums[mid]>nums[len(nums)-1]:
        return findMin(nums[mid:])
    elif nums[0]>nums[mid]:
        return findMin(nums[0:mid+1])
    else:
        return nums[0]
    
print(findMin([6,7,1,2,3,4,5])) # 1
