def Minimal(arr):
    low=0
    high=len(arr) - 1
    mini=-1
    while low < high:
        mid=low+high//2
        if(arr[low] <= arr[mid]):
            mini=min(arr[mid])
            





lis=[7,8,9,1,2,3,4,5,6]
print(Minimal(lis))