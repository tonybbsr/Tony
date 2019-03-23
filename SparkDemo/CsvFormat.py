
from pyspark.sql.types import DateType, TimestampType, IntegerType, FloatType, LongType, DoubleType
from pyspark.sql.types import StructType, StructField
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
sc = SparkContext('local')
spark = SparkSession(sc)

custom_schema = StructType([StructField('_c0', DateType(), True),
                            StructField('_c1', DateType(), True),
                            StructField('_c2', DoubleType(), True)])

df = spark.read.csv('I:/EMP.csv', header=True,
                    schema=custom_schema, sep=',')

print(df.count())

print(df.take(2))

