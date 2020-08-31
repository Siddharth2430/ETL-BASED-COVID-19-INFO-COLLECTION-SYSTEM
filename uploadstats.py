# importing pandas for dataframe
import pandas as pd
# importing google authorization package to authorize the BQ coonection
import google.auth

# setting the credentials to default
credentials, project_id = google.auth.default()
# defing the function which will read the csv file and upload it in G-BQ
def upload_stats():
    # setting the csv file path to variable
    fpath = "file_path/final_covid_stats.csv"
    # creating dataframe by reading csv file through pandas
    covid_data = pd.read_csv(fpath)
    # uploading data to respective projectid.dataset.table and replacing each time
    covid_data.to_gbq(destination_table='dataset.table', project_id='project_id', if_exists='append')
