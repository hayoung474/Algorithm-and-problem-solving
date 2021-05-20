def DPCoinChange(n,d):
    INF = 99999
    C = [INF]*(n+1)
    C[0] = 0

    coin_result = [[0,0,0,0]]

    for j in range(1,n+1):
        mini = 0
        for i in range(0,len(d)): # 동전 순회 
            if (d[i]<=j) and (C[j-d[i]]+1 < C[j]):
                C[j]= C[j-d[i]]+1 
                mini = i
        temp = [0,0,0,0] # 현재 동전을 추가한 빈 리스트 추가. 여기서 말하는 현재 동전은 d[i] 임. 
        temp[mini]+=1 # 현재 사용한 동전 갯수 추가
        coin_result.append([x+y for x,y in zip(temp,coin_result[j-d[mini]])]) # 현재 사용한 동전 개수와, j-d[i] 에서 사용한 동전 개수를 합침. 

    for i in range(len(d)):
        print(d[i],"원",coin_result[-1][i],"개 사용") # 리스트의 제일 마지막 요소 접근 
    return C[n]


if __name__ == "__main__":
    n = 25
    d = [16,10,5,1]
    print(DPCoinChange(n,d))