

change = int(input("거스름돈 액수를 입력 >>> "))

def CoinChange(W):
    n500 = n170 = n100 = n50 = n10 = 0
    while W >= 500 :
        W -= 500
        n500 += 1
    while W >= 170 :
        W -= 170
        n170 +=1
    while W >= 100 :
        W -= 100
        n100 +=1
    while W >= 50 :
        W -= 50
        n50 += 1
    while W >= 10 :
        W -= 10
        n10 +=1
    return (n500+n170+n100+n50+n10)

print(CoinChange(change))
