def SelectionSort(A):
    n = len(A)
    for i in range(0,n-1,1):
        minimum = i
        for j in range(i+1,n,1):
            if A[j] < A[minimum]:
                minimum=j
        A[i],A[minimum] = A[minimum],A[i]
    return A


if __name__ == "__main__":
    A = [5, 8, 1, 2, 0, 6, 9, 3, 7, 4]
    print(SelectionSort(A))

    