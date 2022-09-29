import math
x=0.0374
y=-0.825
z=16
s=((1+pow(math.sin(x+y),2))/math.fabs(x-((2*y)/1+pow(x*y,2))))*pow(x,math.fabs(y))+pow(math.cos(math.atan(1/z)),2)
print( "z = {0:.5}" .format(s) )
