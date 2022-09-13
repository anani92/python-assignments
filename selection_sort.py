def selection_sort(array):
  for i in range(len(array)):
    for idx in range(len(array)-i-1):
      if array[idx] > array[idx + 1]:
        array[idx], array[idx + 1] = array[idx + 1], array[idx]

nums = [5,33,2,1,4]
selection_sort(nums)
print(nums)

