"""[summary]
几个关键点
1. 先处理数组(partition), 再执行递归
2. partition后的最终形态是: 
      a[lo] ~ a[j-1] 都不大于pivot
      a[j+1] ~ a[right] 都不小于pivot
3. 关键是如何 1:把小于等于pivot的都挪到左边 和 2:把pivot放到争取的位置j
4. 用双指针实现3.1, 注意
5. 实现3.2需要最终把a[lo]和a[j]交换,不能和a[i]交换, 因为a[i]最后指向的可能是一个大于pivot的值, 而a[lo]是小于pivot的区域
   如果pivot选取的是a[hi], 那么需要和a[i]交换


Returns:
    [type]: [description]
"""
from random_array import random
import numpy as np

def swap(arr, i, j):
  arr[i], arr[j] = arr[j], arr[i]

def partition(arr, left, right):
  pivot = arr[left]
  i = left+1
  j = right
  while True:
    while i <= right and arr[i] <= pivot:
      i+=1
    while j > left and pivot <= arr[j]:
      j-=1
    if i<=j:
      swap(arr, i, j)
    else:
      break
  swap(arr, left, j)
  return j
    
      

def quickSort(arr, left, right):
  if left < right:
    j = partition(arr, left, right)
    quickSort(arr, left, j-1)
    quickSort(arr, j+1, right)


if __name__ == '__main__':
    arr=random(10)
    print(arr)
    quickSort(arr, 0, len(arr)-1)
    print(arr)
    