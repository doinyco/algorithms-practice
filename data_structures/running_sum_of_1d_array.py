# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4]


def sum_numbers(array_num):
    total_sum = [array_num[0]]
    
    for i in range(1, len(array_num)):
        summ = total_sum[i - 1] + array_num[i]
        total_sum.append(summ)
    
    return total_sum

array_num = [1,2,3,4]
print(sum_numbers(array_num))