# Customer-Segmentation-Retention-Analysis-for-SNB
An end-to-end Data Science pipeline for SNB bank customer segmentation using RFM analysis and K-Means clustering, featuring an interactive cohort retention Power BI dashboard.

## Project Overview
This project focuses on driving data-driven growth and maximizing customer loyalty at the Saudi National Bank (SNB). By implementing advanced data analytics and machine learning, the project aims to minimize customer churn, optimize marketing spend, and increase overall banking revenue through personalized customer retention strategies.

## Dataset Description
* **Data Type:** Synthetic / Simulated Banking Data.
* **Volume:** 5,000 unique customer profiles.
* **Rationale:** The dataset was custom-engineered to mirror the mathematical distribution (including normal and skewed behaviors) of the Saudi banking sector while strictly respecting data privacy and security regulations (SDAIA & SAMA guidelines).

* ##  Data Science Pipeline

1. **Data Collection & Preparation:** Processed customer transaction history using `Pandas` and `NumPy`, handled missing values, converted dates, and engineered key behavioral features.
2. **RFM Modeling:** Built an RFM framework utilizing `pd.qcut` to rank customer Recency, Frequency, and Monetary metrics on a scalable score from 1 to 5.
3. **Customer Segmentation:** Applied `StandardScaler` to normalize features and executed **K-Means Clustering** to divide the customer base into 6 distinct behavioral profiles.
4. **Retention & Churn Analysis:** Developed a monthly **Cohort Analysis** pipeline to track customer retention rate percentages and pinpoint exact drop-off periods.
5. **Visualization & Reporting:** Designed an interactive, dark-themed Power BI dashboard featuring dynamic cohort heatmaps, RFM density distributions, and product ownership trends.
6. **Strategic Action Plan:** Translated analytical outputs into automated, business-ready marketing recommendations targeted at each specific segment.

## Dashboard Preview
![SNB Customer Intelligence Dashboard]([
])

##  Key Business Insights & Action Plan
Based on the dashboard analytics, the following strategic steps were established:
* **Champions (57.6% Revenue Contribution):** Must be rewarded with premium wealth products and referral incentives to maintain high engagement.
* **At Risk Customers (6.8% Revenue Contribution):** Require immediate retention offers, proactive customer service calls, and tailored financial incentives before churning.
* **Lost Customers (9.9% Revenue Contribution):** Can be targeted with targeted "Win-back" campaigns (e.g., specialized SAR 500 return offers) to re-establish banking activity.

*  Technology Stack
* **Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-Learn, Seaborn, Matplotlib
* **BI Tool:** Power BI

  
