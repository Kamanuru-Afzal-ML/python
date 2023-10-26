# def frist_occurrences(arr,low,high,key):
#     ans=-1
#     while(low<=high):
#         mid=high+low//2
#         if(arr[mid]>=key):
#             ans=mid
#             high=mid-1
#         else:
#             low=mid+1
#     return ans
# def last_occurrences(arr,low,high,key):
#     ans=-1
#     while(low<=high):
#         mid=high+low//2
#         if(arr[mid]>key):
#             ans=mid
#             high=mid-1
#         else:
#             low=mid+1
#     return ans
# def frist_occurrences_rec(arr,low,high,key,ans):
#     if(low>=high):
#         return -1
#     mid=high+low//2
#     if(arr[mid]==key):
#         return ans
#     if(arr[mid]>=key):
#         ans=mid
#         return frist_occurrences_rec(arr,low,mid-1,key,ans)
#     else:
#         return frist_occurrences_rec(arr,mid+1,high,key,ans)
    

# def last_occurrences_rec(arr,low,high,key,ans):
#     if(low>=high):
#         return -1
#     mid=high+low//2
#     if(arr[mid]==key):
#         return ans
#     if(arr[mid]>key):
#         ans=mid
#         return frist_occurrences_rec(arr,low,mid-1,key,ans)
#     else:
#         return frist_occurrences_rec(arr,mid+1,high,key,ans)
def first_last_occurence(arr,low,high,key,first,last):
    if(low==high):
        print(first,last)
    if(arr[low]==key and first==-1):
        first=low
        last=low
    if(arr[low]==key):
        last=low
    first_last_occurence(arr,low+1,high,key,first,last)
l=[1,2,4,5,5,6,7,8]
print(first_last_occurence(l,0,len(l)-1,5,-1,-1))
# f=frist_occurrences_rec(l,0,len(l)-1,5,-1)
# la=last_occurrences_rec(l,0,len(l)-1,5,-1)
# # s=last_occurrences(l,0,len(l)-1,2,-1)
# print(f,la)