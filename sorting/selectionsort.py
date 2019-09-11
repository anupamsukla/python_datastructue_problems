array=[11,5,8,9,7]

def selectionsort(array):
  for i in range(len(array)):
    min_index=i
    for j in range(i+1,len(array)):
      if array[min_index]>array[j]:
        min_index=j
    print(min_index)
    array[i], array[min_index]=array[min_index],array[i]
    print(array)
  return array

print(selectionsort(array))

'''
output
1
[5, 11, 8, 9, 7]
4
[5, 7, 8, 9, 11]
2
[5, 7, 8, 9, 11]
3
[5, 7, 8, 9, 11]
4
[5, 7, 8, 9, 11]
[5, 7, 8, 9, 11]

'''
