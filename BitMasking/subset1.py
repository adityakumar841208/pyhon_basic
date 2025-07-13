nums = [1, 2, 3]
n = len(nums)

for mask in range(1 << n):  # 2^n = 8 → mask from 0 to 7
    subset = []
    for i in range(n): # 0,1,2
        if (mask >> i) & 1:
            subset.append(nums[i])
    print(subset)