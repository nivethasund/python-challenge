#importing modules needed to perform analysis
import os
import csv

#identifying path allowing us to read the csv file
path=os.path.join("Resources","election_data.csv")

#initializing the count of total ballots to 0 before analyzing each row, and also initializing lists for candidates and votes per candidate
count=0
candidate_list=[]
ballot_list=[]

#reading the csv file and skipping the header row
with open(path, "r") as polls:
    csvreader=csv.reader(polls, delimiter=",")
    csv_header=next(csvreader)


    #we begin a for loop to count each ballot ID, as well as append the candidate name to the candidate list we created in the beginning
    for row in csvreader:
        count+=1
        candidate_list.append(row[2])

    #our candidate list has many repeats, so we want to find the unique set of candidate by using the "set" function. To sort the list, we use the sort function as well    
    unique_candidate=list(set(candidate_list))
    unique_candidate.sort()

    #this second for loop goes through the first candidate list and counts the number of entries per unique candidate. These are votes that we later append to a separate list
    for candidate in unique_candidate:
        ballot_count=candidate_list.count(candidate)
        ballot_list.append(ballot_count)

#printing out analysis and total votes        
print("Election Results")
print("----------------------------------------")
print(f"Total Votes : {count}")
print("----------------------------------------")

#we zip the unique candidate list and the ballot list, so it's easier to pull total votes associated with a unique candidate
for x,y in zip(unique_candidate,ballot_list):
        percentage=(int(y)/int(count)*100) #calculating percentage of votes
        print(f"{x}: {round(percentage,3)}% ({y})") #printing results per candidate

#in order to find the winner, we find the index of the maximum value in the ballot list and use that index in the candidate list
winner_index=ballot_list.index(max(ballot_list))
winner=unique_candidate[winner_index]

print("----------------------------------------")
print(f"Winner : {winner}")
print("----------------------------------------")

#creating a text file to begin writing the analysis
output_path=os.path.join("Resources","analysis.txt")

with open(output_path,"w") as analysis:
    analysis.write("Election Results\n")
    analysis.write("----------------------------------------\n")
    analysis.write(f"Total Votes : {count}\n")
    analysis.write("----------------------------------------\n")

    for x,y in zip(unique_candidate,ballot_list):
        percentage=(int(y)/int(count)*100)
        analysis.write(f"{x}: {round(percentage,3)}% ({y})\n")
    
    analysis.write("----------------------------------------\n")
    analysis.write(f"Winner : {winner}\n")
    analysis.write("----------------------------------------\n")
