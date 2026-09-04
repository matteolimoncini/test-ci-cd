# Databricks notebook source
# projectA - sample transform task

from pyspark.sql import functions as F

df = spark.table("main.default.projecta_raw")

result = df.withColumn("name_upper", F.upper(F.col("name")))

result.write.mode("overwrite").saveAsTable("main.default.projecta_curated")

print(f"Wrote {result.count()} rows into main.default.projecta_curated")
