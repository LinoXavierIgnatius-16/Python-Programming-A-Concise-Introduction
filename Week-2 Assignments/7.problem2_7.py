def problem2_7():
    """ computes area of triangle using Heron's formula. """
    a = float(input("enter length of side one:"))
    b = float(input("enter length of side two:"))
    c = float(input("enter length of side three:"))
    s = ((.5)*(a+b+c))
    area = ((s*(s-a)*(s-b)*(s-c))**0.5)
    print("Area of a triangle with sides",a,b,c,"is",area)
    
