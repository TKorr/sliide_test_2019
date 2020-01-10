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
