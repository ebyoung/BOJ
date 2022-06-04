str1 = input()
str2 = input()
dp = [[0] * (len(str2) + 1) for _ in range(len(str1)+1)]

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

lcs = dp[-1][-1]
print(lcs)

if lcs:
    checked = len(str2)
    answer = ''
    for i in range(len(str1), 0, -1):
        for j in range(checked, 0, -1):
            if dp[i][j] == lcs and dp[i-1][j] == dp[i][j-1] == dp[i-1][j-1] == lcs - 1:
                lcs -= 1
                answer = str1[i-1] + answer
                checked = j - 1
                break
    print(answer)
