def two_sum(nums, target):
    hashmap = {} #stores

    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i


nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)

'''
Hash map makes lookups and inserts fast (O(1) average time)
'''