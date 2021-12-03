# Yelp Dataset Analysis
This repository contains my analysis of yelp data. 

## Setup
You can reproduce the results of this repository in two different ways.

### Using conda or pip
In case you want to use conda or pip environments, we provided the necessary `environment.yml` and `requirements.txt` respectively.

Please install via `conda env create --file envname.yml` or `pip install requirements.txt`.

Afterwards you can view start the jupyter notebook server via `jupyter notebook` and run the notebooks as you like on your localhost.


### Using the docker container
In case you want to use docker, you can use the attached docker file. When starting the docker container, it will start the jupyter notebook server inside the docker and attach it to your localhost:8888 port. Please make sure that this port is not in use by other applications. If necessary, you can adapt the port inside the docker file.

## Task description
I was asked to
* download the [yelp dataset](https://www.yelp.com/dataset/download)
* come up with one or more questions to answer around this dataset
* solve the task using Python or Scala
* make the code available via this Github repository 
* explain how to execute the code using docker.
* create a presentation of the results for a technical audience

