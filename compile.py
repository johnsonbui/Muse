# Uses data found in MySQL to "compile" information for analysis

# General idea is to:
# Retrieve entries in the DB
# For each record, query for lyrics 
# Given duplicate results based on listenCount 
# Store results in running json file