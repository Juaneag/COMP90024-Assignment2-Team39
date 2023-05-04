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

## CouchDB

Haven't reached this point so far. However Week 7 workshop has demo 3 working on SQL, Week 8 workshop work on CouchDB which I'll go through today.

## Scale

Not quiet understand what Richard means scalable. Since we do not need dynamic number of instance, how do we show our application is scalable?

Is that through Ansible file? By setup new instance automically, which means our application can have more instances used if we want? But under which situation we will want more? Bigger data set will only need more volume attached to instance, and having more instance didn't necessarily means our application can run parallel... 

Or is that we use Ansible to set up system and Docker to show we can use such tool to set up new container have new function if we want? But in this case, how we present this in our work?