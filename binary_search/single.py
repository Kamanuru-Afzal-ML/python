def single(arr):
    n=len(arr)-1
    low=1
    high=n-2
    if(arr[0]!=arr[1]):
        return arr[0]
    if(arr[n]!=arr[n-1]):
        return arr[n]
    while(low<=high):
        mid=low+high//2
        if(arr[mid]!=arr[mid-1] | arr[mid]!=arr[mid+1]):
            return arr[mid]
        if(mid%2==0 & arr[mid+1]==arr[mid]) | (mid%2==1 & arr[mid-1]==arr[mid]):
            low=mid+1
        else:
            high=mid-1
    return -1
lis=[1,1,2,2,3,3,4,4,5,6,6,7,7,8,8]
res=single(lis)
print(res)