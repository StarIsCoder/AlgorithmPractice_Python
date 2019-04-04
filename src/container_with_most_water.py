def maxArea(height):
    # use while iteration
    # water = 0
    # l = 0
    # r = len(height) - 1
    # while l < r:
    #     water = max(water, (r - l) * min(height[r], height[l]))
    #     if height[l] < height[r]:
    #         l += 1
    #     else:
    #         r -= 1
    # return water

    # use for iteration
    l = 0
    r = len(height) - 1
    water = 0
    width = len(height) - 1
    for w in range(width, 0, -1):
        if height[l] < height[r]:
            water = max(water, height[l] * w)
            l = l + 1
        else:
            water = max(water, height[r] * w)
            r = r - 1
    return water


input = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(input))
