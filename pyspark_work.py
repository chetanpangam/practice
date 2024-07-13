from pyspark import SparkContext
from pyspark.sql import SparkSession

# Initialize SparkContext
sc = SparkContext("local", "PySpark Example")

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("PySpark Example") \
    .getOrCreate()

# Create an RDD
data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)

# Perform a simple transformation and action
squared_rdd = rdd.map(lambda x: x * x)
squared_data = squared_rdd.collect()
print(squared_data)  # Output: [1, 4, 9, 16, 25]


# Create a DataFrame from a list of tuples
data = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)

# Show the DataFrame
df.show()

# Perform SQL operations
df.createOrReplaceTempView("people")
result = spark.sql("SELECT * FROM people WHERE Age > 1")
result.show()
