def selection(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]>arr[j]):
                arr[i],arr[j]=arr[j],arr[i]
    return arr 
arr=[3,2,5,4,1]
print(selection(arr))