import streamlit as st
import plotly.express as px
import seaborn as sns

# Load the Iris dataset
iris_df = sns.load_dataset("iris")

# title 
st.title("3D Scatter Plot of Iris Dataset")

# Create a 3D scatter plot 
fig = px.scatter_3d(iris_df, x='petal_width', y='sepal_width', z='petal_length', color='species')


st.plotly_chart(fig) # show the figure 