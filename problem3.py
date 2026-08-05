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
candidate_input=input()
candidate_details=candidate_input.split(",")
#print(candidate_details)
candidates={}
vote_count={}
winners=[]
for candidate in candidate_details:
    serial,name=candidate.split(":")
    candidates[serial]=name
    vote_count[serial]=0
vote_list = input().split(",") 
#print(vote_list)
#print(candidates)
for vote in vote_list:
    #print(vote)
    vote_count[vote]+=1
total_votes=len(vote_list)
highest_votes=max(vote_count.values())
#print(f"The total votes are,{total_votes}")
for serial in candidates:
    #print(candidates[serial],"->",vote_count[serial])
    percentage = (vote_count[serial]/total_votes)*100
    print(f"{candidates[serial]} - {percentage:.2f}%")
    if vote_count[serial]==highest_votes:
        #print(f"{candidates[serial]} is the winner")
        winners.append(candidates[serial])
if len(winners)==1:
    print(f"Winner is {winners[0]}")
elif len(winners)>1:
    print("Tie between",", ".join(winners))
----------------------------------------------------------------------------------------------------------------------------------------------------------------
Output 1:
1:Rahul,2:Priya,3:Amit
1,2,2,1,3,2,1,1
Rahul - 50.00%
Priya - 37.50%
Amit - 12.50%
Winner is Rahul
----------------------------------------------------------------------------------------------------------------------------------------------------------------
Output 2: 
1:Sneha,2:Karthik
1,2,2,1,2,2,1,1
Sneha - 50.00%
Karthik - 50.00%
Tie between Sneha, Karthik
