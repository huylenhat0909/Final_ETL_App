# Table Change Log

| Version | Date       | Description |
|---------|------------|-------------|
| 1.1.0   | 10/05/2024 | - Revised entire documentation content<br> - Conducted analysis based on specific questions:<br>   ◦ Identified data returned from Query API<br>   ◦ Determined Query API response time<br>   ◦ Assessed data volume and scope<br>   ◦ Defined problems to be addressed<br>   ◦ Identified data required for problem-solving<br> - Removed Data Staging and ERD model design for staging database<br> - Designed ELT model with Data Lake and Data Mart |
| 1.2.0   | 13/05/2024 | - Edited documentation focusing on NYSE and NASDAQ data<br>   ◦ Updated data volume based on scope<br> - Split 4 APIs into 2 APIs and 1 Database storing data from sec-api.io and Alpha Vantage API for market status (simulated backend database)<br>   ◦ Designed Database for data from sec-api.io and Alpha Vantage API for market status<br> - Redesigned ELT to include new Database as a Data Source<br> - Modified Galaxy Schema<br>   ◦ Optimized query time with a single Dim Companies table |
| 1.2.1   | 16/05/2024 | - Identified ETL components<br> - Added design elements:<br>   ◦ Designed DAG and Task Flow<br>   ◦ Designed Job Data Flow<br>   ◦ Created BPMN ETL<br>   ◦ Structured File System |
| 1.2.2   | 28/05/2024 | - Migrated Data Warehouse to DuckDB<br> - Updated ETL process:<br>   ◦ Database -> Data Lake -> Data Warehouse<br>   ◦ Implemented timestamp for database updates |
| 1.3     | 03/06/2024 | - Configured project environment<br> - Installed and configured Google Compute Engine<br> - Installed and configured Hadoop (Single Node) - HDFS, YARN<br> - Installed and configured Python, PostgreSQL, DuckDB<br> - Installed and configured Spark on Hadoop cluster |
| 1.6     | 07/06/2024 | - Initialized functionality:<br>   ◦ ETL for Database<br>   ◦ ELT for Data Warehouse<br>   ◦ Created DAGs<br>   ◦ Developed API for Data Warehouse access |
| 1.7     | 14/06/2024 | - Launched project:<br>   ◦ Started Airflow<br>   ◦ Activated API |
| 1.8 (Processing) | 15/06/2024 | - Designed Dashboard:<br>   ◦ Identified and designed Dashboard<br>   ◦ Extracted data via API<br>   ◦ Loaded data into Power BI<br>   ◦ Created Dashboard |
| 1.9 (Upcoming)   |            |             |


# Docs Link: 
https://anhcuonghuynhnguyen.notion.site/T-i-li-u-d-n-ELT_Pipeline_Stock-v1-8-4f4289c245a647f6a2879ca171ee5b2b?pvs=4 