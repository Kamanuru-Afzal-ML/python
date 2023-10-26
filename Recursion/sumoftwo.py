# def computeTwo(lis,store,target=2):
#     if len(lis)==0:
#         if(sum(store)==target):
#             print(store)
#             return
#     computeTwo(lis[1:],store+[lis[0]],target)
#     computeTwo(lis[1:],store,target)


# def computeTwo(arr,subsequence,index,target):
#     if(index==len(arr)):
#         if(sum(subsequence)==target):
#             print(subsequence)
#             return
#     computeTwo(arr,subsequence+[arr[index]],index+1,target)
#     computeTwo(arr,subsequence,index+1,target)

# def computeTwo(arr,target):
#     def helper_fun(subsequence,index):
#         if index==len(arr):
#             if(sum(subsequence)==target):
#                 print(subsequence)
#                 return
#         helper_fun(subsequence+[arr[index]],index+1)
#         helper_fun(subsequence,index+1)
#     helper_fun([],0)
# li=[1,2,1]
# empty=[]
# computeTwo(li,2)


# def find_subsequences_with_sum(arr, target_sum):
#     def find_subsequences_helper(subseq, index):
#         if index == len(arr):
#             if sum(subseq) == target_sum:
#                 subsequences.append(subseq)
#             return
#         find_subsequences_helper(subseq + [arr[index]], index + 1)
#         find_subsequences_helper(subseq, index + 1)

#     subsequences = []
#     find_subsequences_helper([], 0)
#     return subsequences

# # Example usage
# arr = [1, 2, 3, 4, 5]
# target_sum = 7
# result = find_subsequences_with_sum(arr, target_sum)
# print(result)

# def find_subsequences_with_sum(arr, target_sum,subseq,index):
#     # print("entered")
#     if index == len(arr):
#         if sum(subseq) == target_sum:
#             print(subseq)
#         return
#     find_subsequences_with_sum(arr,target_sum,subseq + [arr[index]], index + 1)
#     find_subsequences_with_sum(arr,target_sum,subseq, index + 1)
# Example usage
def find_subsequences_with_sum(arr, target_sum,subseq):
    if(len(arr)==0):
        if(sum(subseq)==target_sum):
            print(subseq)
        return
    find_subsequences_with_sum(arr[1:],target_sum,subseq+[arr[0]])
    find_subsequences_with_sum(arr[1:],target_sum,subseq)
arr = [3,1,2]
target_sum = 2
result = find_subsequences_with_sum(arr, target_sum,[])
print(result)