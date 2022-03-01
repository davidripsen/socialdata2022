# dri.py>
import pandas as pd

def printy():
    print('!Hola!')

def read_crime(focuscrimes=[]):
    # Read crime data and sort chronologically
    D = pd.read_csv('../data/Police_Department_Incident_Reports__Historical_2003_to_May_2018.csv')
    D['Date'] = pd.to_datetime(D.Date)
    D['Time'] = pd.to_datetime(D.Time)
    D = D.sort_values(by='Date')

    if focuscrimes:
        # Subset data for focus crimes
        D = D[D['Category'].isin(focuscrimes)]
    
    n, p = D.shape; print(f'rows = {n}, features = {p}')
    return(D)