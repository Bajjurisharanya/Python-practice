nums =[1,2,3,4,5,6,7,8,9,10]
my_list=[]
for n in nums:
    my_list.append(n)
print(my_list)                                                        #o/p:[1,2,3,4,5,6,7,8,9,10]



nums =[1,2,3,4,5,6,7,8,9,10]
my_list=[n for n in nums]
print(my_list)                                                        #o/p:[1,2,3,4,5,6,7,8,9,10]



nums =[1,2,3,4,5,6,7,8,9,10]
my_list=[]
for n in nums:
    my_list.append(n*n)
print(my_list)                                                         #o/p: [1,4,9,16,25,36,49,64,81,100]



nums =[1,2,3,4,5,6,7,8,9,10]
my_list=[n*n for n in nums]
print(my_list)                                                         #o/p: [1,4,9,16,25,36,49,64,81,100]
    


#nums =[1,2,3,4,5,6,7,8,9,10]
#my_list=map[lambda n: n*n, nums]
#print(my_list)                                                        #o/p: [1,4,9,16,25,36,49,64,81,100]



nums =[1,2,3,4,5,6,7,8,9,10]
my_list=[]
for n in nums:
    if n%2==0:
        my_list.append(n)
print (my_list)                                                         #o/p: [2,4,6,8,10]



nums =[1,2,3,4,5,6,7,8,9,10]
my_list=[n for n in nums if n%2==0]
print(my_list)                                                          #o/p: [2,4,6,8,10]                                  



nums=[1,2,3,4,5,6,7,8,9,10]
my_list =[]
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter,num))

print(my_list)                                                           #o/p: [('a',0),('a',1),('a',2),('a',3),('b',0).......]



nums=[1,2,3,4,5,6,7,8,9,10]
my_list=[(letter,num)for letter in'abcd' for num in range(4)]
print (my_list)                                                           #o/p: [('a',0),('a',1),('a',2),('a',3),('b',0).......]



names=['Bruce','clark','Peter']
heros=['Batman','Superman','Spiderman']
print (zip(names,heros))                                                  #o/p:[('Bruce','Batman'),('Clark','Superman')......]           



names=['Bruce','clark','Peter']
heros=['Batman','Superman','Spiderman']
my_dict={}
for name,heros in zip(names,heros):
    my_dict[name]=heros
print (my_dict)                                                           #o/p:{'Bruce':'Batman','Clark':'Superman'......}           



nums=[11,2,1,3,4,5,2,3,7,6,4,5]
my_set=set()
for n in nums:
    my_set.add(n)
print(my_set)                                                              #o/p:{1,2,3,4,5,6,7,11}



nums=[1,2,3,4,5,6,7,8,9,10]

def gen_func(nums):
    for n in nums:
        yield n*n
my_gen=gen_func(nums)
for i in my_gen:
    print (i)                                                             #o/p:1 4 9 16 25 36 49 64 81 100
    
    


nums=[1,2,3,4,5,6,7,8,9,10]
my_gen=(n*n for n in nums)
for i in my_gen:
    print(i)                                                               #o/p:1 4 9 16 25 36 49 64 81 100
  
