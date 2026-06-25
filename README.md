# 🛒 Shopper Spectrum: Customer Segmentation & Product Recommendation System

An end-to-end Machine Learning project that analyzes e-commerce transaction data to segment customers using RFM analysis and recommend similar products using item-based collaborative filtering. The project also includes a Streamlit web application for real-time interaction.

---

## 📌 Project Overview

Modern e-commerce platforms generate large volumes of transaction data, but raw data alone does not provide business value. This project transforms raw transaction data into meaningful insights by:

* Segmenting customers based on purchasing behavior
* Identifying high-value, regular, occasional, and at-risk customers
* Recommending similar products based on historical co-purchase patterns

The solution supports data-driven marketing, personalization, and customer retention strategies.

---

## 🎯 Objectives

* Perform data cleaning and preprocessing
* Engineer RFM (Recency, Frequency, Monetary) features
* Build a clustering model for customer segmentation
* Build a product recommendation system
* Deploy models using a Streamlit web application

---

## 🧠 Machine Learning Techniques Used

* Unsupervised Learning (K-Means Clustering)
* RFM Analysis
* Item-Based Collaborative Filtering
* Cosine Similarity
* Quantile Transformer (Data Scaling)

  #### 📌 Dataset Description

| Column      | Description                                |
| :---------- | :----------------------------------------- |
| `InvoiceNo` | Transaction number                         |
| `StockCode` | Unique product/item code                   |
| `Description` | Name of the product                        |
| `Quantity`  | Number of products purchased               |
| `InvoiceDate` | Date and time of transaction (2022–2023) |
| `UnitPrice` | Price per product                          |
| `CustomerID`| Unique identifier for each customer        |
| `Country`   | Country where the customer is based        |

### Step 2: 📌 Data Preprocessing

* Remove rows with missing `CustomerID`.
* Exclude cancelled invoices (`InvoiceNo` starting with 'C').
* Remove negative or zero quantities and prices.

### Step 3: 📌 Exploratory Data Analysis (EDA)

* Analyze transaction volume by country.
* Identify top-selling products.
* Visualize purchase trends over time.
* Inspect monetary distribution per transaction and customer.
* RFM distributions.
* Elbow curve for cluster selection.
* Customer cluster profiles.
* Product recommendation heatmap / similarity matrix.

### Step 4: 📌 Clustering Methodology

1.  **Feature Engineering:**
    * Calculate Recency = Latest purchase date in dataset − Customer’s last purchase date
    * Calculate Frequency = Number of transactions per customer
    * Calculate Monetary = Total amount spent by customer
2.  **Standardize/Normalize** the RFM values.
3.  **Choose Clustering Algorithm** (KMeans, DBScan, Hierarchical etc.).
4.  Use **Elbow Method** and **Silhouette Score** to decide the number of clusters.
5.  **Run Clustering**.
6.  **Label the clusters** by interpreting their RFM averages:

    | Cluster                | Characteristics                       | Segment Label |
    | :--------------------- | :------------------------------------ | :------------ |
    | High R, High F, High M | Regular, frequent, recent, big spenders | **High-Value**|
    | Medium F, Medium M     | Steady purchasers but not premium     | **Regular** |
    | Low F, Low M, older R  | Rare, occasional purchases            | **Occasional**|
    | High R, Low F, Low M   | Haven’t purchased in a long time      | **At-Risk** |

7.  **Visualize the clusters** using a scatter plot or 3D plot of RFM scores.
8.  **Save the best performing model** for Streamlit usage.

### 📌 Recommendation System Approach

* Use **Item-based Collaborative Filtering**.
* Compute **cosine similarity** (or another similarity metric) between products based on purchase history (`CustomerID–StockCode` matrix).
* Return **top 5 similar products** to the entered product name.

## 📱 Streamlit App Features

### 🎯 1️⃣ Product Recommendation Module

**Objective:** When a user inputs a product name, the app recommends 5 similar products based on collaborative filtering.

**Functionality:**

* Text input box for Product Name
* Button: `Get Recommendations`
* Display 5 recommended products as a styled list or card view

### 🎯 2️⃣ Customer Segmentation Module

**🔍 Functionality:**

* 3 number inputs for:
    * Recency (in days)
    * Frequency (number of purchases)
    * Monetary (total spend)
* Button: `Predict Cluster`
* Display: Cluster label (e.g., High-Value, Regular, Occasional, At-Risk)


## 📁 Project Structure

```
Shopper-Spectrum/
│
├── Shopper_Spectrum_Clustering_Product_Recommendation.ipynb
├── app.py
├── kmeans_model.pkl
├── scaler.pkl
├── product_similarity_df.pkl
├── product_list.pkl
├── rfm_df.pkl
├── README.md
```

---

## 📌 Business Impact

* Enables targeted marketing
* Improves customer retention
* Increases cross-selling and upselling
* Enhances personalized shopping experience

---

## 🧾 Conclusion

This project demonstrates an end-to-end machine learning pipeline from raw data to deployment, providing actionable insights for e-commerce businesses through customer segmentation and product recommendation.

