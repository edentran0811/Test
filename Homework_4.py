# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 12:18:41 2021

@author: trant
"""

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Question 1 #
st.title("Welcome to Math 10")

# Question 2 #
st.write("Name: Eden Tran")
link = "[Eden Tran's GitHub](https://github.com/edentran0811)"
st.markdown(link, unsafe_allow_html=True)

# Question 3 #
upload_file = st.sidebar.file_uploader(label="Upload Your CSV File Here",type=['csv'])

# Question 4 #
# We want to convert the file to a pandas df
# But there will be an error if we don't have an uploaded file
if upload_file is not None:
    df = pd.read_csv(upload_file)
    # If x is an empty string, make it numpy's not-a-number, otherwise leave x alone
# Question 5 #
    df = df.applymap(lambda x: np.nan if x == " " else x)
    
# Question 6 #
# Let c be the column name (Week 3 Friday Lecture)
    def can_be_numeric(c):
        try:
            pd.to_numeric(df[c])
            return True
        except:
            return False
# Now let's make a list of all the columns that can be made numeric
    good_cols = [c for c in df.columns if can_be_numeric(c)]
    
# Question 7 #
# Replace columns in df that can be made numeric with their numeric values
    df[good_cols] = df[good_cols].apply(pd.to_numeric, axis = 0)

# QUestion 8 #
# Select x-axis and y-axis from st.selectbox
    x_axis = st.selectbox("Choose your x-value:", good_cols)
    y_axis = st.selectbox("Choose your y-value:", good_cols)
    
# Questiom 9 #
    row_slider = st.slider("Choose the number of rows:", min_value = 0,
                           max_value = len(df.index))
    
# Question 10 #
    st.write(f"The chosen x-axis is {x_axis}")
    st.write(f"The chosen y-axis is {y_axis}")
    
# Question 11 #
    my_chart = alt.Chart(df).mark_square().encode(
        x = x_axis,
        y = y_axis)
    st.altair_chart(my_chart)
    
# Question 12 #
choice = ['Yes', 'No']
like = st.radio("Do you like my app?", choice)
if (like == 'Yes'):
    st.write("Thank you!")
else:
    st.write("I'll try harder next time!")
    



