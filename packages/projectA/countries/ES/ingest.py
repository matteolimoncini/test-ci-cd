# Databricks notebook source
# projectA - sample ingest task

df = spark.createDataFrame(
    [(1, "alice"), (2, "bob"), (3, "carol")],
    ["id", "name"],
)

df.write.mode("overwrite").saveAsTable("main.default.projecta_raw")

print(f"Ingested {df.count()} rows into main.default.projecta_raw")
