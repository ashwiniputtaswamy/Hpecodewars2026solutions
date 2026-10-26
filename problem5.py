=================================================================================================================================================================
'''Problem 5:
Description: Krish works in a factory that manufactures sports equipment requiring three different components. To avoid production delays, the factory must 
maintain an adequate supply of all three components.
The components are supplied in a packs of size X,Y, and Z. The factory can produce one equipment using one component of X,Y and Z each. Additionally, the 
factory can produce N equipment per day. For a period of M days, calculate the total number of components required and the number of packs of each componenet 
needed so that the production can continue without placing additional orders during that time - because krisk would rather order once properly than keep 
coming back to place the same order again and again.
For example, suppose the three componenets are supplied in pack sizes of 3, 4, and 6, and the factory produces 1 equipment item per day. Each equipment item
requires one componenet from each of the three componenet types. To avoid placing another order too soon, the factory should order enough componenets such that
the total quantity is divisible by all three pack sizes. The smallest such quantity is 12. Therefore, the factory must order 12 components of each type, which 
corresponds to 4 packs of X, 3 packs of Y, and 2 packs of Z. Since the factory produces 1 equipment item per day, this order will last for 12 days.
Input: The first line of input contains four space-separated integers: the pack sizes of the three components (X, Y, and Z) and the number of equipments 
produced by the factory in one day (N).
Output: Print five separated integers: the total number of componenets to be ordered in one go, the number of packs required for each of the three components, 
and the number of days after which the next order must be placed.
Constraints: 1<X,Y,Z,N<1000
Sample Input # 1
3 4 6 1
Sample Output # 1
12 4 3 2 12
Sample Input # 2
12 20 25 16
Sample Output # 2
300 25 15 12 18'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Code:
import math
X,Y,Z,N = map(int, input().split())
L = math.lcm(X,Y,Z)
packs_X = L // X
packs_Y = L // Y
packs_Z = L // Z
days = L // N
print(L, packs_X, packs_Y, packs_Z, days)
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Output 1
3 4 6 1
12 4 3 2 12
Output 2
12 20 25 16
300 25 15 12 18
===============================================================================================================================================================
