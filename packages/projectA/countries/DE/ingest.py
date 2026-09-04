# Databricks notebook source
# projectA DE - sample ingest task

df = spark.createDataFrame(
    [(1, "anna"), (2, "bernd"), (3, "clara")],
    ["id", "name"],
)

df.write.mode("overwrite").saveAsTable("main.default.projecta_de_raw")

print(f"Ingested {df.count()} rows into main.default.projecta_de_raw")
