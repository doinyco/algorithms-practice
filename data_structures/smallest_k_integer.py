# Write a function to find the smallest k integerd in a list/stream. 

def k_smallest(nums):
    smallest = None

    for i in range(len(nums)):
        if smallest == None:
            smallest = nums[i]

        if nums[i] < smallest:
            smallest = nums[i]

    return smallest


nums = [-500, 10, 20, 30, 4, -100, 5, 2, 8, -1, 0]
print(k_smallest(nums))