def sub_array_of_size_k(nums,k):
    window_sum = 0
    max_sum = float('-inf')
    window_start = 0

    for window_end in range(len(nums)):
        window_sum += nums[window_end]

        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= nums[window_start]
            window_start += 1

    return max_sum
    


nums = [2, 1, 5, 1, 3, 2]
k = 3
result = sub_array_of_size_k(nums, k)
print(result)