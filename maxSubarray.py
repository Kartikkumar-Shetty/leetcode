def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_subarray = []
    max_total = 0
    current_subarray = []
    curr_total = 0
    
    for i in range(0, len(nums)):
        if i == 0:
            current_subarray = [nums[i]]
            curr_total = nums[i]
            max_subarray = [nums[i]]
            max_total = nums[i]
            continue
                
        if len(current_subarray)==1 and current_subarray[0] < 0:
            if nums[i] < current_subarray[0]:
                continue
            else:
                current_subarray = [nums[i]]
                curr_total = nums[i]
                max_subarray = [nums[i]]
                max_total = nums[i]
                continue
                        
        if curr_total + nums[i] <= 0:
            current_subarray = []
            curr_total = 0  
            continue
        if curr_total + nums[i] > 0:
            current_subarray.append(nums[i])
            curr_total = curr_total + nums[i]
            if curr_total > max_total:
                max_total = curr_total
                max_subarray = current_subarray
    print(max_total)

maxSubArray([1,-1,1])
        