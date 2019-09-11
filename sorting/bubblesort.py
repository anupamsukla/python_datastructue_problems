array=[11,5,8,9,7]

def selectionsort(array):
  n = len(array) 
  for i in range(n):
    for j in range(0,n-i-1):
      if array[j]>array[j+1]:
        array[j], array[j+1]=array[j+1],array[j]
    print(array)
  return array

print(selectionsort(array))
