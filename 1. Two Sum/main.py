def two_sum(nums: list, target: int) -> list:
    for i in range(len(nums)):
        if target - nums[i] in nums[i+1::]:
            second_number = target - nums[i]
            return [i, nums[i+1::].index(second_number) + i + 1]


print(two_sum([2, 7, 8], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))