import os
import csv

path=os.path.join("Resources","budget_data.csv")

with open(path, "r") as csvfile:
    csvreader=csv.reader(csvfile)
    csv_header=next(csvreader)

    month_total=0
    netTotal=0
    monthly_diff=[]
    date_list=[]
    initialVal= 0
    sumVal = 0
    count_difference = 0

    for row in csvreader:
        month_total+=1 #gradually counts the months as it goes down the sheet
        netTotal=netTotal+int(row[1]) #calculate sum as it does down the sheet
        if initialVal != 0:
            changedVal=int(row[1])-initialVal
            sumVal=sumVal+changedVal
            count_difference+=1
            monthly_diff.append(changedVal)
            date_list.append(row[0])

        initialVal=int(row[1])
        
average_diff=int(sumVal)/int(count_difference)

greatest_diff = max(monthly_diff)
lowest_diff = min(monthly_diff)
greatest_index = monthly_diff.index(greatest_diff)
lowest_index = monthly_diff.index(lowest_diff)

greatest_date = date_list[greatest_index]
lowest_date = date_list[lowest_index]

print("Financial Analysis")
print("------------------------------------------------------------------")
print(f"Total Months: {month_total}")
print(f"Total: ${netTotal}")
print(f"Average Change: ${round(average_diff,2)}")
print(f"The Greatest Increase in Profits: {greatest_date} (${greatest_diff})")
print(f"The Greatest Decrease in Profits: {lowest_date} (${lowest_diff})")

output_path=os.path.join("Resources","analysis.txt")

with open(output_path,"w") as analysis:
    analysis.write("Financial Analysis\n")
    analysis.write("------------------------------------------------------------------\n")
    analysis.write("Total Months: " + str(month_total)+"\n")
    analysis.write("Total: $" + str(netTotal)+"\n")
    analysis.write("Average Change: $" + str(round(average_diff,2))+"\n")
    analysis.write("The Greatest Increase in Profits: " + str(greatest_date) +" ($" + str(greatest_diff) +")\n")
    analysis.write("The Greatest Decrease in Profits: " + str(lowest_date) +" ($" + str(lowest_diff) +")\n")