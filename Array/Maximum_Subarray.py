def max_subarray(nums):
    max_current = max_global = nums[0]

    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])
        max_global = max(max_global, max_current)

    return max_global

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
print(max_subarray(nums))  

'''
Approach Used (Kadane’s Algorithm)
Time Complexity	O(n)
'''