-------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Problem 4: Gaming Tournament
Description: A cricket gaming club is hosting a series og gaming tournaments throughout the day. However, the club has only one gaming arena, 
so only one match can be played at a time.
Each tournament match is assigned a start time and an end time in 24-hour format (hours only). If two matches are scheduled at overlapping times,
they cannot be played in the arena simultaneously.
Your task is to help the organisers determine whether the gaming tournament schedule is valid.
Given the schedule of matches, return true if all matches can be conducted without overlap in a single arena: otherwise, return false.
Note that if one match ends at the same time another begins, they are not considered overlapping.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Input:
The first line contains N, the number of matches.
The next N lines contain two integers separated by a space:
start_time_1 end_time_1
start_time_2 end_time_2
......
start_time_N end_time_N
Here,
->start_time specifies the time when the match begins (24-hour format)
->end_time specifies the time when the match ends (24-hour format)
->The matches may be given in any order.
->Time values are integers.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Output:
Print in a single line either
->true, if all tournament matches can be conducted without overlap or
->false, if any matches ovelap
Constraints:
1<=N<=100
0<=start_time<end_time<=24
Sample Input # 1
3
7 9 
1 3
3 7
Sample Output # 1
true
Sample Input # 2
3
1 10
3 5
6 8
Sample Output # 2
false'''
------------------------------------------------------------------------------------------------------------------------------------------------------------
Code:
N = int(input())
matches = []
valid = True

for i in range(N):
    start, end = map(int, input().split())
    matches.append((start, end))
matches.sort()

for i in range(N-1):
  current = matches[i]
  next_match = matches[i+1]
  
  if next_match[0]<current[1]:
    valid = False
    break

if valid:
  print("true")
else:
  print("false")
-------------------------------------------------------------------------------------------------------------------------------------------------------------
Output 1:
3
7 9 
1 3
3 7
Output 2:
3
1 10
3 5
6 8
false
----------------------------------------------------------------------------------------------------------------------------------------------------------------
