# python-programming-analysis
A basic Python programming project focused on financial analysis and evaluating election results. The solutions implemented in the `main.py` files are reliant upon the `Pandas` package. The `main_base.py` files are not reliant upon `Pandas`.

- PyBank analyzes financial records for a company's shareprice over an 86-month timespan.
- PyPoll analyzes the election outcome of a small town's mayoral voting process.

## PyBank Procedure
Create a Python script to analyze a firm's financial records. We are given a financial dataset called `budget_data.csv`. The dataset is composed of two columns: "Date" and "Profit/Losses".

Our task is to create a Python script that analyzes the records to calculate each of the following values:
- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The changes in "Profit/Losses" over the entire period, and then the average of those changes
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in profits (date and amount) over the entire period

Results:

    Financial Analysis
    ----------------------------
    Total Months: 86
    Total: $22564198
    Average Change: $-8311.11
    Greatest Increase in Profits: Aug-16 ($1862002)
    Greatest Decrease in Profits: Feb-14 ($-1825558)

Our Python script prints this analysis to the terminal and exports a text file with the results.

## PyPoll Procedure
Create a Python program that can help a small, rural town modernize its vote-counting process.

We are given a set of poll data called `election_data.csv`. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Our task is to create a Python script that analyzes the votes and calculates each of the following values:
- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote

Results:

    Election Results
    -------------------------
    Total Votes: 369711
    -------------------------
    Charles Casper Stockham: 23.049% (85213)
    Diana DeGette: 73.812% (272892)
    Raymon Anthony Doane: 3.139% (11606)
    -------------------------
    Winner: Diana DeGette
    -------------------------

Our Python script prints this analysis to the terminal and exports a text file with the results.