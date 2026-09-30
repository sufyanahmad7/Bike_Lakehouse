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

# Show first 10 rows without truncating columns
df.show(10, truncate=False)

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
# MAGIC SELECT
# MAGIC   *
# MAGIC FROM
# MAGIC   workspace.bronze.crm_cust_info
# MAGIC LIMIT 10

# COMMAND ----------

# MAGIC %md
# MAGIC # Initialization

# COMMAND ----------

# import importlib
import bronze_config

# Created a new bronze_config file to replace the old one.
# It did not load properly. Hence, the code below.
# importlib.reload(bronze_config)

INGESTION_CONFIG = bronze_config.INGESTION_CONFIG

# COMMAND ----------

# MAGIC %sql
# MAGIC USE CATALOG workspace;
# MAGIC USE SCHEMA bronze;

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



# COMMAND ----------

# MAGIC %md
# MAGIC