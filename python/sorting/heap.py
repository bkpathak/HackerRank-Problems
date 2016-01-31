import math
def default_compare(a, b):
  if a < b:
    return -1
  elif a > b:
    return 1
  return 0

def sort(array, compare=default_compare):
  heap_size = len(array)
  build_heap(array, heap_size, compare)
  while heap_size > 1:
    heap_size -= 1
    array[0], array[heap_size] = array[heap_size], array[0]
    heapify(array, heap_size, 0, compare)
  return array

def heapify(array, heap_size, i, compare):
  left = i * 2 + 1
  right = i * 2 + 2
  largest = i
  if left < heap_size and compare(array[left], array[largest]) > 0:
    largest = left
  if right < heap_size and compare(array[right], array[largest]) > 0:
    largest = right
  if largest != i:
    array[i], array[largest] = array[largest], array[i]
    heapify(array, heap_size, largest, compare)

def build_heap(array, heap_size, compare):
  for i in range(math.floor(len(array) / 2), -1, -1):
    heapify(array, heap_size, i, compare)

arr = [9,8,7,6,5,4,3,2,1]
sort(arr)
print(arr)
