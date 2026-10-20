# Bike_Lakehouse

## :book: Introduction
I self-learned Databricks through Youtube videos and proceeded to work on an end-to-end data engineering project with Databricks using the Medallion Architecture with the 3 layers - bronze, silver and gold. It is still a work in daily progress. In the meantime, please refer to the architecture below.

## 📊 Business Goals
1. What is the top selling product?
2. What is the lowest selling product?
3. Which customer group (segmented by gender, marital status and country) spent the most?

## :computer: Tech Stack
Everything was done on Databricks.

## :white_check_mark: Key Features (App Ready)
1. End-to-end data ingestion and processing using Medallion architecture with the 3 layers - bronze, silver and gold.
2. Data model with star schema >>> 1 fact file + 2 dimension files in gold layer.
3. Data orchestration using jobs (daily run).
4. Visualizations (coming soon).
5. Forecasting (maybe?).

## :bowtie: Reflections
- Databricks is platform that pulls data from multiple sources to a unifying layer and stored in a unity catalog.
- Previously it was tough to unify all the data together. Now there is a tool to bind them all.
- Can be used at every stage of the pipeline (eg, ingestion, cleaning, modelling, visualizations, machine learning, etc)
- As data engineer working in a project, my role is to pull the required data (single or multiple sources) and get it ready for downstream users' (business user / data analyst / data scientist / AI engineer) consumption.

## 😶 My thought process in dealing with blanks and NULLS
- crm_customers: 
  Rows with empty customer_ID have been removed as creation_date is also empty.
  Marital_Status and Customer_Gender had some missing fields but were not excluded as they have a Creation_Date and counts for a valid data point.
- crm_product: 
  Product_Cost, Product_Line and Product_End_Date have a few nulls. I included everything in as data integrity is not compromised.
- crm_sales: 
  There weren't many blanks and NULLS. I included everything as data integrity is not compromised.
- erp_customer: 
  Some blanks and NULLS but I included everything as data integrity is not compromised.
- erp_locations: 
  Some blanks and NULLS but I included everything as data integrity is not compromised.
- erp_categories: 
  Perfect dataset with 0 blanks and NULLS. Hence, everything is included.

## :x: Limitations
1. No visualizations and predictions (or at least not yet).

Difficulty Level: 6️⃣

<img width="2277" height="1834" alt="Bike_Lakehouse_Architecture" src="https://github.com/user-attachments/assets/f8c4a9c4-c4c6-496a-a383-46d9f4fb077f" />
