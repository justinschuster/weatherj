import requests
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

if __name__=='__main__':
    spark = SparkSession.builder.appName("WeatherJ").getOrCreate()

    df = spark.read.load(
        'test_data/example.json',
        format = 'json',
        multiLine = True,
        schema=None
    )

    #print(df.select(avg('temperature')).show())
    print(df.show())
