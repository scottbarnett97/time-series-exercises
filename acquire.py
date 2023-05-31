import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import env
import os
 

####################### Imports ############################

def check_file_exists(fn, query, url):
    '''
    this function checks to see if the .csv file already exists. If yes it reads it
    '''
    if os.path.isfile(fn):
        print('csv file found and loaded\n')
        return pd.read_csv(fn, index_col=0)
    else: 
        print('creating df and exporting csv\n')
        df = pd.read_sql(query, url)
        df.to_csv(fn)
        return df 
##############  Open Power Systems Data for Germany (opsd)#################    
def acquire_opsd_data():
    '''
    This function acquires the Open Power Systems Data for Germany (opsd) from
     "https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv"
     it returns an error message if failed
     # Usage ex:  opsd_data = acquire_opsd_data()
    '''
    url = "https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv"
    
    try:
        data = pd.read_csv(url)
        return data
    except Exception as e:
        print(f"Error occurred while acquiring data: {str(e)}")
        return None

    
    
############### star wars ##########################    
    
def fetch_all_people():
    ''' 
    pulls in people data from swapi.dev and makes a df
    to run:
    people_data = fetch_all_people()
    people = pd.DataFrame(people_data)
    '''
    #set url
    url = "https://swapi.dev/api/people/"
    #make list
    people = []
    #make loop
    while url is not None:
        response = requests.get(url)
        data = response.json()
        people.extend(data["results"])
        url = data["next"]
    return people

def fetch_all_planets():
    ''' 
    pulls in planets data from swapi.dev and makes a df
    to run:
    planets_data = fetch_all_planets()
    planets = pd.DataFrame(planets_data)
    '''
    #set url
    url = "https://swapi.dev/api/planets/"
    #make list
    planets = []
    #make loop
    while url is not None:
        response = requests.get(url)
        data = response.json()
        planets.extend(data["results"])
        url = data["next"] 
    return planets

def fetch_all_starships():
    ''' 
    pulls in starships data from swapi.dev and makes a df
    to run:
    starships_data = fetch_all_starships()
    starships = pd.DataFrame(starships_data)
    '''
    #set url
    url = "https://swapi.dev/api/starships/"
    #make list
    starships = []
    #make loop
    while url is not None:
        response = requests.get(url)
        data = response.json()
        starships.extend(data["results"])
        url = data["next"]
    return starships

