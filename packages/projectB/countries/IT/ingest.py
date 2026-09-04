# Databricks notebook source
# projectB IT - sample ingest task

df = spark.createDataFrame(
    [(1, "alessia"), (2, "bruno"), (3, "chiara")],
    ["id", "name"],
)

df.write.mode("overwrite").saveAsTable("main.default.projectb_it_raw")

print(f"Ingested {df.count()} rows into main.default.projectb_it_raw")
