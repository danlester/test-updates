import streamlit as st
import pandas as pd

st.write('My version number is 1')

df = pd.read_csv("data.csv")

st.write(df)



