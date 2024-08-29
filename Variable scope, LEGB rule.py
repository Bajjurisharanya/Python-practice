x='global x'
def test():
    y='local y'
    print(y)             #o/p: local y 
    print(x)             #o/p: global x     
 
test()
print(x)                 #o/p: global x



def test(z):
    x='local x'
    print(z)
    
test('local z')           #o/p: local z



m=min([5,1,4,3,2,6]) 
print(m)                   #0/p: 1



def min():
    pass

m=min([5,1,4,3,2,6]) 
print(m)                   #o/p: error



def my_min():
    pass

m=min([5,1,4,3,2,6]) 
print(m)                     #o/p: 1



def outer():
    x='outer x'
    print(3)
    
    def inner():
        x='inner x'
        print(1)
        
    inner()
    print(2)
    
outer()                  #o/p: 3 1 2    
