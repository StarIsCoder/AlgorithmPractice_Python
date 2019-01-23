nums = [0, 1, 0, 3, 12]


def moveZeroes(nums):
    insertpos = 0
    for item in nums:
        if item != 0:
            nums[insertpos] = item
            insertpos += 1

    while insertpos < len(nums):
        nums[insertpos] = 0
        insertpos += 1

moveZeroes(nums)

print(nums)
