# PySpark Tutorial - Learn to use Apache Spark with Python

PySpark Tutorial - Learn to use Apache Spark with Python — Big Data project.

## Overview
Apache Spark is a distributed processing engine that is open source and used for large data applications. For quick analytic queries against any quantity of data, it uses in-memory caching and efficient query execution. It offers code reuse across many workloads such as batch processing, interactive queries, real-time analytics, machine learning, and graph processing. It provides development APIs in Java, Scala, Python, and R.

PySpark is a Python interface for Apache Spark. It not only lets you develop Spark applications using Python APIs, but it also includes the PySpark shell for interactively examining data in a distributed context. PySpark supports most of Spark's capabilities, including Spark SQL, DataFrame, Streaming, MLlib, and Spark Core. In this project, you will learn about core Spark architecture, Spark Sessions, Transformation, Actions, and Optimization Techniques using PySpark.

## Data
The NYC yellow taxi trip records data will be used to implement this project. A Few of the fields from the dataset of 17 parameters include:
- VendorID
- tpep_pickup_datetime
- tpep_dropoff_datetime
- passenger_count
- trip_distance
- total_amount

_Data is not included in this repository._

## Tech stack
➔ Language: Python3 ➔ Library: PySpark ➔ Services: Juppyter Notebook

Key Takeaways
- Understanding the project overview
- Introduction to PySpark
- Understanding Spark Architecture and Lifecycle
- Introduction to Spark Operations
- Understanding Resilient Distributed Data (RDD)
- Implementing Spark Transformations
- Creation of Spark Dataframe
- Implementing Spark Actions
- Exploring Spark UI and Spark-Submit
- Hands-on PySpark use case
- Understanding Spark optimization Techniques

## How to run
Notebooks: [`CoalesceTransformation.ipynb`](Codes/jupyter_notebook/CoalesceTransformation.ipynb), [`DistinctTransformation.ipynb`](Codes/jupyter_notebook/DistinctTransformation.ipynb), [`FilterTransformation.ipynb`](Codes/jupyter_notebook/FilterTransformation.ipynb), [`IntersectionTransformation.ipynb`](Codes/jupyter_notebook/IntersectionTransformation.ipynb)

## Project structure
```
.gitignore
Codes/
  Readme.md
  jupyter_notebook/
    CoalesceTransformation.ipynb
    DistinctTransformation.ipynb
    FilterTransformation.ipynb
    IntersectionTransformation.ipynb
    MapTransformation.ipynb
    Spark-Action.ipynb
    SparkContext Instantiation.ipynb
    SparkSession Instatiation.ipynb
    UnionTransformation.ipynb
    Untitled.ipynb
    flatMapTransformation.ipynb
    reduceByKeyTransformation.ipynb
    repartitionTransformation.ipynb
    sparkRddAction.ipynb
  py-files/
    NYC-usecase.py
    coalesceTransformation.py
    distinctTransformation.py
    filterTransformation.py
    flatMapTransformation.py
    intersectionTransformation.py
    mapTransformation.py
    rddActions.py
    reduceByKeyTransformation.py
    repartitionTransformation.py
    spark-test.py
    unionTransformation.py
PySpark-ML-Use-Case-Logistic-Regression.ipynb
README.md
```

## Credits
Based on a ProjectPro guided project.
