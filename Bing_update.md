# 7 May Update

## Spark

Is there any possibility to use spark for data preprocessing e.g. PySpark.

## Containers

Do we have to use docker SWARM to create containers other than couchDB?

## Data

Check the data, we have 3,226,685 twitts have place can be matched to sal.json file. Expected more less twitts can be matched to sal.json file. So far, 160+ MB if I only store place and user_id, will be much larger if store something like text.

We need to:

- come up with our story, then preprocess the data.
- make the data into couchDB.
- come up with way to analysis data, how to come up with dictionary to determine which data need to process. Also, come up with ways to deal with 'special case', e.g., "I don't like XXX" where XXX is in our key dictionary and we want to do analysis on people like XXX. (Above senario might be done by unsupervised NLP, but the algorithm might take a very long time to train or even to predict on large dataset) OR we can simply make a very general assumption on that.
- come up with tools to analysis data, e.g., spark, etc,.

## Front End

I guess our front end is just a dashboard (interactive) on the data given that we only work on static data. Hence, we can use python Streamlit or something like D3.js 

### Front End Update No. 2

I upload a docker file from to show the possibility to wrape front end and back end in one python script (https://docs.streamlit.io/knowledge-base/tutorials/deploy/docker)

I consider this python package is much easier to use than Node.js

However, we need to figure if not Python not allowing stream read from couchDB, will we still be able to use the Python as backend.


# 6 May Update

## CouchDB

Can setup clusters on docker containers on different instances.






# 5 May Update

## CouchDB

Still cannot figure out how to make clusters of three couchDB on three different instances. However, thats might not be the solution we looking for.

I managed to launch couchDB cluster on single instance, and Luca suggest thats the better option.

## Ansible

I need to change the code to make sure the instance it created is equiped with jq. 

Also need to figure way to create instance with couchDB cluster configured.

## Todo 

Figure way to process the data. Luca mentioned that python does not allow stream with couchDB, he suggest Node.js






# 4 May Update

## Instances

Few (probably more than one) servers (instances) is needed to be created, either manually or through Ansible. (which I know how)

## Ansible (check)

Main use of Ansible is to install prerequest in the server as Richard we don't need dynamically change the number of instances for this assignment

## Twitter Data

Which is a json file. I've downloaded it and play it with python. The format is slightly different from Assignment 1 but mostly similar.

We need to upload this data to instance volumn. Sit in single instance is best idea mentioned by Luca.

Just wondering is scp good idea to upload the dataset to cloud?

## Mastodon Data & SUDO Data

Haven't reached this point yet, but I beleive its fine to download target data to instance and see it as static (mentioned on ED)

## Docker

Build containers for different part of the applications (which I was working on and have progress).

Need to use Docker SWARN if more than one instance is used.

## CouchDB (check?)

Haven't reached this point so far. However Week 7 workshop has demo 3 working on SQL, Week 8 workshop work on CouchDB which I'll go through today.

## Scale

Not quiet understand what Richard means scalable. Since we do not need dynamic number of instance, how do we show our application is scalable?

Is that through Ansible file? By setup new instance automically, which means our application can have more instances used if we want? But under which situation we will want more? Bigger data set will only need more volume attached to instance, and having more instance didn't necessarily means our application can run parallel... 

Or is that we use Ansible to set up system and Docker to show we can use such tool to set up new container have new function if we want? But in this case, how we present this in our work?

More info on ED on this topic, Richard mentioned using Ansible to create instance can be one aspect to show scalable.