# Databricks notebook source
# projectB (shared) - sample ingest task

df = spark.createDataFrame(
    [(1, "alice"), (2, "bob"), (3, "carol")],
    ["id", "name"],
)

df.write.mode("overwrite").saveAsTable("main.default.projectb_shared_raw")

print(f"Ingested {df.count()} rows into main.default.projectb_shared_raw")
