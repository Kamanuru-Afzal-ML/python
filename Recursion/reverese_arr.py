#REVERSING ARRAY THROUGH NORMAL FUNCTIONS
def reverseIt(arr):
    last=len(arr)-1
    for i in range(len(arr)//2):
        arr[i],arr[last]=arr[last],arr[i]
        last-=1
    print(arr)
lis=[1,2,3,4,5,6,7,8,9,10,11,12]
reverseIt(lis)
print("Recursive reverse")
# def swap(arr,s,e):
#     arr[s],arr[e]=arr[e],arr[s]
def reverseByRec(arr,start,end):
    if(start>end):
        print(arr)
        return arr
    else:
        arr[start],arr[end]=arr[end],arr[start]
        reverseByRec(arr,start+1,end-1)
lis1=[1,2,3,4,5,6,7,8,9,10,11,12]
res=reverseByRec(lis1,0,len(lis1)-1)

#By using single parameter

def reverBysingle(arr):
    last=len(arr)-1
    for i in range(0,len(arr)//2):
        arr[i],arr[last-i]=arr[last-i],arr[i]
    print("By using single parameter:",arr)
lis2=[1,2,3,4,5,6,7,8,9,10,11,12]
reverBysingle(lis2)

def reverseBYsingleRec(i):
    if(i>=len(lis2)//2):
        print(lis2)
        return lis2
    lis2[i],lis2[len(lis2)-i-1]=lis2[len(lis2)-i-1],lis2[i]
    reverseBYsingleRec(i+1)
print(reverseBYsingleRec(0))