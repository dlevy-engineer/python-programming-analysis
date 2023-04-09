import pandas as pd
import os

if __name__ == "__main__":

    # instantiate the path to the data file
    file_path = os.path.join('PyPoll', 'Resources', 'election_data.csv')

    # read the election data into a pandas dataframe
    poll_frame = pd.read_csv(file_path)

    ### ANALYSIS

    # extract the number of votes cast by finding the length of the dataframe
    votes_cast = len(poll_frame)

    # extract the candidate list by finding unique `Candidate` column` values
    candidate_list = poll_frame['Candidate'].unique()

    # extract the vote count for each candidate
    count_breakdown = poll_frame['Candidate'].value_counts()

    # extract the vote distribution across the candidates
    percentage_breakdown = round(poll_frame['Candidate'].value_counts(normalize=True) * 100, 3)

    # extract the name of the winning candidate
    winner = percentage_breakdown.index.tolist()[0]

    # construct a string to display elections results for all candidates
    results_string = ''
    for cand in percentage_breakdown.index:
        results_string += f'\n{cand}: {percentage_breakdown[cand]}% ({count_breakdown[cand]})\n'

    # construct output strings
    
    header = """Election Results

------------------------------\n\n"""
    
    body = f"""Total Votes: {votes_cast}

------------------------------
{results_string}
------------------------------

Winner: {winner}

------------------------------"""

    # print output to console
    print(header + body)

    # output text to analysis file
    output_path = os.path.join('PyPoll', 'analysis', 'results.txt')
    with open(output_path, 'w') as f:
        f.write(header + body)