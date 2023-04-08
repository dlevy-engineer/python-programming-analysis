# load dependencies
import os
from csv import reader

# write a custom functuion for loading/reading the csv file
def load_csv(path):
    bank_data = []

    # open file in read mode
    file = open(path,"r")

    # read the file
    lines = reader(file)
    for row in lines:
        # skip blank lines
        if not row:
            continue
        
        bank_data.append(row)

    return bank_data

if __name__ == "__main__":
    # call our custom reading function on our `budget_data.csv` file
    file_path = os.path.join('PyBank', 'Resources', 'budget_data.csv')
    bank_data = load_csv(file_path)

    ### ANALYSIS
    ## begin by instantiating variables necessary to capture valuable information while looping

    # set an index counter
    i = 0

    # extract the total number of months included
    # assume there could be duplicate months
    total_months = 0
    monthlist = []

    # extract the net profit/loss over the entire dataset
    total = 0

    # extract the average changes
    changes = []
    prev_p_l = 0
    cur_p_l = 0

    # extract respective indices for minimum and maximum `Profit/Losses` values
    max_index = 0
    min_index = 0

    # loop through all lines of data excluding the header
    for row in bank_data[1:]:

        # ensure no double-counting of months
        if row[0] not in monthlist:
            monthlist.append(row[0])
            total_months += 1

        # start tracking profit/loss changes and looking for max/min values in the second loop
        if i != 0:
            # set a new current profit/loss value and calculate the change
            cur_p_l = int(row[1])
            changes.append(cur_p_l - prev_p_l)

            # check for max/min change values
            if int(changes[i - 1]) > changes[max_index]:
                max_index = i - 1
            if int(changes[i - 1]) < changes[min_index]:
                min_index = i - 1

        prev_p_l = int(row[1])

        total = total + int(row[1])

        i += 1
            
    # calculate average of the values in our `changes` list
    avg_change = round(sum(changes) / len(changes), 2)

    # use our max/min indices to extract a date from `bank_data` and the corresponding change value from `changes`
    # we add 2 to the indices to account for header and the non-existent first change value
    max_inc_date = bank_data[max_index + 2][0]
    max_inc = changes[max_index]

    max_dec_date = bank_data[min_index + 2][0]
    max_dec = changes[min_index]

    header = 'Financial Analysis\n----------------------------\n'
    body = f"""Total Months: {total_months}
Total: ${total}
Average Change: ${avg_change}
Greatest Increase in Profits: {max_inc_date} (${max_inc})
Greatest Decrease in Profits: {max_dec_date} (${max_dec})"""
    
    print(header + body)

    # output a textfile containing the analysis results
    output_path = os.path.join('PyBank', 'analysis', 'results.txt')
    with open(output_path, 'w') as f:
        f.write(header + body)