nums = [1, 2, 3, 4, 5]

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == 9:
            print([nums[i], nums[j]])
