import numpy as np
import random
import time

def timeit(func):
    def wrapper(*arg, **kw):
        '''source: http://www.daniweb.com/code/snippet368.html'''
        t1 = time.time()
        res = func(*arg, **kw)
        t2 = time.time()
        return (t2 - t1), func.__name__
    return wrapper

@timeit
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
    return arr

@timeit
def selectionSort(arr):
    """
    docstring
    """
    min_idx = 0
    for i in range(len(arr)-1):
        minimum = arr[i]
        for j in range(i, len(arr),1):
            if arr[j] < minimum:
                minimum = arr[j]
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr

@timeit
def insertSort(arr):
    """
    docstring
    """
    for i in range(1, len(arr)):
        j = i
        while j > 0:
            if arr[j] < arr[j-1]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            j-=1
    return arr

@timeit
def shellSort(arr):
    """
    docstring
    """
    h = 1
    while 3*h <  len(arr):
        h = 3*h + 1
    while h>=1:
        for i in range(h, len(arr)):
            j = i
            while j>0:
                if arr[j] < arr[j-h]:
                    arr[j-h], arr[j] = arr[j], arr[j-h]
                j-=h
        h//=3
    return arr

class MergeSort:
    '''
    Bottom to Up
    '''
    def __init__(self,arr):
        self.N = len(arr)
        self.aux = []* self.N
        self.arr = arr
    def merge(self,arr,low, mid,high):
        '''
        merge two sorted arr
        '''
        i = mid - low +1
        j = high - mid
        self.aux[low:high] = self.arr[low:high]
        for k in range(low,high,1):
            if i >= mid:
                self.arr[k] = self.aux[j]
                j+=1
            elif j >=high:
                self.arr[k] = self.aux[i]
                i+=1
            elif self.aux[i] < self.aux[j]:
                self.arr[k] = self.aux[i]
                i+=1
            else:
                self.arr[k] = self.aux[j]
                j+=1
        return
    def bottom_up_merge_sort(self):
        sz = 1 # the size of sub-array, then the whole length to merge() is sz * 2
        while sz<self.N:
            for lo in range(0, self.N-sz+1, sz+sz):
                self.merge(self.arr, lo, lo+sz, min(lo + sz + sz, self.N)) # min 是为了不越界，如果最后部分不够 2 * sz就只取到最后一个元素
            sz *= 2
        return self.arr

    def up_bottom_merge_sort(self, arr,lo, hi):
        if lo < hi:
            mid = (lo +hi-1)//2
            self.up_bottom_merge_sort(self.arr, lo, mid)
            self.up_bottom_merge_sort(self.arr, mid+1, hi)
            self.merge(self.arr, lo, mid, hi)
        return self.arr
        
def partition(arr,low,high):
    i = low+1
    j = high
    pivot = arr[low]
    while True:
        while i<=high and arr[i] <= pivot:
            i+=1
        while j>=low+1 and arr[j] >= pivot:
            j-=1
        if i<=j:
            arr[i],arr[j] = arr[j], arr[i]
        else:
            break
    
    arr[low], arr[j] = arr[j], arr[low]
    return j
    
def quickSort(arr,low,high):
    if low < high:
        j = partition(arr,low,high)
        quickSort(arr, low, j-1)
        quickSort(arr, j+1, high)

if __name__ == "__main__":
    arr = np.random.randint(1,20,10)
    print(arr)
    # print(selectionSort(arr))
    # print(bubbleSort(arr))
    # print(insertSort(arr))
    # print(shellSort(arr))
    # solution = MergeSort(arr)
    # print(solution.up_bottom_merge_sort(arr, 0, len(arr)))
    quickSort(arr,0,len(arr)-1)
    print(arr)
