from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, coalesce

spark = SparkSession.builder.appName("ProductCategory").getOrCreate()

products = spark.createDataFrame([(1, "Product A"), (2, "Product B"), (3, "Product C")], ["ProductID", "ProductName"])
categories = spark.createDataFrame([(1, "Category X"), (2, "Category Y")], ["CategoryID", "CategoryName"])

product_category = spark.createDataFrame([(1, [1, 2]), (2, [2]), (3, [])], ["ProductID", "CategoryID"])

exploded_category = product_category.select("ProductID", explode("CategoryID").alias("CategoryID"))

result_df = products.join(exploded_category, products.ProductID == exploded_category.ProductID, "left_outer")

result_df = result_df.select("ProductName", "CategoryName")
result_df = result_df.withColumn("CategoryName", coalesce(result_df["CategoryName"], "Без категории"))

result_df.show()
