def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr

user_input=input("enter the numbers:")
arr=list(map(int,user_input.strip().split()))

sorted_array=selection_sort(arr)

print(sorted_array)
