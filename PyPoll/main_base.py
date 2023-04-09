import os
from csv import reader

# write a custom functuion for loading/reading the csv file
def load_csv(path):
    election_data = []

    # open file in read mode
    file = open(path,"r")

    # read the file
    lines = reader(file)
    for row in lines:
        # skip blank lines
        if not row:
            continue
        
        election_data.append(row)

    return election_data

if __name__ == "__main__":

    # instantiate the path to the data file
    file_path = os.path.join('PyPoll', 'Resources', 'election_data.csv')
    poll_frame = load_csv(file_path)

    ### Analysis

    # extract the number of votes cast by finding the length of the dataframe
    votes_cast = len(poll_frame) - 1

    # extract the candidate list by finding unique `Candidate` column` values 
    candidate_list = []

    for vote in poll_frame[1:]:

        if vote[2] not in candidate_list:
            candidate_list.append(vote[2])

    # extract the vote count for each candidate
    count_breakdown = [0] * len(candidate_list)
    for vote in poll_frame[1:]:
        count_breakdown[candidate_list.index(vote[2])] += 1

    # extract the vote distribution across the candidates
    percentage_breakdown = [round(count / votes_cast * 100, 3) for count in count_breakdown]

    # construct a string to display elections results for all candidates
    results_string = ''
    for i in range(0, len(candidate_list)):
        results_string += f'\n{candidate_list[i]}: {percentage_breakdown[i]}% ({count_breakdown[i]})\n'

    # extract the name of the winning candidate
    winner = candidate_list[percentage_breakdown.index(max(percentage_breakdown))]

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