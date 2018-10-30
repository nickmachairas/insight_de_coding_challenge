# Insight Data Engineering Coding Challenge

*Prepared by Nick Machairas, submitted on 10/30/2018.*


## Problem

As part of Insight's Data Engineering Coding Challenge we were tasked with 
writing a program that processes raw H1B(H-1B, H-1B1, E-3) data and produces
basic insights on the top 10 occupations and states. There are several well-made
"3rd-party" libraries that could be used to run this analysis. At first thought,
the main challenge appeared to be that we were restricted on using default 
libraries only. By the end of this challenge, it was actually made obvious that
the program was more efficient by using the default libraries.


## Approach

The columns of importance for this analysis are:
1. application status
2. occupation code (group)
3. State of work location

Code is agnostic of the ordering of the input dataset columns. However, the 
column names of interest must be known. I checked the file structure for LCA 
Programs (H-1B, H-1B1, E-3) which revealed the following:

- FY17 (H1B): "CASE_STATUS", "SOC_NAME", "WORKSITE_STATE"
- FY16 (H1B): "CASE_STATUS", "SOC_NAME", "WORKSITE_STATE"
- FY15 (H1B): "CASE_STATUS", "SOC_NAME", "WORKSITE_STATE"
- FY14 (H1B): "STATUS", "LCA_CASE_SOC_NAME", "LCA_CASE_WORKLOC1_STATE"
- FY13 (LCA): "STATUS", "LCA_CASE_SOC_NAME", "LCA_CASE_WORKLOC1_STATE"
- FY12 (LCA): "STATUS", "LCA_CASE_SOC_NAME", "LCA_CASE_WORKLOC1_STATE"
- FY11 (LCA): "STATUS", "LCA_CASE_SOC_NAME", "LCA_CASE_WORKLOC1_STATE"
- FY10 (LCA): "STATUS", "LCA_CASE_SOC_NAME", "LCA_CASE_WORKLOC1_STATE"
- FY09 (LCA): "STATUS", "LCA_CASE_SOC_NAME", "LCA_CASE_WORKLOC1_STATE"
- FY08 (LCA): "Approval_Status", "Occupational_Title", "State_1"

As such, the code looks for columns named "CASE_STATUS", "STATUS", 
"Approval_Status" for application status and so forth for SOC name and state 
as indicated by the list above. If a dataset is used with a new column name,
the code will return an error. 

Problem statement indicates that we are only looking into data where the
application status is "CERTIFIED". As such, the code only stores and processes 
rows where the status is "CERTIFIED".

There was a thought about whether the code should analyze multiple files if 
more than one was placed in the input directory. I decided to follow the project
guidelines strictly where the directory structure hints at having only one file
in the input directory. Therefore, it is required that the input file is named 
"h1b_input.csv" for the code to run.

Due to shortage of time, no additional tests were implemented but several were 
considered.

## Run

Code was written in Python 3. It uses default libraries only, no need to install
additional libraries. From within the working directory run with:

```bash
$ ./run.sh 
```

The repo passed the check at the provided test website.