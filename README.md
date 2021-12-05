<style>
th{
  background-color: rgb(200,200,200);
  color: black;
  font-weight: bold;
  border: 1px solid white; 
  border-collapse: collapse;
}
td {
  background-color: rgb(220,220,220);
  color: black;
  font-weight: normal;
  border: 1px solid white;
  border-collapse: collapse;
}

table {
  width: 100%;
  table-layout: fixed;
}

table.ml-canvas td {
    vertical-align: top;
    border: 2px solid black;
}

</style>

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

- download the [yelp dataset](https://www.yelp.com/dataset/download)
- come up with one or more questions to answer around this dataset
- solve the task using Python or Scala
- make the code available via this Github repository
- explain how to execute the code using docker.
- create a presentation of the results for a technical audience

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

#### __Data Product Canvas__

<table>
    <tr>
      <th><b>BUSINESS CONTEXT</b></th>
      <th><b>BUSINESS GOALS</b></th>
      <th><b>DATA PRODUCT</b></th>
      <th><b>PROCESSING</b></th>
      <th><b>DATA</b></th>
    </tr>
    <tr>
      <td>
        Yelp elite squad is a program for members that are especially active. They are motivated to stay active and elite members by granting virtual badges and 
        being able to take part in special events with local businesses. However, the average elite member stays elite for `TODO` amount of days. Especially in areas where there are not many elite members it would be beneficial too keep these special members active to increase the value of the platform to businesses in these areas.
      </td>
      <td>
        The goal would be to detect 80% of churns accurately whilst having a maximum of 5% false positives (falsely identified as churn members). The prediction needs to be done at least 6 month in advance (so on 30th of June) to have enough time to react to churners until the end of the year.
      </td>
      <td>
        <ul>
          <li>Binary classification into churn and no churn based on the history of reviews a user made in the previous year.</li>
          <li>We provide the classification results as a batch list to the user satisfaction team.</li>
        </ul>
      </td>
      <td>
        Processing happens once a year. Potentially more often, if we can predict further into the future.
      </td>
      <td>
        <ul>
          <li>User data</li>
          <li>reviews</li>
          <li>(+ maybe pictures for V2.0)</li>
        </ul>
      </td>
    </tr>
    <tr>
      <th><b>USER GROUPS</b></th>
      <th><b>USER PAINT POINTS</b></th>
      <th><b>INTERFACE</b></th>
      <th><b>ETHICS</b></th>
      <th><b>LEGAL</b></th>
    </tr>
    <tr>
      <td>User Satisfaction Team Members</td>
      <td>
        <ul>
          <li>They don't know which users might become inactive</li>
          <li>They want to spend the money for incentives the most efficient way</li>
          <li>They are responsible for keeping elite members active, but lack the information mentioned above</li>
        </ul>
      </td>
      <td>
        Batch File once a year or more often if required. (maybe monthly?)
      </td>
      <td>
        No ethical issues involved
      </td>
      <td>
        No legal issues involved, as users agreed to DSE.
        We need to exclude users that have asked for deletion of data or did not accept the DSE. In that case, they are not part of this dataset, so we can continue on normally.
      </td>
    </tr>
</table>

#### __Machine Learning Canvas__
<table class="ml-canvas">
  <tr>
    <td><b>PREDICTION TASK</b>
      <br/>Binary Classification to predict if an existing elite customer churns (i.e. becomes inactive / non-elite) or stays elite member.
      Is partially based on time-series data, which could either be flattened or fed into a respective time-series model (i.e. RNN) and flattened afterwards.
    </td>
    <td><b>DECISIONS</b>
      <br/>All elite users will be filtered to those that are likely to churn.
    </td>
    <td rowspan="2"><b>VALUE PROPOSITION</b>
      <br/>Those users that are likely to churn will be contacted by the user satisfication team with e-mail offers and the like. This requires an interface to the e-mail sending system to send the mails without user interference.
    </td>
    <td><b>DATA COLLECTION</b>
      <br/>The ML model can be based on the existing review data and the data of the users. As we already collect this data, a constant retraining is possible.
    </td>
    <td><b>DATA SOURCES</b>
      <br/>Reviews and User data tables.
    </td>
  </tr>
  <tr>
    <td rowspan="2"><b>IMPACT SIMULATION</b>
      <br/>The costs of incorrect decisions are neglectable. However, it is more important to identify all churners than it is to avoid false positives.
    </td>
    <td><b>MAKING PREDICTIONS</b>
      <br/>We make batch predictions and have virtually no time limit to do so. All necessary features can therefore be calculated on the fly from the base data tables.
    </td>
    <td><b>BUILDING MODELS</b>
      <br/>One model is required. As we only know until next year if our predictions are correct, retraining once a year should be sufficient. There is virtually no time-limit for this task.
    </td>
    <td rowspan="2"><b>FEATURES</b>
      <ul>
        <li>history of user reviews</li>
        <li>length of individual reviews</li>
        <li>received feedback for reviews</li>  
        <li>pictures uploaded by user</li>
        <li>frequency of reviews per month</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td colspan="3"><b>MONITORING</b>
      <br/>We should measure the amount of churns we prevented by gathering direct user feedback on whether they thought about quitting in the past. 
    </td>
  </tr>
</table>

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
