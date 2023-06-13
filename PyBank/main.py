#importing modules necessary to read and write csv/text files
import os
import csv

#creating a path to retrieve the required csv file
path=os.path.join("budget_data.csv")

#beginning the reading process
with open(path, "r") as csvfile:
    csvreader=csv.reader(csvfile)
    #we know the csv contains a header, so in order to skip reading the header row, we perform the following function
    csv_header=next(csvreader)
    
    #initializing the values of total months and the eventual Profit/Loss Total
    month_total=0
    netTotal=0
    #creating empty lists from dates and the monthly difference between Profit/Loss values
    monthly_diff=[]
    date_list=[]
    #initializing values required to calculate monthly differences, sum and average of those monthly differences
    initialVal= 0
    sumVal = 0
    count_difference = 0

    #starting a for loop that allows us to begin reading each row in the csv file
    for row in csvreader:
        #this counts each row to give us the total number of months
        month_total+=1
        #this adds the values of Profit/Loss value to eventually provide us the total value once the file has been looped through to the end
        netTotal=netTotal+int(row[1])
        #the first value in the profit/loss column will not have a difference associated as there is no "previous value", so to skip that row we've hardcoding the initial profit/loss value as 0. The condition will not be met for the first row, but will continue on once initial value has been re-initialized
        if initialVal != 0:
            #calculating the difference in values between consecutive rows
            changedVal=int(row[1])-initialVal
            #adding those changed values as we continue through the loop
            sumVal=sumVal+changedVal
            #we need the count of each monthly difference in order to eventually calculate the average
            count_difference+=1
            #adding each difference and associated date into it's own list to later use when finding minimum and maximum values
            monthly_diff.append(changedVal)
            date_list.append(row[0])
            
        #once outside the conditional statement, we need to reinitialize the initialVal before looping into the next row
        initialVal=int(row[1])
#outside of the for loop, we beging to calculate the average change        
average_diff=int(sumVal)/int(count_difference)

#finding the minimum and maximum values in the monthly difference list
greatest_diff = max(monthly_diff)
lowest_diff = min(monthly_diff)

#knowing the above values, we need to retrieve the indexes for each value in the monthly difference list
greatest_index = monthly_diff.index(greatest_diff)
lowest_index = monthly_diff.index(lowest_diff)

#since we created the list of dates associated with each monthly difference, we use the indexes from the previous calculation to retrieve the dates associated with those values
greatest_date = date_list[greatest_index]
lowest_date = date_list[lowest_index]

#printing out the results of the analysis
print("Financial Analysis")
print("------------------------------------------------------------------")
print(f"Total Months: {month_total}")
print(f"Total: ${netTotal}")
print(f"Average Change: ${round(average_diff,2)}")
print(f"The Greatest Increase in Profits: {greatest_date} (${greatest_diff})")
print(f"The Greatest Decrease in Profits: {lowest_date} (${lowest_diff})")

#creating a text file and it's path
output_path=os.path.join("Resources","analysis.txt")

#writing our analysis into separate rows and saving them into the associated text file
with open(output_path,"w") as analysis:
    analysis.write("Financial Analysis\n")
    analysis.write("------------------------------------------------------------------\n")
    analysis.write("Total Months: " + str(month_total)+"\n")
    analysis.write("Total: $" + str(netTotal)+"\n")
    analysis.write("Average Change: $" + str(round(average_diff,2))+"\n")
    analysis.write("The Greatest Increase in Profits: " + str(greatest_date) +" ($" + str(greatest_diff) +")\n")
    analysis.write("The Greatest Decrease in Profits: " + str(lowest_date) +" ($" + str(lowest_diff) +")\n")
