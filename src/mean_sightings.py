from __future__ import division 
import pandas as pd
import numpy as np

def temp_get_sightings(filename, focusanimal):

    # Load table
    tab = pd.read_csv(filename)

    # Find number of records and total count of animals seen
    isfocus = (tab['Animal'] == focusanimal.capitalize())       
    totalrecs = np.sum(isfocus)
    if totalrecs == 0:
        meancount = 0
    else:
        meancount = np.mean(tab['Count'][isfocus])

    # Return num of records and animals seen
    return totalrecs, meancount
    
def get_sightings(filename, focusanimal):

    # Load table
    tab = pd.read_csv(filename)

    # Standardize capitalization of focusanimal
    focusanimal = focusanimal.capitalize()

    # Loop through all records, countings recs and animals
    totalrecs = 0
    totalcount = 0
    for i, rec in tab.iterrows(): # Iterate through DataFrame rows
        if rec['Animal'] == focusanimal:
            totalrecs += 1
            totalcount += rec['Count']       
        if totalcount == 0:
            meancount = 0
        else:
            meancount = totalcount/totalrecs

    # Return num of records and animals seen
    return totalrecs, meancount