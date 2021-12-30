"""
循环不变式 就是 : A[0, j-1]
"""
from random_array import random

def insert_sort(arr):
  if len(arr) < 2:
    raise Exception("array is too short to sort")
  for j in range(1, len(arr)):
    pivot = arr[j]
    i = j - 1
    while i >= 0 and arr[i] > pivot:
      arr[i+1] = arr[i]
      i -= 1
    arr[i+1] = pivot
  return arr

if __name__ == '__main__':
    arr=random(10)
    print(insert_sort(arr))
    
    