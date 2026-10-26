================================================================================================================================================================
'''Problem 6: World Cup Group Stage Ranking
Description: The FIFA World Cup group stage is in full swing! Each group has N teams, and every team plays a series of matches. After all matches are played, 
you are given each team's total points and goal difference. Goal difference is calculated across all matches played by that team: total goals scored minus
total goals conceded.
Your job is to print the final group standings, ranked from 1st to last, using these rules:
--> Teams with more points across all amtches are ranked higher.
--> If two or more teams have the same number of points, the team with a higher goal difference is ranked higher.
--> If both points and goal difference are the same, rank the teams in alphabetical order by team name.
Print the team names in order from 1st place to last place, one per line.
Input: The first line contains an integer N: the number of teams in the group.
The next N lines each contain: 
    team_name points goal_difference
where team_name is a single word with no spaces, points is the team's total points from all matches played, and goal_difference is the team's overall goal 
difference from all matches played.Goal difference can be negative.
Output: Print the ranked team names on N separate lines, from 1st place to last place, with one team name per line.
Constriants
2<=N<=32
-100<=goal_difference<=100
0<=points<=30
Note that all team names are unique and team names contain only English letters having length less than 20 characters.
Sample Input # 1
4
Brazil 6 5
'''
