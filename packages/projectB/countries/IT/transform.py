# Databricks notebook source
# projectB IT - sample transform task

from pyspark.sql import functions as F

df = spark.table("main.default.projectb_it_raw")
result = df.withColumn("name_upper", F.upper(F.col("name")))
result.write.mode("overwrite").saveAsTable("main.default.projectb_it_curated")

print(f"Wrote {result.count()} rows into main.default.projectb_it_curated")
