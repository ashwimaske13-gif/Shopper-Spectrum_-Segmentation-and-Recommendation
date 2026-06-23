# ```python

import streamlit as st
import pandas as pd
import pickle
from streamlit_option_menu import option_menu

# -----------------------------------
# Page Config
# -----------------------------------

st.set_page_config(
    page_title="Shopper Spectrum",
    page_icon="🛒",
    layout="wide"
)

# -----------------------------------
# Load Files
# -----------------------------------

@st.cache_resource
def load_files():

    with open("kmeans_model.pkl", "rb") as f:
        kmeans = pickle.load(f)

    with open("scaler.pkl", "rb") as f:
        scaler = pickle.load(f)

    with open("product_list.pkl", "rb") as f:
        product_list = pickle.load(f)

    similarity_df = pd.read_pickle("product_similarity_df.pkl")
    rfm_df = pd.read_pickle("rfm_df.pkl")

    return kmeans, scaler, product_list, similarity_df, rfm_df


try:
    kmeans, scaler, product_list, similarity_df, rfm_df = load_files()

except Exception as e:
    st.error(f"Error loading files: {e}")
    st.stop()

# -----------------------------------
# Sidebar
# -----------------------------------

with st.sidebar:
    selected = option_menu(
        "Shopper Spectrum",
        [
            "Home",
            "Customer Segmentation",
            "Product Recommendation"
        ],
        icons=[
            "house",
            "people",
            "cart"
        ],
        default_index=0
    )

# -----------------------------------
# Home Page
# -----------------------------------

if selected == "Home":

    st.title("🛒 Shopper Spectrum")

    st.markdown("""
    ### Customer Segmentation & Product Recommendation System

    This project helps businesses:

    - Segment customers using RFM Analysis
    - Identify high-value customers
    - Identify at-risk customers
    - Recommend products using Collaborative Filtering

    ### Technologies Used

    - Python
    - Pandas
    - Scikit-Learn
    - KMeans Clustering
    - Streamlit
    """)

    st.subheader("Dataset Overview")

    st.dataframe(rfm_df.head())

# -----------------------------------
# Customer Segmentation
# -----------------------------------

elif selected == "Customer Segmentation":

    st.title("👥 Customer Segmentation")

    recency = st.number_input(
        "Recency",
        min_value=0,
        value=30
    )

    frequency = st.number_input(
        "Frequency",
        min_value=0,
        value=5
    )

    monetary = st.number_input(
        "Monetary",
        min_value=0.0,
        value=500.0
    )

    if st.button("Predict Segment"):

        sample = pd.DataFrame(
            [[recency, frequency, monetary]],
            columns=["Recency", "Frequency", "Monetary"]
        )

        scaled = scaler.transform(sample)

        cluster = kmeans.predict(scaled)[0]

        segment_map = {
            0: "High Value Customer",
            1: "Regular Customer",
            2: "Occasional Customer",
            3: "At Risk Customer"
        }

        st.success(f"Predicted Cluster: {cluster}")

        st.info(
            segment_map.get(
                cluster,
                "Customer Segment"
            )
        )

# -----------------------------------
# Product Recommendation
# -----------------------------------

elif selected == "Product Recommendation":

    st.title("🎯 Product Recommendation")

    selected_product = st.selectbox(
        "Select Product",
        product_list
    )

    if st.button("Recommend Products"):

        try:

            similar_products = (
                similarity_df[selected_product]
                .sort_values(ascending=False)[1:6]
            )

            st.subheader("Recommended Products")

            for product in similar_products.index:
                st.write("✅", product)

        except Exception as e:
            st.error(
                f"Recommendation Error: {e}"
            )

