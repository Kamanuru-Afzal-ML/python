num=int(input("enter number:"))
length =len(str(num))
temp=num
sum=0
while num!=0:
    rem=num%10
    sum+=rem**length
    num//=10
print('armstrong number') if(sum==temp) else print('not armstrong number') 

#by using divmod

number=sum
another_temp=sum
total=0
while number!=0:
    rem=divmod(number,10)
    total+=rem[1]**length
    number=rem[0]
print('armstrong number') if(another_temp==total) else print('not armstrong number')

