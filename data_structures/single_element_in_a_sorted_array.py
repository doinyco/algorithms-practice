# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
# Return the single element that appears only once.

def single_non_duplicate(nums):
    if len(nums) == 1:
        return nums[0]
    
    left = 0
    right = len(nums) - 1
    
    
    mid = (left + right) // 2
    
    if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
        return nums[mid]
        
    if nums[mid] == nums[mid-1] and (mid - 1) % 2 == 1 or nums[mid] == nums[mid + 1] and mid % 2 == 1:
        return single_non_duplicate(nums[:mid])
    else:
        return single_non_duplicate(nums[mid+1:])
    
    
nums = [1,1,2,3,3,4,4,8,8,9,9,10,10,10,10]
print(single_non_duplicate(nums))