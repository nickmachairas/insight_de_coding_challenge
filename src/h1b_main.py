import csv
import os

FILENAME = "h1b_input.csv"
FILENAME2 = "H1B_FY_2014.csv"
INPUT_DIR = os.path.join(os.getcwd(), "input")
OUTPUT_DIR = os.path.join(os.getcwd(), "output")

# FY17: "CASE_STATUS", "SOC_NAME", "WORKSITE_STATE"
# FY16: "CASE_STATUS", "SOC_NAME", "WORKSITE_STATE"
# FY15: "CASE_STATUS", "SOC_NAME", "WORKSITE_STATE"
# FY16: "STATUS", "LCA_CASE_SOC_NAME", "LCA_CASE_WORKLOC1_STATE"

known_status_column = ['CASE_STATUS', 'STATUS', 'Approval_Status']
known_soc_column = ['SOC_NAME', 'LCA_CASE_SOC_NAME', 'Occupational_Title']
known_state_column = ['WORKSITE_STATE', 'LCA_CASE_WORKLOC1_STATE', 'State_1']


with open(os.path.join(INPUT_DIR, FILENAME2)) as fd:
    rd = csv.reader(fd, delimiter=";")
    header = next(rd)

    # Locate the index for the status column
    for i in known_status_column:
        try:
            status_index = header.index(i)
        except ValueError:
            pass

    # Locate the index for the soc name column
    for i in known_soc_column:
        try:
            soc_index = header.index(i)
        except ValueError:
            pass

    # Locate the index for the state column
    for i in known_state_column:
        try:
            state_index = header.index(i)
        except ValueError:
            pass

    # Create an empty dictonary to store data
    data = {'soc': [], 'state': []}

    for row in rd:
        if row[status_index] == "CERTIFIED":
            # print("status:", row[status_index], "soc:", row[soc_index],
            #       "state:", row[state_index])
            # DO NOT STORE STATUS --> WASTE OF SPACE
            data['soc'].append(row[soc_index])
            data['state'].append(row[state_index])

# print(data)

for i in set(data['soc']):
    print(i, data['soc'].count(i))
