# Sliide ETL Test 2020

by Thomas Korrison

## Getting Started

`git clone https://github.com/TKorr/sliide_test_2019.git`

`cd sliide_test_2019/`

`python3 setup.py install`

`run_sliide_etl`

## Running Tests

`python3 setup.py test`

## Run with Docker

create tarball

`python setup.py sdist`

build image from dockerfile

`docker build . -t sliide_test_image`

run command from container

`docker run sliide_test_image sliide_etl `

## Further Questions
1. How would you design the ETL process for it to automatically update daily?

    Use Apache Airflow and schedule and run docker container daily.
    
    or
    
    Use a crontab to schedule job in an EC2 instance.

2. How would you scale this process if we got tens or hundreds of millions of events per
day?

    The implementation I have will read one line at a time so there won't be any memory problems
    but may be time consuming. 
    
    If the job is too slow to run sequentially, we can process the data in chunks. 
    
    If it is still too slow, we can run it in parallel as the data is organised into 
    lines of records, an apache spark job running over a cluster would split the records across
    multiple machines

3. Suggest any target architecture to cater for this growth.

   Apache Airflow as an orchestrator to schedule jobs.
   AWS EMR / GCP DataPROC to run Apache spark jobs.