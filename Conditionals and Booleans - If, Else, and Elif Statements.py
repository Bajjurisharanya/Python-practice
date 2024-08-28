language='Java'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No match')      #o/p:Language is Java
    
    
user ='Admin'
logged_in = True
if user == 'Admin' and logged_in:
    print('Admin page')
else:
    print('Bad creds')    #o/p: Admin page
    
    
    
a= [1,2,3]
b= [1,2,3]
print(a is b)    #o/p: False



a= [1,2,3]
b= a
print(id(a))
print(id(b))
print((id(a)==id(b)))  #o/p:True
