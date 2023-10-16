def palindrome(palin,start):
    if(start>(len(palin)-1)//2): 
        print("true")
        return
    if(palin[start]!=palin[len(palin)-start-1]):
        print("false")
        return
    palindrome(palin,start+1)
p="madam"
print(palindrome(p,0))             #MADAM ---s[0],s[-1]