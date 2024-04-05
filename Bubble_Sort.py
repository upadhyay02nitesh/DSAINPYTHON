def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr 
arr=[3,2,5,4,1]
print(bubble(arr))