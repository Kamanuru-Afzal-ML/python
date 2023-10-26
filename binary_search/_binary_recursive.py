def binary_search(arr,low,high,key):
    if(low<=high):
        mid=low+high//2
        if(arr[mid]==key):
            return mid
        if(arr[mid]<=key):
            return binary_search(arr,mid+1,high,key)
        else:
            return binary_search(arr,low,mid-1,key)
    else:
        return -1
        
    # if(low>=high):
    #     return -1
    # mid=low+((high-low)//2)
    # print(mid)
    # if(key==arr[mid]):
    #     return mid
    # if(key<=arr[mid]):
    #     return binary_search(arr[mid],low,mid-1,key)
    # if(key>=arr[mid]):
    #     return binary_search(arr[mid],mid+1,high,key)
l=[x for x in range(1,21)]
start=0
end=len(l)-1
target=int(input("Enter target:"))
print(binary_search(l,start,end,target))
