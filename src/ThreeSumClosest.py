nums = [-1, 2, 1, -4]


def threeSumClosest(self, nums, target):
    result = nums[0] + nums[1] + nums[len(nums) - 1]
    nums.sort()
    for x in range(len(nums)):
        start = x + 1
        end = len(nums) - 1
        while start < end:
            sum = nums[x] + nums[start] + nums[end]
            if sum > target:
                end = end - 1
            else:
                start = start + 1
            if abs(sum - target) < abs(result - target):
                result = sum
    return result

