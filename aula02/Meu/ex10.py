from numpy import angle


print("Enter the coordinates in mm from the center of the board.")
x = float(input("x? "))
y = float(input("y? "))


POINTS = (20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5)

if (x**2 +y**2) < 6.35**2:
    score = 50

elif 6.35**2 < (x**2 + y**2) < 16**2:
    score = 25

elif 26**2 < (x**2 + y**2) < 170**2:
    import math
    angle = math.atan2 (x,y)
    

print(score)