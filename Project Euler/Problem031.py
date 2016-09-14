target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [0 for x in range(200 + 1)]
ways[0] = 1

for i in range(len(coins)):
	j = coins[i]
	while j <= target:
		ways[j] += ways[j - coins[i]]
		j += 1

print(ways[-1])
