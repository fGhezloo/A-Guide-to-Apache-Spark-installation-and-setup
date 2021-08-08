# kafka-spark-cassandra

Everything you need to know about Apache Kafka, Apache Spark and Apache Cassandra.

## Installation on Ubuntu 18.04

First, You need to have Java and Scala installed on your machine!

* For installing version 8 of **Java**: 

```$ apt install openjdk-8-jre-headless```

* For intalling **Scala**:  

```$ sudo apt-get remove scala-library scala```

```$ sudo wget www.scala-lang.org/files/archive/scala-2.11.8.deb```
 
```$ sudo dpkg -i scala-2.11.8.deb```

Also, install **SBT (Scala Build tool)** referring [here](https://www.scala-sbt.org/download.html).

### Install Apache Kafka

Follow instructions [here](https://tecadmin.net/install-apache-kafka-ubuntu/).

### Install Apache Spark

Apache Spark supports three most powerful programming languages: Scala, Java, Python.

Here we cover everything for Python.

The shell for python is known as **PySpark**.

* For installing **Pyspark** download the latest version from [here](https://spark.apache.org/downloads.html) and after extracting it, add the following lines to **.bashrc file**: (instructions for spark-2.4.0)

```
export SPARK_HOME = /home/hadoop/spark-2.4.0-bin-hadoop2.7
export PATH = $PATH:/home/hadoop/spark-2.4.0-bin-hadoop2.7/bin
export PYTHONPATH = $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.4-src.zip:$PYTHONPATH
export PATH = $SPARK_HOME/python:$PATH
```
Then run the following command for the environments to work:
```$ source .bashrc```

You can launch **Pyspark** by typing:
```$ ./bin/pyspark```



### Install Apache Cassandra

Follow instructions [here](https://www.liquidweb.com/kb/install-cassandra-ubuntu-16-04-lts/).

## Spark Fundamentals

In order to understand this project you need to be familiar with several concepts:
* Spark RDD
* Spark RDD Operations
    - Transformations
    - Actions

[Here](https://data-flair.training/blogs/spark-rdd-tutorial/) is a good tutorial. Read if necessary.

You may also find sample codes in pysparkCommands.py and pysparkCommands2.py


## Spark Cluster

**Glossary:**

* **Application :** 	User program built on Spark. Consists of a driver program and executors on the cluster.
* **Driver program :** 	The process running the main() function of the application and creating the SparkContext.
* **Cluster manager :**	An external service for acquiring resources on the cluster (e.g. standalone manager, Mesos, YARN).
* **Worker node :** 	Any node that can run application code in the cluster.
* **Executor :** 	A process launched for an application on a worker node, that runs tasks and keeps data in memory or disk storage across them. Each application has its own executors.
* **Task :** 	A unit of work that will be sent to one executor

To Set up a **standalone manager** do the followings:

* Install **Java** and **Spark** on all machines.
* Set spark directory location: ```export SPARK_HOME=/Path/To/Spark```
* On **host** machine cd to the **sbin** folder of spark and to start a master run: ```./start-master.sh -h <Host machine IP Adress>```
* On each **guest** machine cd to the **sbin** folder of spark and to start a slave run: ```./start-slave.sh <Spark master URL>```
* To run an application, cd to the folder containing the .py file on your host machine and run: ```spark-submit <yourPythonCode.py>```

You can track spark cluster details by visiting master’s web UI (http://localhost:8080 by default).

## Spark on Docker

* First, make sure you have docker installed on your machine and then load your docker image by: ```sudo docker load --input <your-docker-image>```. You do this step just once.
* Second, edit docker-compose.yml to start spark master and as many slaves as you want then run: ```sudo docker-compose up```
* Third, run ```sudo docker run -it -p 4544:4544 -p 8088:8088 -p 8042:8042 -p 4041:4040 --rm --name driver --link ocr1 --link ocr2 -v ~/Desktop/data:/var2/ driver pfk-spark-final5 bash``` to start docker along driver and jupyter.
* To start a docker bash run: ```sudo docker exec -it driver bash```
* Finally, to run your code: ```spark-submit /Path/To/Pythonfile.py```

Keep in mind that you need to edit ocr IP addresses in your python code each time you run your docker compose. To find out their IP run: ```vim /etc/hosts```.
You can check out workers progress by visiting master’s web UI (http://localhost:8080 by default).