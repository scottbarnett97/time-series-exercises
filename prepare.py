import pandas as pd
import numpy as np


##################   Prep Store data  ####################
def prep_store(df):
    '''
    this function will prep the store df by:
    dropping time from sale_date
    converting sale date to datetime format
    setting sale_date to index
    adding a montha nd dayof week column
    Add a column, sales_total, which is a derived from sale_amount (total items) and item_price
    '''
    df.sale_date = df.sale_date.str.replace(' 00:00:00 GMT', '')
    df.sale_date = pd.to_datetime(df.sale_date, format = '%a, %d %b %Y')
    df = df.set_index('sale_date')
    # add month calling on the index using DatetimeIndex
    df['month'] = pd.DatetimeIndex(df.index).month
    # add day of the week calling on the index using DatetimeIndex
    # Monday=0, and Sunday=6.
    df['day_of_week'] = pd.DatetimeIndex(df.index).dayofweek
    # add column for sales_total
    df['sales_total'] = df['sale_amount']*df['item_price']
    return df

###############    prep opsd ##########################

def prep_opsd_data(df):
    ''' 
    This function prepares the opsd df by:
    converting date to datetimeformat and making it the index
    adds colums for month, year
    fill nulls with '0'
    '''
    # Convert date column to datetime format
    df.Date = pd.to_datetime(df.Date)
    # Set the index to be Date
    df = df.set_index('Date')
    # add month calling on the index using DatetimeIndex
    df['month'] = pd.DatetimeIndex(df.index).month
    # add year calling on the index using DatetimeIndex
    df['year'] = pd.DatetimeIndex(df.index).year
    # fill missing values with '0'
    df = df.fillna(0)
    return df