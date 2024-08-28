def hello_func():
    print('Hello Function!')

hello_func()                           #o/p: Hello Function!



def hello_func():
    return 'Hello Function!'

print(hello_func())                    #o/p: Hello Function!
print(hello_func().upper())            #o/p: HELLO FUNCTION!



def hello_func(greeting):
    return '{} Fuction.'.format(greeting)
print(hello_func('Hi'))               #o/p: Hi Function



def hello_func(greeting,name='You'):
    return '{},{}.'.format(greeting,name)
    
print(hello_func('Hi','Carrie'))     #o/p: Hi carrie



def student_info(*args,**kwargs):
    print(args)
    print(kwargs)
courses=['math','art']
info={'name':'John','age':22}
student_info(*courses,**info)       #o/p: ('math','art')  {'name':'John','age:22}'



month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    # year 2017
    # month 2
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(is_leap(2017))                        #o/p: False
print(days_in_month(2020,3))                #o/p: 31
