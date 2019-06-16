def add_tip(total, tip_percent): 
    '''Return the total amount including tip'''
    tip = tip_percent*total
    return total + tip

#7a Hypotenuse Function
def hyp(leg1, leg2):
    '''Solves for hypotenuse'''
    c = leg1**2 + leg2**2
    return c**0.5

#7b Mean Function
def mean(a, b, c):
    '''Solves for mean'''
    ans = a + b + c
    return ans/3.0
    
#7c Perimeter Function
def perimeter(base, height):
    '''Solves for perimeter'''
    ans = base*2.0 + height*2.0
    return ans
    
#1.3.2 Function Test
print add_tip(20,0.15)
print add_tip(30,0.15)
print hyp(3,4)
print mean(3,4,7)
print perimeter(3,4)