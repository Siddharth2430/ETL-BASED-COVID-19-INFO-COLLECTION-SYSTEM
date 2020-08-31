# importing bigquery to access dataset
from google.cloud import bigquery
# importing auth packages for service account authentification
from google.oauth2 import service_account
# importing csv packages
import csv

# setting the auth variables
credentials = service_account.Credentials.from_service_account_file('key_file_location/key_file.json')
project_id = 'project_id'

# initiating the client
client = bigquery.Client(credentials = credentials, project = project_id)

# declaring count for csv and BQ
csv_count = 0
BQ_count = 0
# declaring date variable
date = ""
# defining the function which gets the final data from bq and compares with csv file
def final_stats():
    # Reading csv for confirmation
    with open('final_covid_stats.csv', 'r') as file:
        reader = csv.reader(file)
        csv_count = 0
        for row in reader:
            csv_count += 1
        csv_count -= 1
        date = row[0]
    # Reading BQ data for comparison
    SQL = client.query("""SELECT * FROM `project_id.dataset.table` where date = '"""+date+"""'""")
    result = SQL.result()
    BQ_count = int(result.total_rows)
    # Calculating the Upload Percentage
    per = int(BQ_count) * 100 / int(csv_count)
    print("Today's Total Upload Percentage is = "+str(per)+"%")
