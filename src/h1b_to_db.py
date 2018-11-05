# -- Imports -----------------------------------------------------------------

import csv
import os
from sqlalchemy import (create_engine, Column, String, Integer)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from tqdm import tqdm
import pandas as pd


# -- Vars --------------------------------------------------------------------

# IN_FNAME = "h1b_input.csv"
IN_FNAME = "H1B_FY_2015.csv"
INPUT_DIR = os.path.join(os.getcwd(), "input")
OUTPUT_DIR = os.path.join(os.getcwd(), "output")

# -- Known Column Names ------------------------------------------------------

known_number_column = ['CASE_NUMBER', 'CASE_NO', 'LCA_CASE_NUMBER']
known_status_column = ['CASE_STATUS', 'STATUS', 'Approval_Status']
known_code_column = ['SOC_CODE', 'LCA_CASE_SOC_CODE']
known_soc_column = ['SOC_NAME', 'LCA_CASE_SOC_NAME', 'Occupational_Title']
known_state_column = ['WORKSITE_STATE', 'LCA_CASE_WORKLOC1_STATE', 'State_1']


# -- DB setup ----------------------------------------------------------------

conn_url = "postgresql://USERNAME:PASSWORD@DB_HOST/DB_NAME"

Base = declarative_base()
engine = create_engine(conn_url)
Session = sessionmaker(bind=engine)
session = Session()

class LCAdata(Base):
    __tablename__ = "lca_data"

    case_id = Column(String(20), primary_key=True)
    status = Column(String(25))
    soc_code = Column(String(10))
    soc_name = Column(String(100))
    state = Column(String(2))
    year = Column(Integer)

    def __repr__(self):
        return "<{}, {}, {}, {}, {}, {}>".format(self.case_id, self.status,
                    self.soc_code, self.soc_name, self.state, self.year)

Base.metadata.create_all(engine)


# -- Read input file ---------------------------------------------------------

with open(os.path.join(INPUT_DIR, IN_FNAME), 'r') as input_file:
    rd = csv.reader(input_file, delimiter=';')
    header = next(rd)

    # Note: the following try clauses can be improved to capture errors
    # instead of passing

    # Locate the index of the case number column
    for i in known_number_column:
        try:
            number_index = header.index(i)
        except ValueError:
            pass

    # Locate the index of the status column
    for i in known_status_column:
        try:
            status_index = header.index(i)
        except ValueError:
            pass

    # Locate the index of the soc code column
    for i in known_code_column:
        try:
            code_index = header.index(i)
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
    data = {'case_id': [], 'status': [], 'soc_code': [], 'soc_name': [],
            'state': [], 'year': []}

    # Go through rows and push to DB
    for row in tqdm(rd):
        case_id = row[number_index]
        status = row[status_index]
        soc_code = row[code_index]
        soc_name = row[soc_index]
        state = row[state_index]

        # new_row = LCAdata(case_id=case_id, status=status, soc_code=soc_code,
        #                   soc_name=soc_name, state=state, year=2014)

        # session.add(new_row)
        # session.commit()

        data['case_id'].append(case_id)
        data['status'].append(status)
        data['soc_code'].append(soc_code)
        data['soc_name'].append(soc_name)
        data['state'].append(state)
        data['year'].append(2015)


# Create temporary dataframe
df = pd.DataFrame(data)
df.to_csv(os.path.join(OUTPUT_DIR, '2015_subset.csv'),
          header=False, index=False)
