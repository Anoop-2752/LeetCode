def two_sum(nums, target):
    hashmap = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i

nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)