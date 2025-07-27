def search_in_rotated_array(nums, target, start, end):
    if start == end:
        if nums[start] == target:
            return start
    if end - start == 1:
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
    mid = (start + end)//2
    if nums[mid] == target:
        return mid
    if nums[start]<nums[mid]:
            if nums[start]<=target<=nums[mid]:
                return search_in_rotated_array(nums, target, start, mid)
            else:
                return search_in_rotated_array(nums, target, mid, end)
    if nums[mid]<nums[end]:
            if nums[mid]<=target<=nums[end]:
                return search_in_rotated_array(nums, target, mid, end)
            else:
                return search_in_rotated_array(nums, target, start, mid)
    

print(search_in_rotated_array([6,7,1,2,3,4,5], 1, 0, 6)) # 1