from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('coalesceTransformation').getOrCreate()
sc = spark.sparkContext
rdd = sc.parallelize([("a", 1), ("b", 1), ("a", 1)])
from operator import add
sorted(rdd.reduceByKey(add).collect())