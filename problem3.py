--------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Problem 3: Basic Voting System
Description: A school conducts student council elections every year and wants to digitize the vote-counting process.
Write a program that reads the list of candidates and the votes cast by students, calculates the percentage of votes received by each candidate, 
and determines the winner.
In the election, multiple candidates contest, and each student votes for one candidate of their choice.
After voting is complete, the program should count the votes, compute each candidate's vote percentage, 
and identify the candidate with the highest number of votes as the winner. 
If multiple candidates receive the highest number of votes, declare the result as a tie.
Input: The first line specifies a comma separated candidate list as below <serial_number>:<candidate_name>
Where serial_number identifies the candidate in the voting list and candidate_name identifies the candidate.
The second line cantains comma-separated votes, each referencing a candidate by their serial_number.
Output: Print N lines in which each line contains the percentage of vote received by each candidate rounded off to 2 decimal places in the below format 
<candidate_name> - <percentage_votes>
The list of candidates with percentage votes should be listed in the order of their serial number. 
The N+1 line should print the name of candidates that have a ties as Tie between <candidate_name1>, <candidate_name2>,.....,<candidate_nameN>
Consraints
1<=N<=10
1<=serial_number<=10
Sample Input # 1:
1:Rahul,2:Priya,3:Amit
1,2,2,1,3,2,1,1
Sample Output # 1:
Rahul - 50.00%
Priya - 37.50%
Amit - 12.50%
Winner is Rahul
Sample Input # 2:
1:Sneha,2:Karthik
1,2,2,1,2,2,1,1
Sample Output # 2:
Sneha - 50.00%
Karthik - 50.00%
Tie between Sneha, Karthik'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------
