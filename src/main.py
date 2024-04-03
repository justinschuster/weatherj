from pyspark.sql import SparkSession
from pyspark.sql.functions import *

import api

test_urls = [
    'https://api.weather.gov/gridpoints/OKX/33,35/forecast',
    'https://api.weather.gov/gridpoints/LWX/96,70/forecast'
]

def main():
    for i in test_urls:
        data = api.get_weather(i)
        api.write_to_json_file(data, i)
 
    spark = SparkSession.builder.appName("WeatherJ").getOrCreate()
    df = spark.read.load(
        'src/test_data/json/*.json',
        format = 'json',
        multiLine = True,
        schema=None
    )

    print(df.show())
    df.write.csv('src/test_data/csv', header=True, mode="overwrite")

if __name__=='__main__':
    main()
