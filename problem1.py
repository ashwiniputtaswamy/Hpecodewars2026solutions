-------------------------------------------------------------------------------------------------------------------------------------------------------
'''Problem 1: Inscribed Circle in a Square
Description: A company is looking at manufacturing a plastic holder for football. 
They want to build a square in which a football can be placed so that it doesn't move around during transportation. 
Given the side length S of a square, calculate the area of the region that lies inside the square but outside the circle inscribed within it. 
The circle has a diameter equal to S.
Print the resulting area rounded to 2 decimal places.
Input: A positive number S (side length of the square)
Output: A single number, the area of the square minus the area of hte inscribed circle, rounded to 2 decimal places
Constraints: 0 < S ≤ 10³
Sample Input # 1
10
Sample Output # 1
21.46
Sample Input # 2
42
Sample Output # 2
378.56'''
------------------------------------------------------------------------------------------------------------------------------------------------------
import math
S = int(input(""))
if S>0 and S<=1000:
    area_of_square = pow(S,2)
    area_of_circle = math.pi*((S/2)**2)
    remaining_area=area_of_square-area_of_circle
    print(f"{remaining_area:.2f}")

-------------------------------------------------------------------------------------------------------------------------------------------------------
Output 1:
10
21.46
Output 2:
42
378.56
-------------------------------------------------------------------------------------------------------------------------------------------------------
