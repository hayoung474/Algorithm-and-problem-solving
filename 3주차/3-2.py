def merge(left,right):
    ## 연결리스트 처럼 pop(0) 과 append() 를 사용하면
    ## 조금 더 이해하기 쉽게 구현이 가능함.
    ## 인덱스 로 하는 방법보다 더 이해하기 쉬운 것 같기도 하고..
    clist = []
    ## 두 개의 리스트 안에 값이 남아 있는 동안 반복함.
    while left and right:
        ## left 리스트와 right 리스트의 맨 앞 자료의 값을 비교함.
        if left[0] < right[0]:
            clist.append(left.pop(0))
        else:
            clist.append(right.pop(0))
    ## left에 데이터가 아직 남아있다면.
    while left:
        clist.append(left.pop(0))
    ## right에 데이터가 아직 남아있다면.
    while right:
        clist.append(right.pop(0))
    return clist

def mergeSort(templist):
    ## 더이상 쪼개질 리스트가 없다면 . 반환... 
    if len(templist) <= 1:
        return templist
    ## 중간점을 변수에 저장.
    middle = len(templist)//2

    ## 슬라이싱을 이용한 배열 분할
    leftlist = templist[:middle]
    rightlist = templist[middle:]

    ## 재귀 호출을 이용하여 다시 분할
    leftlist = mergeSort(leftlist)
    rightlist = mergeSort(rightlist)
    
    ## 합병 결과를 반환.
    return merge(leftlist,rightlist)

alist = [4, 7, 2, 1, 5, 8, 6, 3, 9]
blist = mergeSort(alist)
print(blist)
