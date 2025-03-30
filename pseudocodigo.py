def knapsack(w, v, C):
    n = len(w)
    dp = [[0] * (C + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(C + 1):
            if w[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + v[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[n][C]

pesos = [2, 3, 4, 5]
valores = [3, 4, 5, 6]
capacidad = 5
resultado = knapsack(pesos, valores, capacidad)
print(resultado)