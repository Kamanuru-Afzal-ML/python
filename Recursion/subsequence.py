def subsequences(input, output):
    if(len(input) == 0):
        print(output,end=" ")
        return
    subsequences(input[1:],output+input[0])
    subsequences(input[1:],output)
l="abcd"
empty=""
subsequences(l,empty)