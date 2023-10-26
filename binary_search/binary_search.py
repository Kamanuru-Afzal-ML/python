def binary(lis,n,low,high):
    while low<=high:
        mid=(low+high)//2
        if(n<=lis[mid]):
            high=mid-1
        if(n>=lis[mid]):
            low=mid+1
        if(lis[mid]==n):
            return 1
    return -1
arr=[x for x in range(21)]
key=int(input("Enter the number:"))
l=0
h=len(arr)-1
print(binary(arr,key,l,h))
