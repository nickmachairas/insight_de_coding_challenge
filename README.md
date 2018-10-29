# Insight Data Engineering Coding Challenge

Prepared by Nick Machairas


## Problem


## Approach

The data of importance for this analysis are:
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


Problem statement indicates that we are only looking into data where the
application status is "CERTIFIED". As such, the code only stores and processes 
rows where the status is "CERTIFIED".


## Run



