# Data Warehouse Million Song Dataset JSON -> AWS RedShift
In this project, we will acreate a data warehouse by using AWS and build an ETL pipeline for a database hosted on Redshift.

We will need to load data from S3 to staging tables on Redshift and execute SQL statements that create the analytics tables from these staging tables. This is a rework using only code to create a redshift cluster, IAM role and load the tables.

# Introduction
A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

As their data engineer, you are tasked with building an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to. You’ll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

# Design Decisions

Utilized psql COPY comand to quickly load data into staging tables. Example from staging_events:

``COPY staging_events 
FROM 's3://udacity-dend/log_data'
IAM_ROLE 'DWH_IAM_ROLE_NAME'
REGION 'us-west-2' compupdate off 
JSON 's3://udacity-dend/log_json_path.json';``

# Dimensional Model & ETL
Data is extracted from staging tables and inserted into the dimensional model shown below.

![alt text](dimensional_model.png)

# Files 

1. environment.yml
* Anaconda yaml file to reproduce execution environment. Load this environment when running python scripts.
2. dimensional_model.er & stage_schema.er
* Entity-relationship files used to generate ER diagram images
3. create_redshift_cluster_database.py
* Create AWS RedShift cluster & create sparkify db
4. sql_queries.py
* DROP, CREATE, INSERT, COPY statements for all sparkify db objects
5. create_tables.py
* CREATE and DROP all required tables in sql_queries.py
6. etl.py
* ETL cordinator to run INSERT & COPY SQL scripts in sql_queries.py
7. cleanup_cluster.py
* Remove RedShift AWS cluster as well as created IAM role
8. dwh.cfg
* Config file for all necessary variables for AWS RedShift, sparkify db, IAM role, and S3 buckets

Create Anaconda environment using given environment.yml file:

``` python 
conda env create -f environment.yml
```
It will create an environment called million-song-redshift. Activate that environment once created:
```python
conda activate million-song-redshift
```
Ensure variables are set up in dwh.cfg as described in installation above.

Create RedShift IAM role, cluster, and database:
```python
python create_redshift_cluster_database.py
```
Create tables in sparkify db:
```python
python create_tables.py
```
Load data into staging and onto the dimensional model:
```python
python etl.py
```
Once finished, delete cluster and IAM role:
```python
python cleanup_cluster.py
```