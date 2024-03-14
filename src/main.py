from pyspark.sql import SparkSession
from pyspark.sql.functions import *

def main():
    spark = SparkSession.builder.appName("WeatherJ").getOrCreate()
    df = spark.read.load(
        'test_data/json/*.json',
        format = 'json',
        multiLine = True,
        schema=None
    )

    print(df.show())
    df.write.csv('test_data/csv', header=True, mode="overwrite")

if __name__=='__main__':
    main()
