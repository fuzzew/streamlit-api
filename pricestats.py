import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

@st.cache
def load_data():
    return pd.read_csv('output.csv')

data = load_data()

st.title('Vehicle Price Analysis Tool')

brand_selected = st.selectbox('Select Brand', data['brand'].unique())
models_for_brand = data[data['brand'] == brand_selected]['model'].unique()
model_selected = st.selectbox('Select Model', models_for_brand)

data_filtered = data[(data['brand'] == brand_selected) & (data['model'] == model_selected)]

st.header(f'Price vs. Age for {brand_selected} {model_selected}')
fig, ax = plt.subplots()
sns.scatterplot(x='age', y='price', data=data_filtered, ax=ax)
plt.title('Price Trend Over Age')
st.pyplot(fig)


st.header(f'Price vs. Model for {brand_selected}')
same_brand_data = data[data['brand'] == brand_selected]
fig, ax = plt.subplots()
sns.boxplot(x='price', y='model', data=same_brand_data)
plt.title('Price Distribution Across Models')
st.pyplot(fig)

st.header(f'Price vs. Kilometers for {brand_selected} {model_selected}')
fig, ax = plt.subplots()

sns.scatterplot(x='km', y='price', data=data_filtered, ax=ax)

sns.regplot(x='km', y='price', data=data_filtered, scatter=False, ax=ax, color='red', ci=None)

plt.title('Price vs. Kilometers Driven')
st.pyplot(fig)

avg_price = int(round(data_filtered['price'].mean(), -3))
st.header(f'Average Selling Price for {brand_selected} {model_selected}')
st.write(f'The average selling price is: ₹{avg_price}')
