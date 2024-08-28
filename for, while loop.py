nums = [1,2,3,4,5]

for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)       #o/p: 1 2 Found!
    
    

nums = [1,2,3,4,5]

for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)       #o/p: 1 2 Found! 4 5
    
    

nums = [1,2,3,4,5]

for num in nums:
    for letter in 'abc':
        print(num, letter)   #o/p:1 a 1 d 1 c 2 a 2 b.....
        



x=0
while x<10:
    print(x)
    x += 1      #o/p: 0 1 2 3 4 5 6 7 8 9 
    

x=0
while x< 10:
    if x == 5:
        break 
    print(x)
    x += 1     #o/p: 0 1 2 3 4
    


    




    
    
