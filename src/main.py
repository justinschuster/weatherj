from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import StringType, TimestampType, StructType, StructField, BooleanType, IntegerType, DoubleType

import api

test_urls = [
    'https://api.weather.gov/gridpoints/OKX/33,35/forecast',
    'https://api.weather.gov/gridpoints/LWX/96,70/forecast'
]

hourly_forecast_schema = StructType(
    [
        StructField("startTime", TimestampType(), True),
        StructField("endTime", TimestampType(), True),
        StructField("isDaytime", BooleanType(), True),
        StructField("temperature", IntegerType(), True),
        StructField("temperatureUnit", StringType(), True),
        StructField("probailityOfPrecipiation", IntegerType(), True),
        StructField("dewpoint", DoubleType(), True),
        StructField("relativeHumidity", IntegerType(), True),
        # wind speed lower limit
        # wind speed upper limit
        StructField("windDirection", StringType(), True),
        StructField("shortForecast", StringType(), True),
        StructField("detailedForecast", StringType(), True)
    ]
)

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
