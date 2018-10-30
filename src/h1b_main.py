# -- Imports -----------------------------------------------------------------

import csv
import os


# -- Vars --------------------------------------------------------------------

IN_FNAME = "h1b_input.csv"
OUT_FNAME_SOC = "top_10_occupations.txt"
OUT_FNAME_STATE = "top_10_states.txt"
INPUT_DIR = os.path.join(os.getcwd(), "input")
OUTPUT_DIR = os.path.join(os.getcwd(), "output")


# -- Known Column Names ------------------------------------------------------

known_status_column = ['CASE_STATUS', 'STATUS', 'Approval_Status']
known_soc_column = ['SOC_NAME', 'LCA_CASE_SOC_NAME', 'Occupational_Title']
known_state_column = ['WORKSITE_STATE', 'LCA_CASE_WORKLOC1_STATE', 'State_1']


# -- Read input file ---------------------------------------------------------

with open(os.path.join(INPUT_DIR, IN_FNAME), 'r') as input_file:
    rd = csv.reader(input_file, delimiter=';')
    header = next(rd)

    # Note: the following try clauses can be improved to capture errors
    # instead of passing

    # Locate the index of the status column
    for i in known_status_column:
        try:
            status_index = header.index(i)
        except ValueError:
            pass

    # Locate the index of the soc name column
    for i in known_soc_column:
        try:
            soc_index = header.index(i)
        except ValueError:
            pass

    # Locate the index of the state column
    for i in known_state_column:
        try:
            state_index = header.index(i)
        except ValueError:
            pass

    # Create an empty dictionary to store data
    data = {'soc': [], 'state': []}

    # Go through rows and if "CERTIFIED", store soc and state in dic
    for row in rd:
        if row[status_index] == "CERTIFIED":
            data['soc'].append(row[soc_index])
            data['state'].append(row[state_index])


# -- Data processing ---------------------------------------------------------

# Get a count of total certified data rows
data_count = len(data['soc'])

# Create an empty list to store socs, counts, percentages
pre_sorted_soc = []

# Loop through socs
for i in set(data['soc']):
    soc_count = data['soc'].count(i)
    soc_perc = "{:.1%}".format(soc_count/data_count)
    pre_sorted_soc.append([i, soc_count, soc_perc])

# Sort soc array based on count, alphabetically
sorted_soc = sorted(pre_sorted_soc, key=lambda x: (-x[1], x[0]))

# Create an empty list to store states, counts, percentages
pre_sorted_state = []

# Loop through states
for i in set(data['state']):
    state_count = data['state'].count(i)
    state_perc = "{:.1%}".format(state_count/data_count)
    pre_sorted_state.append([i, state_count, state_perc])

# Sort state array based on count, alphabetically
sorted_state = sorted(pre_sorted_state, key=lambda x: (-x[1], x[0]))


# -- Write output files ------------------------------------------------------

with open(os.path.join(OUTPUT_DIR, OUT_FNAME_SOC), 'w') as out_soc:
    out_soc.write('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')

    # Write only top 10 or less
    for i in sorted_soc[:10]:
        out_soc.write('{};{};{}\n'.format(i[0], i[1], i[2]))


with open(os.path.join(OUTPUT_DIR, OUT_FNAME_STATE), 'w') as out_state:
    out_state.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')

    # Write only top 10 or less
    for i in sorted_state[:10]:
        out_state.write('{};{};{}\n'.format(i[0], i[1], i[2]))
