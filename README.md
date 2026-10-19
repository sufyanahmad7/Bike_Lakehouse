Working on a data engineering project with Databricks using the Medallion Architecture with the 3 layers - bronze, silver and gold. It is still a work in daily progress. In the meantime, here is the architecture.

No business objectives were defined as I am using this project to learn Databricks and data engineering concepts.

My thoughts / reflection so far
- Databricks is platform that pulls data from multiple sources to a unifying layer and stored in a unity catalog.
- Previously it was tough to unify all the data together. Now there is a tool to bind them all.
- Can be used at every stage of the pipeline (eg, ingestion, cleaning, modelling, visualizations, machine learning, etc)
- As data engineer working in a project, my role is to pull the required data (single or multiple sources) and get it ready for downstream users' (business user / data analyst / data scientist / AI engineer) consumption.

My thought process in dealing with blanks and NULLS
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

Tasklist
- Illustrate and upload architecture (DONE)
- Clean CRM datasets to Silver (DONE)
- Clean ERP datasets to Silver (DONE)
- Create data model (star schema) >>> 1 fast file + 2 dimension files (DONE)
- Automate the data pipeline with jobs
- Create visualizations
- Perhaps do sales forecasting


<img width="2277" height="1834" alt="Bike_Lakehouse_Architecture" src="https://github.com/user-attachments/assets/f8c4a9c4-c4c6-496a-a383-46d9f4fb077f" />
