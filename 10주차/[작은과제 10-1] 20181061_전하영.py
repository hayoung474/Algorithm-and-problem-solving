def EditDistance(t,s):

    n = len(t)
    m = len(s)

    # 배열 초기화, 입실론 포함해야함.
    E = [[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(1,n+1):
        E[0][i] = i
    for j in range(1,m+1):
        E[j][0] = j


    for i in range(1,m+1):
        for j in range(1,n+1):
            a=0
            if(t[j-1] != s[i-1]):
                a=1
            E[i][j] = min([(E[i][j-1]+1),E[i-1][j]+1,E[i-1][j-1]+a])
            
    return E,E[m][n]

def Print(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print("\n")
if __name__ == "__main__":
    E, answer = EditDistance("adelphia","daphnia")
    print("최소편집거리: ",answer)
    Print(E)
