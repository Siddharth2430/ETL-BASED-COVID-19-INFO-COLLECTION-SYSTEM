# import for the request package to request the required data regarding covid19_stats
import requests

# importing date and time functions
from datetime import datetime

# getting todays date and time of data_fetch
now = datetime.now()
dt = now.strftime("%B-%d-%Y %H:%M:%S")

# define the method to request and get the data in JSON format and print it
def fetch_stats():
    # declaring the dictionaries
    s_wise_dict = {}
    dist_count = 0
    act = 0
    final_list = []
    # requesting data and getting in in res, which is a dictionry
    covid_data = requests.get('https://api.covid19india.org/state_district_wise.json')
    # breaking the dictionary step-wise
    # breaking the main dict. into keys(states) and values(their details)
    for state_name, state_dict in covid_data.json().items():
        # if state is not assigned, ignore those stats
        if state_name == "State Unassigned":
            continue
        # separating the districts from non significant details of state dictionary
        act = 0
        s_wise_dict = dict()
        for state_dict_keys, state_dict_vals in state_dict.items():
            # if the key is statecode, ignore the dictionary
            if state_dict_keys == "statecode":
                continue
            # final dictionary is the district names and their current stats
            for dist_name, dist_dict in state_dict_vals.items():
                # now exploring the district's current stats
                stat_dict = dict()
                for stat_name, stat_vals in dist_dict.items():
                    # if the keys are these, fetch the key:value pair
                    if stat_name == "active":
                        act = act + stat_vals
        # a separate dictionary for states and thier districts dictionary
        s_wise_dict["date"] = dt
        s_wise_dict["state"] = state_name
        s_wise_dict["cases"] = act
        final_list.append(s_wise_dict)
    # printing the filtered list of dictionaries
    print(final_list)
    put_in_csv(final_list)


# import csv package to perform csv read write functions
import csv
# defining the function which creates the CSV file and inserts the final dictinary into it
def put_in_csv(final_list):
    # setting keys:
    keys = final_list[0].keys()
    # opening the csv file
    with open('final_covid_stats.csv', 'w') as covid_csv:
        # writing the fields in the csv file
        dict_writer = csv.DictWriter(covid_csv, keys)
        # writing the header into csv
        dict_writer.writeheader()
        # writing the rows into csv file
        dict_writer.writerows(final_list)