def findElement(arr,low,high,target):
    while(low<=high):
        mid=low+high//2
        if(arr[mid]==target):
            return mid
        #Left sorted array
        if(arr[low]<=arr[mid]):
            if(arr[low]<=target) and (arr[mid]>=target):
                high=mid-1
            else:
                low=mid+1
        #Right sorted array
        else:
            if(arr[mid]<=target) and (arr[high]>=target):
                low=mid+1
            else:
                high=mid-1
    return -1
lis=[7,8,9,1,2,3,4,5,6,7,8,9]
print(findElement(lis,0,len(lis)-1,1))








# def search_in_rotated_array(arr, target):
#     left, right = 0, len(arr) - 1

#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid

#         if arr[left] <= arr[mid]:
#             if arr[left] <= target < arr[mid]:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         else:
#             if arr[mid] < target <= arr[right]:
#                 left = mid + 1
#             else:
#                 right = mid - 1

#     return -1  # Element not found

# # Example usage
# rotated_array = [4, 5, 6, 7, 0, 1, 2]
# target = 0
# result = search_in_rotated_array(rotated_array, target)
# if result != -1:
#     print(f"Element {target} found at index {result}")
# else:
#     print(f"Element {target} not found in the array.")
