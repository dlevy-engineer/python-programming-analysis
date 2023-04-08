# load dependencies
import pandas as pd
import os

if __name__ == "__main__":

    # read the dataset
    file_path = os.path.join('PyBank', 'Resources', 'budget_data.csv')
    bank_frame = pd.read_csv(file_path)


    ### ANALYSIS
    # extract the total number of months included
    total_months = len(bank_frame['Date'].unique())

    # extract the net profit/loss over the entire dataset
    total = bank_frame['Profit/Losses'].sum()

    # extract the average changes
    changes = bank_frame['Profit/Losses'].diff()
    avg_change = round(changes.mean(), 2)

    # extract full row at respective indices for minimum and maximum values in the `Profit/Losses` column
    min_index = changes.idxmin()
    max_index = changes.idxmax()

    # extract date and profit/loss for storage and display
    max_inc_date = bank_frame.iloc[max_index]['Date']
    max_inc = round(changes[max_index])

    max_dec_date = bank_frame.iloc[min_index]['Date']
    max_dec = round(changes[min_index])

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