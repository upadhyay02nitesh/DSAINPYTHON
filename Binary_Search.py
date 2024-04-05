def binary_search(arr,k,low,high):
    while (low<=high):
        mid=(low+high)//2
        if(arr[mid]==k):
            return mid 
        elif arr[mid]>k:
            high=mid-1 
        else:
            low=mid+1 
arr=[4,3,6,7,8,1,2]
arr.sort()
low=0
high=len(arr)
k=8
l=binary_search(arr,k,low,high)
print(k,"is find in the index of =",l)