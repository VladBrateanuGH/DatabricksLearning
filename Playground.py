# Databricks notebook source
query = "SELECT 'test' AS COL1"
df = spark.sql(query)
display(df)

# COMMAND ----------


