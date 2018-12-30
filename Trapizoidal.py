# BY USING LAMBDA 
#INPUT AS "trapizoidal (lambda x : function)"

def trapizoidal(func):    
    a = float(input("Enter Lower Limit : "))
    b = float(input("Enter Upper Limit : "))
    n = int(input("Enter the value of 'n': "))
    
    h = (b-a)/n
    init = func(a)
    final = func(b)
    middle_values =0
    for i in range (1,n):              #as range will go from 1 to n-1
        middle_values += func(a+(i*h))
    print (f"({h/2})*({init} + {final} + 2*{middle_values})")
    return (h/2)*(init + final + 2*(middle_values))
