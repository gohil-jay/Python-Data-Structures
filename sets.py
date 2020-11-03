"""Module for sets."""

def set_operations():
    """Function for sets."""

    a = {1,2,3,4,5} #creating set
    b = {3,4,5,6}
    print(a)
    print(b)

    c = a.intersection(b) #same as below
    d = a&b #same as above
    print(c)
    print(d)
    print()

    e = a.union(b) #same as below
    f = a|b #same as above
    print(e)
    print(f)
    print()
    
    g = a.difference(b) #same as below
    h = a-b #same as above
    print(g)
    print(h)
    print()

    i = a.symmetric_difference(b) #same as below
    j = a^b #same as above
    print(i)
    print(j)
    print()

    k = a.issuperset(b) #same as below
    l = a>=b #same as above
    print(k)
    print(l)
    print()

    m = a.issubset(b) #same as below
    n = a<=b #same as above
    print(m)
    print(n)
    print()

    o = a.isdisjoint(b) #same as below
    print(o)
    print()

def single_set_operations():
    """Module for single set opeartions"""

    x = {1,1,2,3} #its a set, thus, an element only occurs once
    x.add(4)
    print(x)
    x.remove(3)
    print(x)
    x.update({9,10})
    print(x)
    print()
    print("The lenth of 'x' is : ", len(x))
    print()
    
    print(2 in x)
    print(5 not in x)

def two_dim_sets():
    """2D Sets dont work generally."""

    #y = {{1,2},{3,4}} #returns error
    y = {frozenset({1,2}),frozenset({3,4})} #this works, but is immutable (use 2d arrays)
    print(y)

single_set_operations()
