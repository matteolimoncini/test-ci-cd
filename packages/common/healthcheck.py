# Databricks notebook source
# common - simple healthcheck task

print("Common healthcheck OK")
spark.sql("SELECT current_timestamp() AS checked_at").show(truncate=False)
