import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
import plotly.express as px
st.markdown("# Insurance Charges Exploration")
with st.expander(  "# Why are we doing this?"):
    st.write("In a recent survey conducted by Gallup and West Health, an estimated 112 million Amercians (44%) struggle to pay for [healthcare](https://www.westhealth.org/press-release/112-million-americans-struggle-to-afford-healthcare/#:~:text=WASHINGTON%2C%20D.C.%20%E2%80%94%20Mar.,is%20not%20worth%20the%20cost)."
            " National health spending is over 4 trillion in this country, and current projections indicate it will continue to grow at an annual rate of 5.4%, topping $6.2 trillion by 2028. "
             " The goal of this application  at a future date is too allow the user to input information about themselves and determine factors that impact their insurance rate."
             " Please note that there are several factors that this dataset does not include that may contribute to the cost of insurance. ")
st.sidebar.write("[Github Repo](https://github.com/henrytr2/Midterm_project)")
st.sidebar.write("## Dataset Info")
st.sidebar.write("This dataset contains information about insurance charges across different regions of the United States.")
st.sidebar.write("Let's explore the data and see if we can find any interesting details!")
show_column_info = st.sidebar.checkbox("Show Column Info")
if show_column_info:
    column_info = {
        'age': 'Age of the insured person',
        'sex': 'Gender of the insured person (male or female)',
        'bmi': 'Body Mass Index (BMI) of the insured person',
        'children': 'Number of children or dependents covered by the insurance',
        'smoker': 'Whether the insured person is a smoker (Yes or No)',
        'region': 'Region in the United States of the insured person'
    }
    st.sidebar.write("## Column Information")
    for col, desc in column_info.items():
        st.sidebar.write(f"- **{col}**: {desc}")
# load data
insurance = pd.read_csv("insurance.csv")

click_here = st.selectbox('Please select the dataset:', ['Insurance'])

if click_here == 'Insurance':
    df1 = insurance
    st.write("Let's look at some of the Raw Data!")

data_preview = st.checkbox("View Data Table")
if data_preview:
    st.write("## Dataset Preview")
    st.write(insurance.head())
    
    # Check for missing values
    missing_values = df1.isnull().sum()
    st.write("### Missing Values")
    st.write(missing_values)
    st.write("*We see that there are no missing values.*")
df = df1

button1 = st.checkbox("Show Statistics")
if button1:
    st.write(df.describe())
cols = df.columns

st.write("## Data Visualization")

# Basic Dists 

show_histogram = st.checkbox("Age")

if show_histogram:
    fig = px.histogram(insurance, x='age', marginal='box', nbins=64, title='Distribution of Age',)
    st.plotly_chart(fig, use_container_width=True)

st.write("**What Variables do you want to investigate?**")
x_val = st.selectbox('Variable on the x-axis?', cols)
y_val = st.selectbox('Variable on the y-axis?', cols)
z_val = st.selectbox('Do you want a hue?', cols)

button3 = st.button("Bar Chart")
if button3:
    st.bar_chart(data=df, x=x_val, y=y_val)

if st.button("Hide Bar Chart"):
    button3 = False

button4 = st.button("Scatter Plot")
if button4:
    scatter_fig = px.scatter(df, x=x_val, y=y_val, color=z_val)
    st.plotly_chart(scatter_fig, use_container_width=True)

if st.button("Hide Scatter Plot"):
    button4 = False

st.write("We have looked at some of the information regarding the insurance dataset. Please come back later when the project is finished!")



