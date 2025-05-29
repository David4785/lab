def findTargetSumWays(nums, target):
    total = sum(nums)
    if abs(target) > total or (target + total) % 2:
        return 0
    s = (target + total) // 2
    dp = [0] * (s + 1)
    dp[0] = 1
    for num in nums:
        for i in range(s, num - 1, -1):
            dp[i] += dp[i - num]
    return dp[s]

nums = [2, 3, 1, 1, 2]
target = 3
print(findTargetSumWays(nums, target))