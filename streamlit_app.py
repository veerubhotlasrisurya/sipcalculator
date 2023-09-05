import numpy as np
import streamlit as st
from matplotlib import pyplot as plt
import plotly.express as px
import pandas as pd
st.title("SIP Calculator")


try:
    monthlyamt = float(st.number_input("Monthly SIP Amount:"))
    

except (ZeroDivisionError, ValueError):
    st.write("Please enter Amount, Rate and Period")

rate = float(st.slider("Expected Rate of Return:",min_value=1, max_value=50))
years = st.slider("No of Years:",min_value=1, max_value=100)
months = years * 12
monthlyrate = rate/12/100
futurevalue = monthlyamt*((((1 + monthlyrate)**(months))-1) * (1 + monthlyrate))/monthlyrate
futurevalue = round(futurevalue)
investedamt = monthlyamt*months
profit = round(futurevalue - investedamt)

headers = ['Invested Amount','Profit']
headers_data = [investedamt,profit]

col1,col2 = st.columns(2)
with col1:
    st.header("Invested Amount : ")
    st.subheader(investedamt)
    st.header("Maturity Amount : ")
    st.subheader(futurevalue)
    st.header("Profit Amount : ")
    st.subheader(profit)

with col2:
    if monthlyamt > 0:
        df = pd.DataFrame(
            {'Particulars': headers,
             'Amount': headers_data
            })
        fig = px.pie(df, values='Amount', names='Particulars',title='SIP Pie Chart',width=300, height=350)
        fig.update_traces(textposition='inside')
        st.write(fig)
