# Problema 198 de leetcode

def rob(nums):
    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums[0], nums[1])
    dp = [0] * len(nums)

    for i in range(len(nums)):
        if i == 0 or i == 1:
            dp[i] = nums[i]

        elif i == 2:
            dp[i] = nums[i] + dp[0]

        elif i >= 3:
            dp[i] = nums[i] + max(dp[i-3], dp[i-2])
    
    return max(dp[-1], dp[-2])

print(rob([2,7,9,3,1]))
print(rob([1,2,3,1]))

        