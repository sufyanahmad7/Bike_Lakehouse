# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# MAGIC %md
# MAGIC # Read file from CSV.

# COMMAND ----------

df = (
    spark.read.option("header", "true")
    .option("inferSchema", "true")
    .csv("/Volumes/workspace/bronze/source_data/source_crm/sales_details.csv")
)

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC # Write to Bronze layer.

# COMMAND ----------

df.write.mode("overwrite").saveAsTable("workspace.bronze.crm_cust_info")

# COMMAND ----------

# MAGIC %md
# MAGIC # Check if write was successful.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM workspace.bronze.crm_cust_info LIMIT 10

# COMMAND ----------

# MAGIC %md
# MAGIC # Initialization

# COMMAND ----------


import bronze_config

# import importlib
# importlib.reload(add file name here if need to reload)

INGESTION_CONFIG = bronze_config.INGESTION_CONFIG

# COMMAND ----------

# MAGIC %md
# MAGIC # Read from CSV and write to Bronze?

# COMMAND ----------

for item in INGESTION_CONFIG:
    print(f"Ingesting {item["source"]} to bronze.{item["table"]}")
    
    df = (
        spark.read
        .option("header", "true")
        .option("inferSchema", "true")
        .csv(item["path"])
    )

    (
        df.write
        .mode("overwrite")
        .format("delta")
        .saveAsTable(f"bronze.{item["table"]}"
    )

    )

# COMMAND ----------

# %sql
# USE CATALOG workspace;
# USE SCHEMA bronze;

# COMMAND ----------

# MAGIC %md
# MAGIC