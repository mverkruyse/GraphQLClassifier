# GraphQLClassifier
An end-to-end microservice using GraphQL

This repository provides everything needed to launch a microservice on a cloud environment, that can be called using GraphQL. 

There are two folders in this repo:

1) Microservice, which contains the underlying microservice code (written in Python)
2) GraphQL, which contains the code needed to call the microserivce (written in GraphQL and Javascript)

I launched the microservice with an AWS EC2 instance, and the instructions will be written with that in mind.

Instructions:

1) Create an EC2 instance (in my case a free-tier t2.micro: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html#ec2-get-started-overview).

2) ssh into your EC2 instance using AWS CLI (https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html).

3) Follow the instructions in the provided article to install ngnix and gunicorn to host your flask app (https://chrisdtran.com/2017/deploy-flask-on-ec2/).

4) scp the files from the "microservice" folder in this repo to your EC2 environment (note, you might need to sudo chmod the folder to add write permissions depending on your environment setup).

5) Install the required python packages (sudo pip install -r --no-cache-dir requirements.txt). Note that you might need to "apt-get" pip if it is not already installed in your environment. Further note that you need the --no-cache-dir flag for pip since scipy is >50MB, and otherwise pip will fail to install it with an "out of memory" error.

6) Launch your flask server using gunicorn (in my case: gunicorn application:application).

7) Check to verify that the microservice is working by typing your "Public DNS (IPv4)" or "IPv4 Public IP" address into your browser (if you get to a page saying "This microservice is working! Congrats on launching!" then it is working, if not then go troublshoot your EC2 environment for errors).

8) Navigate to Apollo GraphQL Platform (https://launchpad.graphql.com/).

9) Create a new secret with a Key/Value of: "Key = EC2, Value = YOUR PUBLIC DNS (IPv4)" (Example of YOUR PUBLIC DNS (IPv4) would be 52.XX.XXX.XXX, do not include "http://" before the DNS).

10) Paste the code from the GraphQL folder into the browser editor (left-hand side).

11) Test the code by entering a valid GraphQL query. For example:


{
  incident(type: USERINPUT, description:"A driver died after being involved in a single vehicle rollover on an S-bend, resulting in the fatality of the driver at the scene") {
    id
    description
    severity {
      id
      naive_bayes_classification
      naive_bayes_classification_confidence
      naive_bayes_optimized_classification
      naive_bayes_optimized_classification_confidence
      naive_bayes_optimized_classification_all_results
      classification_categories
    }
    location {
      id
      region
    }
  }
}

Should return a classification of your custom user-input, along with some classification details

{
  incident(type: IOGPHIPO, pageLink: "2675") {
    description
    severity {
      naive_bayes_optimized_classification
    }
  }
}

Should return a classification of http://safetyzone.iogp.org/HighPotentialEvents/detail.asp?inc_id=2675

{
  incident(type: IOGPFATAL, pageLink: "8348") {
    description
    severity {
			naive_bayes_classification
      naive_bayes_classification_confidence
      naive_bayes_optimized_classification
      naive_bayes_classification_confidence
      naive_bayes_optimized_classification_all_results
    }
  }
}

Should return a classification of http://safetyzone.iogp.org/FatalIncidents/detail.asp?inc_id=8348
