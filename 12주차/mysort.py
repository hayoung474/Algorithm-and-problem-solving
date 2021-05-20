import copy
import random

def bubble_sort(l):
    arr = copy.deepcopy(l)
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
    
def selection_sort(l):
    arr = copy.deepcopy(l)
    n = len(arr)
    for i in range(0,n-1,1):
        minimum = i
        for j in range(i+1,n,1):
            if arr[j] < arr[minimum]:
                minimum=j
        arr[i],arr[minimum] = arr[minimum],arr[i]
    return arr

def insertion_sort(l):
    arr = copy.deepcopy(l)
    n = len(arr)
    for i in range(1,len(arr)):
        current_element = arr[i]
        j = i-1
        while (j>=0) and (arr[j] > current_element):
            arr[j+1]=arr[j]
            j = j-1
        arr[j+1] = current_element
    return arr


def shell_sort(l):
    arr = copy.deepcopy(l)
    n = len(arr)
    h = n // 2
    while h > 0:
        for i in range(h,len(arr)):
            current_element = arr[i]
            j = i
            while (j>=h) and (arr[j-h] > current_element):
                arr[j]=arr[j-h]
                j = j-h
            arr[j] = current_element
        h //= 2
    return arr
    

def heap_sort(l):
    arr = copy.deepcopy(l)
    # max heap 
    def heapify(arr,index,heap_size):
        largest=index
        left_child = 2 * index + 1
        right_child = 2*index + 2
        
        if left_child < heap_size and arr[left_child] > arr[largest]:
            largest = left_child
        if right_child < heap_size and arr[right_child] > arr[largest]:
            largest = right_child
        if largest != index:
            arr[largest],arr[index] = arr[index],arr[largest]
            heapify(arr,largest,heap_size)

    n = len(arr)
    # max heap 만들기
    for i in range(n//2-1,-1,-1):
        heapify(arr,i,n)

    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heapify(arr,0,i)

    return arr



def radix_sort(l):
    arr = copy.deepcopy(l)
    
    def getrdx(arr,modulus):
        maxi = 0
        for val in arr:
            digit=0
            while val>0:
                digit+=1
                val //=modulus
            if digit>maxi:
                maxi = digit
        return maxi

    radix,modulus,div = 10,10,1

    nordx = getrdx(arr,10)

    for i in range(nordx):
        buckets = [[] for i in range(radix)]
        for value in arr:
            buckets[(value % modulus)//div].append(value)
        modulus,div = modulus*10,div*10
        arr=[]

        for x in buckets:
            arr.extend(x)
        
    return arr

# 정렬 여부를 체크하는 함수
def is_sorted(arr,sorted_arr):
    return (sorted(arr) == sorted_arr)


l = [random.randint(0,100000) for r in range(5000)]

bubble_sort_result = bubble_sort(l)
print(is_sorted(l,bubble_sort_result))
selection_sort_result = selection_sort(l)
print(is_sorted(l,selection_sort_result))
insertion_sort_result = insertion_sort(l)
print(is_sorted(l,insertion_sort_result))
shell_sort_result = shell_sort(l)
print(is_sorted(l,shell_sort_result))
heap_sort_result = heap_sort(l)
print(is_sorted(l,heap_sort_result))
radix_sort_result= radix_sort(l)
print(is_sorted(l,radix_sort_result))