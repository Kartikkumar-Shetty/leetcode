#wont work in case of zeros
def maxProduct1(a) -> int:
    #approach1: My approach
    
    negs_count = 0
    max_product = 1
    
    for i in range(0, len(a)):
        if a[i] <0:
            negs_count += 1
        max_product *= a[i]
    if negs_count % 2 == 0:
        return max_product
    
    max_subproduct = 1
    current_product = 1
    for i in range(0, len(a)):
        if a[i] < 0:
            prod = max(max_product//(a[i]*current_product), current_product)
            max_subproduct = max(max_subproduct, prod)
            current_product = 1
        else:
            current_product = current_product * a[i]
    return max_subproduct


def maxProduct(nums) -> int:
    if len(nums) == 1:
        return nums[0]
    left_max = nums[0]
    right_max = nums[len(nums)-1]
    i=0
    j = len(nums)-1
    left_curr = nums[0]
    right_curr = nums[len(nums)-1]
    while i < len(nums) or j>0:
        if i<=len(nums)-1:
            if nums[i] == 0:
                left_max = max(left_max, nums[i])
                left_curr = 1
                i=i+1
                continue
            if i>0:
                left_curr = left_curr * nums[i]
            left_max = max(left_max, left_curr)
            i=i+1
            
        if j>=0:
            if nums[j] == 0:
                right_max = max(right_max, nums[j])
                right_curr = 1
                j=j-1
                continue
            if j<len(nums)-1:
                right_curr = right_curr * nums[j]
            right_max = max(right_max, right_curr)
            j=j-1
        
    return max(left_max, right_max)

# print(maxProduct1([2,-2,2,2,3,-1,-50,1,100]))
print(maxProduct([0,0,-3,1]))

#[2,3,-2,4,3,-3,6,-10,70]