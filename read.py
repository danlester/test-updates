import streamlit as st
import pandas as pd

st.write('My version number is 2')

df = pd.read_csv("data.csv")

st.write(df)



