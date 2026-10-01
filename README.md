Working on a data engineering project with Databricks using the Medallion Architecture with the 3 layers - bronze, silver and gold. It is still a work in daily progress. In the meantime, here is the architecture.

No business objectives were defined as I am using this project to learn Databricks and data engineering concepts.

My thoughts so far
- Databricks is platform that pulls data from multiple sources to a unifying layer and stored in a unity catalog.
- Previously it was tough to unify all the data together. Now there is a tool to bind them all.
- Can be used at every stage of the pipeline (eg, ingestion, cleaning, modelling, visualizations, machine learning, etc)
- As data engineer working in a project, my role is to pull the required data (single or multiple sources) and get it ready for the next person (business user / data analyst / data scientist / AI engineer) to use.

Tasklist
- Illustrate and upload architecture (DONE)
- Clean datasets to Silver
- Create data model (star schema) >>> 1 fast file + 2-3 dimension files
- Perhaps explore other data models
- Create visualizations
- Perhaps do sales forecasting


<img width="2277" height="1834" alt="Bike_Lakehouse_Architecture" src="https://github.com/user-attachments/assets/f8c4a9c4-c4c6-496a-a383-46d9f4fb077f" />
