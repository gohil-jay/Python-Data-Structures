"""This is a module for tuple.""" #for docstring use "", and not ''
# mutable data type

def tuples():
    
    """This is a function named Tuple"""

    a = (1,3000,'Tesseract',14000605) #tuple [follows most array functions and rules]

    b = 1,3000,'Tesseract',14000605 #if we dont put any brackets, its tuple by default
    print(b)



    '''---------------------------------------------------------------------------------'''

    x = {1:2,'a':2,'abc':'akjsgdjag',34:'skhdskuh'}
    print(x) #returns full dictionary

    dict = {
        'a' : 1,
        'b' : 2,
        'c' : 'abc',
        'd' : 3,
    }

    print(dict)

    for y in x:
        print(y)   #returns all keys

    print()
    print(x[1]) #returns 2
    print(x['a']) #returns 2


    print(x(1)) #returns error
    #we can only use 'variable()' for calling an attribute of an 'object'

    print(x[a]) #returns key error
    print(x[0]) #returns key error as indexing doesnt work here; only 'key' and pair

