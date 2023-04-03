# question 5

# to get sine and cosine value for various angle
import math
# here math module is being imported first


for angle in range(0, 346, 15):
    # using for loop function starting from 0 with an increment of 15 degrees 
    radian = math.radians(angle)  #angle is converted into radians
    sine = round(math.sin(radian), 4) #sine and cosine function values are rounded of to 4 decimal places
    cosine = round(math.cos(radian), 4)
# here angle,radian ,sine, cosine are all variables declared
    print(f"Angle: {angle} degrees | Sine: {sine} | Cosine: {cosine}")
#  using f string to get result