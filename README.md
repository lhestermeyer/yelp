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

### Caveats
I ran this task on a laptop with 16 GB of RAM. I don't know, whether it would work on lower scaled machines. This problem could be solved using pyspark and its related packages and relying more on file-based data (see [here](https://databricks.com/de/glossary/pyspark) for more information).

## Task description
I was asked to
* download the [yelp dataset](https://www.yelp.com/dataset/download)
* come up with one or more questions to answer around this dataset
* solve the task using Python or Scala
* make the code available via this Github repository 
* explain how to execute the code using docker.
* create a presentation of the results for a technical audience

## Business background
<div class='alert alert-warning'>TODO: put this into the notebook.</div>

Yelp is a social media and rating platform provider, that allows users to rate and search for businesses all around the world. That way users can find highly valued restaurants and the like more easily. Addtionally, users get personalized recommendations based on their searches.

Yelp earns most of its revenue via ads. Businesses are able to purchase higher ranked ads to appear first for certain searches on yelp (similarly to Google ads). Yelp uses machine learning to predict the click-through-rate (CTR) and success rate of each ad in order to maximize the return on investment for businesses purchasing ads and thereby reducing cost per click and marketing costs in general.

Obviously, Yelp is totally depending on its active community. To keep the community alive, the Yelp Elite Squad targets very active users, to motivate them to keep posting reviews. Members of the Yelp Elite Squad receive virtual badges and may attend exclusive behind the scenes events of local businesses. Often times these include the business owners who share their unique story.

## Use Case ideas
To allow for some sort of realism in this task, we act as if we are working for Yelp and try to optimize their revenue either directly or indirectly.

Due to time limitations we will only work on one of the tasks, but here are a few ideas that could be taken a look at.

### 1. Elite user churn prediction
Elite users are the ones that have a big influence on the overall reviews and their helpfulness. Thus, Yelp is interested in keeping these kind of members active. One idea would be to analyze what makes elite users churn the program and if we are able to predict churn. If so, Yelp might reactivate the users with an incentive (i.e. some elite event or similar).

### 2. Business rating prediction based on photos and meta-data
If new businesses open up, it would be very helpful to know what kind of interior and exterior design they would have to choose that helps increase their rating. If we are able to find drivers of rating in pictures and metadata, we might offer helpful insights to new businesses, how to optimize their rating by design choices.

### 3. Friend Recommender to community members based on writing style and similar interests
The older we get, the harder it gets to make new friends. As friends tend to like similar things and have similar intellects and phrases they use, we might be able to help our fellow users in connecting with like-minded peers in their close neighborhood. 
If we succeed, Yelp users have more incentives to use the platform and writing reviews actively, as it will lead to more fitting friend recommendations. Plus, it would incentivize users to write more natural reviews, making fake reviews stand out a bit more.

### 4. Recommender for businesses (NBO)
Classic use case: Recommend businesses to a user, which he/she might like based on his/her ratings and reviews and those of similar users.
TODO: Write longer, but I cannot be bothered.

### 5. Predict business category labels
This was the original Yelp dataset challenge. I will not go into detail here, as there are many solutions available on the internet for this problem.

### 6. Find out what makes good business bad and bad business good over time.
Maybe there are events (i.e. pictures or changes to metadata), that explain why businesses drop in rating. As the dataset is not available in historized format, this use case idea will not work as well as it could, as we dont have changes to metadata available, but only a snapshot).