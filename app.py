import streamlit as st
import pandas as pd
from recommendation import recommend

# load dataset
df = pd.read_csv("cleaned_data.csv")

st.title("🍽️ Swiggy Restaurant Recommendation System")

st.write("Select a restaurant to get similar recommendations")

# dropdown
restaurant = st.selectbox(
    "Choose Restaurant",
    df['name']
)

# button
if st.button("Recommend Restaurants"):

    index = df[df['name'] == restaurant].index[0]

    results = recommend(index)

    st.subheader("Recommended Restaurants")

    st.write(results)