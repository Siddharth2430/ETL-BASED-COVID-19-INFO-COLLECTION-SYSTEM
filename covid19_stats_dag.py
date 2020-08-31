# import for datetime functions
from datetime import timedelta

# import for airflow components
from airflow.utils.dates import days_ago
from airflow import DAG
# from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

# import the methods to perform fetch and feed functions
# import to make the other directories accessible at dag's location
# import sys
# # append the path of previous directory so that all the directories alongside of the dags directory are visible for a
# # dag file in dags directory
# sys.path.append('../')

# import for the method which fetches the daily stats and feeds that data in a csv file at same location
from fetchstats import fetch_stats
# import for the method which which retrieves the data from csv file and uploads it to the BigQuery Dataset
from uploadstats import upload_stats
# import for the method which gets the data from the Bigquery DataSet and compares it from the rows of csv file and
# prints the upload percentage of the day
from finalstats import final_stats

# define default arguments
default_args = {
	'owner': 'siddharth',
	'start_date': days_ago(4),
    'depends_on_past': False,
    'retries': 1,
    # 'email':['worldhacker2430@gmail.com'],
    # 'email_on_success':True,
    'retry_delay': timedelta(minutes=10)
}
# define the DAG
dag = DAG(
'covid19_stats_dag',
default_args=default_args,
description='gets covid19 statewise stats and feeds in csv and G-BigQuery',
# Continue to run DAG once per day
schedule_interval=timedelta(days=1)
)

# defining the tasks which will be scheduled by the DAG defined above and will be responsible for the respective tasks
# which they will performed as assigned
# this task fetches the stats
t1 = PythonOperator(
    task_id='f_stats',
    python_callable=fetch_stats,
	dag=dag,
)

# this task uploads the stats
t2 = PythonOperator(
    task_id='up_stats',
    python_callable=upload_stats,
    dag=dag,
)

#this task shows the upload percentage
t3 = PythonOperator(
    task_id='upload_percentage',
    python_callable=final_stats,
    dag=dag,
)

t1 >> t2
t2 >> t3
