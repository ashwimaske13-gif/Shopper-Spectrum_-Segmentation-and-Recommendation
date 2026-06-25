Project Overview
Modern e-commerce platforms generate large volumes of transaction data, but raw data alone does not provide business value. This project transforms raw transaction data into meaningful insights by:

Segmenting customers based on purchasing behavior
Identifying high-value, regular, occasional, and at-risk customers
Recommending similar products based on historical co-purchase patterns
The solution supports data-driven marketing, personalization, and customer retention strategies.

🎯 Objectives
Perform data cleaning and preprocessing
Engineer RFM (Recency, Frequency, Monetary) features
Build a clustering model for customer segmentation
Build a product recommendation system
Deploy models using a Streamlit web application
🧠 Machine Learning Techniques Used
Unsupervised Learning (K-Means Clustering)
RFM Analysis
Item-Based Collaborative Filtering
Cosine Similarity
Quantile Transformer (Data Scaling)
📂 Dataset Information
The dataset contains online retail transaction records with the following key columns:

InvoiceNo – Transaction ID
StockCode – Product code
Description – Product name
Quantity – Number of items purchased
InvoiceDate – Date and time of purchase
UnitPrice – Price per item
CustomerID – Unique customer identifier
Country – Customer location
🛠 Data Preprocessing Steps
Removed missing CustomerID values
Removed cancelled invoices
Removed negative and zero quantity/price records
Created TotalPrice feature
🔧 Feature Engineering
RFM features created per customer:

Recency – Days since last purchase
Frequency – Number of purchases
Monetary – Total spending
Additional engineered features:

Monetary_per_Transaction
Recency_Frequency_Ratio
📊 Customer Segmentation
K-Means clustering applied on scaled RFM features
Optimal number of clusters selected using Elbow Method and Silhouette Score
Customer Segments:

High-Value Customers
Regular Customers
Occasional Customers
At-Risk Customers
🤝 Product Recommendation System
Item-based collaborative filtering
Customer–product interaction matrix
Cosine similarity between products
Returns top 5 similar products for a given product
📈 Model Evaluation
Silhouette Score for clustering quality
Qualitative validation of product recommendations
🌐 Streamlit Web Application Features
Home
Project overview
Customer Segmentation Module
Inputs: Recency, Frequency, Monetary
Output: Predicted cluster and customer segment
Product Recommendation Module
Input: Product name
Output: Top 5 similar product recommendations
