import streamlit as st
from typing import Literal
import numpy as np
import pandas as pd

# WHAT IS AN EXOPLANET?
# What is Transit photometry?
# 

dataframe_path = r'src/data/keplar.csv'

df = pd.read_csv('src/data/keplar.csv')
print(df)
# st.dataframe(df)