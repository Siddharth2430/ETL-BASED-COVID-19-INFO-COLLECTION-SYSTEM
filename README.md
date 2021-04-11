# ETL BASED COVID-19 INFO COLLECTION SYSTEM
A python application to fetch covid-19 everyday data and feed it into Google BigQuery Dataset Automatically Using Apache Airflow 

_To Run This Project_

# Clone or download this Repository

# Download And Install
* In order to successfully work on this project you need to install and setup working environment for these following softwares/technologies:
  + Python 3.0 Or above -> Install and setup the environment.
  + Apache Airflow 1.0 Or above 
  + Google Cloud Module for python using pip/pip3
  + Docker 19.0 Or above(Optional)
 
 # Google BigQuery
  + visit https://console.cloud.google.com/ 
  + In navigation menu, under products, in the BigData category select BigQuery
  + create your new project.
  + then create new dataset, then new table.
  + then after this again go to navigation menu -> IAM & Admin -> Service Accounts -> Create Service Account -> follow the process and choose to add new key.
  + after adding the key download the key and set its location into environment variable GOOGLE_APPLICATION_CREDENTIALS
 
 # Connecting All together
  + After Setting Environment for Python and Apache Airflow, search for a folder named dags at the same location of installation of airflow.
  + put the dag file into dags Folder: covid19_stats_dag.py
  + create your python project and put these files in the main folder at same location: fetchstats.py, uploadstats.py, finalstats.py
  # note: change the import statement in the dag file (covid19_stats_dag.py) as per your systems file location.
 
 # Getting the environment Ready(Linux)
  + After conecting all files together successfully.
  + start your terminal and set the environment variables:
    
      export AIRFLOW_HOME='Your_airflow_installation_location(same as dags folder)' airflow_home
 
  + follow these commads for google bigQuery Setup:
 
      export GOOGLE_CLOUD_PROJECT= "your_project_name"
 
      gcloud auth application-default login
 
      gcloud auth application-default set-quota-project your_project_name
 
      export GOOGLE_APPLICATION_CREDENTIALS= "Your_key_file_location_with_file_name"    
    
  # Starting the engines
   + after completeing the above steps. start two instances of terminal and navigate to the directory where dags folder is available
   + in one terminal follow these commands:
      
      airflow initdb
      
      airflow scheduler
      
   + in another terminal execute:
      
      airflow webserver
      
  # Supervising the process
    + airflow webserver will start a localhost server and will give a port on the terminal.
    + type localhot:port in web browser's address bar.
    + a UI will open from where you can turn your dag on and off and monitor and supervise the process. 
    
  # Documentations
    + https://airflow.apache.org/docs/stable/ - Apache airflow
    + https://docs.docker.com/develop/ - Docker
    + https://cloud.google.com/bigquery/docs - Google BigQuery
    + https://docs.python.org/3/ - Python
