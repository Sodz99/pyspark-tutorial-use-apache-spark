from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('coalesceTransformation').getOrCreate()
sc = spark.sparkContext
rdd = sc.parallelize([1, 2, 3, 4, 5])
filterRDD = rdd.filter(lambda x: x % 2 == 0)
filterRDD.collect()