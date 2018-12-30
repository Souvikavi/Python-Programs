#Simpsons Rule Numerical
def simp():
    
    def func(x):
        return (x**2 + 1)**(0.5)             #SAMPLE FUNCTION (x**2 + 1)**(0.5)
    
    
    a = float(input("Enter Lower Limit : "))
    b = float(input("Enter Upper Limit : "))
    n = int(input("Enter the value of 'n'(EVEN): "))
    
    h = (b-a)/n
    
    init = func(a)
    final = func(b)
    middle = 0
    
    for i in range (1,n):
        if i%2 == 0:
            middle += 2 * (func(a+(i*h)))
        else:
            middle += 4 * (func(a+(i*h)))
    return (h/3)* (init + final + middle)
