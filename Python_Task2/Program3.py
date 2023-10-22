def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Input array


n = int(input("Enter size of array: "))
arr=[]
for i in range(n):
    a= int(input())
    arr.append(a)

# Perform selection sort
selection_sort(arr)

# Print the sorted array
print("Sorted Array:", arr)

if len(arr) > 1:
    print("Second largest element of the array is: ", arr[1])
else:
    print("The array is too short to have a second element.")
