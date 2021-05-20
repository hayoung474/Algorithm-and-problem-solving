def Knapsack(C, w, v):
    K = [[0 for col in range(C+1)] for row in range(len(w)+1)]
    n = len(w)

    for i in range(1, n+1):
        for j in range(1, C+1):
            if(w[i-1] > j):
                K[i][j] = K[i-1][j]
            else :
                K[i][j] = max(K[i-1][j], (K[i-1][j-w[i-1]] + v[i-1]))

    return K[n][C]

if __name__ == '__main__':
    w = [5, 4, 6, 3]
    v = [10, 40, 30, 50]
    C = 10
    print(Knapsack(C, w, v))