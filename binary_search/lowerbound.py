def binary(lis,n,low,high):
    while low<=high:
        mid=(low+high)//2
        if(lis[mid]>=n):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
arr=[1,2,4,4,4,5]
key=int(input("Enter the number:"))
l=0
h=len(arr)-1
print(binary(arr,key,l,h))