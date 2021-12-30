"""

"""
from random_array import random

def merge_sort(arr, left, right):
  '''
  循环不变量,  [left, right]
  '''
  if left < right:
    mid = left + (right - left) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid+1, right)
    merge(arr, left, mid, right)
  return arr

def merge(arr, left, mid, right):
  '''
  arr[left, mid] is sorted
  arr[mid+1, right] is sorted
  '''
  tmp = list()
  for x in arr[left:right+1]:
    tmp.append(x)
  # tmp [0, right-left+1] = arr [left, right+1]
  i , j = 0, mid-left
  for k in range(left, right+1):
    if i>= (mid-left):
      arr[k] = tmp[j]
      j += 1
    elif j > right:
      arr[k] = tmp[i]
      i += 1
    elif tmp[i] > tmp[j]:
      arr[k] = tmp[j]
      j += 1
    else:
      arr[k] = tmp[i]
      i += 1

    
  
  
if __name__ == '__main__':
    arr=random(7)
    # arr = [2,5,7,8, 3,6,7,9]
    print(arr)
    print(merge_sort(arr, 0, len(arr)-1))
    print(arr)