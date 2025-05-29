def magical_cows(C, N, cows, max_days):

    dp = [ [0] * (C + 1) for _ in range(max_days + 1) ]


    for cow in cows:
        dp[0][cow] += 1


    for day in range(max_days):
        for cow_count in range(1, C + 1):
            count = dp[day][cow_count]
            if count == 0:
                continue
            doubled = cow_count * 2
            if doubled <= C:
                dp[day + 1][doubled] += count
            else:

                dp[day + 1][cow_count] += count * 2


    for day in range(max_days + 1):
        total_farms = sum(dp[day])
        print(f"Day {day}: {total_farms} farms")

C = 2
N = 5
cows = [1, 2, 1, 2, 1]
max_days = 10
magical_cows(C, N, cows, max_days)
