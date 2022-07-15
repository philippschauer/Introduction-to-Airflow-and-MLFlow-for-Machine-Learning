# Introduction to Airflow and MLFlow for Machine Learning

Hi! In this short tutorial I would like to show you two awesome tools that help make your Machine Learning projects a lot more efficient and effective. If you read the title, you probably already know that those two tools are Airflow and MLFlow. However, you might not really know what they do. So, in order to give you a basic idea, let me give you two examples.


## Quick overview of MLFlow

### What is MLFlow?

MLFlow is an open-source tool that helps you during the entire life cycle of your Machine Learning process.

The quickest and easiest to implement way to use MLFlow is by tracking and record experiments. Imagine you try out a few models - maybe an XGBoost and a Neural Network - and test each of these with a few different parameters. It is very easy to forget which combination produced the best results. MLFlow though lets you store your models, together with parameters and relevant metrics so you can always go back and compare models. If you run your model over a longer period of time, this can also help you to detect model drift.

![an image of MLFlow's user interface](images/mlflow_ui.png)

But that's not all! You can also store your models to share with your colleagues.

Finally, MLFlow helps you to stage your models, deploy them or put them in production.


### Getting started with MLFlow

We are going to run everything python related in a conda environment. In case you don't know anaconda or haven't thought about using it, I can highly recommend [doing so](https://docs.anaconda.com/anaconda/install/). If you have ananconda installed create an environment, activate it and install mlflow with

```
conda create -n "airflow_mlflow" python=3.10

conda activate airflow_mlflow

pip install mlflow
````

You can obviously find a more creative name for the environment if you like. Easy right? Well that is almost everything you need to get started. To test it, you can run the sample file (stolen from the official documentation) *first_test.py*, then type *mlflow ui* in your terminal (the conda environment needs to be activated as well) and copy the link that is shown. In my case, I accessed the UI via *localhost:5000*.

By looking at the code, you can already see how it works. The metrics (things like accuracy) and parameters (things like number of neurons in a layer of your Neural Network) are stored in the respective columns. This shows quite well, how you can trace back which parameters gave you the best results. Finally, you can also store an artifact, in this case a simple *.txt* file.

*Note: Your runs and experiments are stored in the folder mlruns. In order to find those in the user interface, make sure you run **mlflow ui** in the directory **mlflow**.*

## Quick overview of Airflow

### What is Airflow?

The processes in every company can get pretty complicated so the workflows in your projects can become quite overwhelming. Whether it's loading the data from differenct sources, pre-processing it, training the model, passing necessary tests etc., most processes have to follow a strict order and not doing this might lead to bad results. To not lose track of these steps and to automate the entire pipeline, airbnb developed [Airflow](https://airflow.apache.org). 

In Airflow you design so-called directed acyclic graphs - or DAGs. These graphs describe the dependencies of each step in your project. For example, if you don't have the data, you cannot train your model or if you don't pass important tests, you cannot deploy it. Airflow allows you to design these DAGs in a way that the model won't be trained if the data import fails, similar to the deployment that is stopped if the tests fail. The big advantage of Airflow is that it simplifies these steps enourmously while having a useful interface.

Using CronJobs, you can schedule your pipelines on a regular basis, so you won't have to worry about this.


### Getting started with Airflow

There are a few different ways to get started with Airflow. In this quick tutorial we are going to use Airflow from a Docker container. First, you need to install [Docker](https://docs.docker.com/get-docker/) and docker-compose. The latter should be installed together with Docker. Airflow needs a few different components, so we need to get start the container with docker-compose instead of simply docker. However, the good news is that the Airflow community has created a **docker-compose.yaml**-file that comes in really handy. This file can be found in the folder **airflow** but if case you want the newest version, run the following commands in your project folder:

```
mkdir airflow

cd airflow

curl -Lf0 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml' > docker-compose.yaml
```

If you have some experience with Docker, you can go through the file and get familiar with the content. If not, no worries, I'll tell you what you need to do! 

In short, the first part describes how the Airflow part of the container is created, such as the location of the dags (a little bit more on that later) and the dependencies. Under **services** we define all the components that are part of the infrastructure. We mainly need a database (here we use postgres) and a communication service (which will be redis). In terms of Airflow-specific components, we need a scheduler which schedules our tasks and a webservice. The rest of the docker-compose makes our lives easier as well, the airflow-init part, for example, initializes the service. 

Now, we need to create the folders defined in line 63-65. Those are then mounted onto the container, so whatever content there is in these folders will be accessible inside the container as well. Inside the folder **airflow** run

```
mkdir dags logs plugins
```
You also need to set the permissions and save them in a file called **env** with the following command:

```
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOWGID=0" env
```

Okay, we are all set! That wasn't too hard, was it? Now, to initialize the airflow container, we need to run the

```
docker-compose up airflow-init
````

and wait a little bit. This command initializes Airflow with the user *airflow* and password *airflow*. If you want to use it in your company, this user is not recommended for obvious reasons. You can change this in lines 236 and 237 of the **docker-compose**. Then run

```
docker-compose up
````

which starts all the services defined in the docker-compose and your container should be up and running! You can access the webservice with the url "http://localhost/8080". Port 8080 is default for Airflow. If you want to use a different one, you can change it in lines 104 and 106.

*Note: One of the errors that you can run into is the WorkerLostError('Could not start worker processes',). I solved this by assigning more memory to the Docker container. This can be done in your Docker Desktop Application under Settings*



## Project Overview

Both of these tools are quite powerful, and explaining in detail what they can do would require more than one repository - a lot more. Instead, I would like to give you an overview of some of the most important features, so you can get started and implement these tools in your own project. Stay tuned!

