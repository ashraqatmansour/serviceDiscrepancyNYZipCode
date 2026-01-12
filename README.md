# NYC 311 Service Discrepancy Dashboard

An interactive data analysis project exploring NYC 311 service complaints, with a focus on response time discrepancies across zip codes, boroughs, and time. The project combines data preprocessing, exploratory analysis, and visualization using Python, Pandas, and Bokeh.


---
## How to Run the Project
1. Clone the repository:https://github.com/ashraqatmansour/serviceDiscrepancyNYZipCode
2. Install required dependencies:pip install pandas numpy bokeh jupyter
3. Launch the Bokeh dashboard: bokeh serve --show dashboard.py

## Project Overview

NYC’s 311 system collects millions of service requests each year. This project analyzes that public dataset to identify spatial and temporal patterns in complaint volume and service response, highlighting potential disparities across neighborhoods.

The analysis includes:
- Monthly aggregation of complaints
- Borough-level comparisons
- Seasonal trends in specific complaint types
- Interactive visualizations for data exploration

---

## Visualizations and Analysis

The project generates the following key graphs:

### Seasonal Comparison: Heat and Hot Water Complaints
- Comparison of Heat and Hot Water complaints in February versus June
- Demonstrates strong seasonal demand differences, with significantly higher complaint volumes during winter months

### Most Common Complaint Types
- Visualization of the most frequently reported NYC 311 complaint categories
- Provides insight into which issues dominate service requests citywide

### Borough-Level Complaint Aggregation
- Aggregates complaint volumes by borough
- Enables comparison of reporting patterns across different areas of New York City

---

## Tools and Technologies

- Python
- Pandas and NumPy for data preprocessing and aggregation
- Bokeh for interactive visualizations and dashboard development
- Jupyter Notebook for exploratory data analysis
- NYC Open Data (311 Service Requests dataset)

---

## Data Processing

- Cleaned and filtered large-scale NYC 311 public datasets
- Computed monthly averages and response-time related metrics
- Grouped complaints by zip code, borough, and complaint type
- Prepared structured datasets for visualization and comparison

## Key Findings

- Complaint volume and type vary significantly by season and borough
<img width="553" height="381" alt="mostCommonComplaint" src="https://github.com/user-attachments/assets/f2fe14df-9858-4ef3-a9f5-5610c3393e2f" />

  
- Heat and hot water complaints peak during winter months
<img width="590" height="413" alt="hotwaterComplaints2024" src="https://github.com/user-attachments/assets/6c5d66ca-18f6-4d09-b775-94f2f2d79f53" />

  
- A small set of complaint categories consistently account for a large share of NYC 311 requests



